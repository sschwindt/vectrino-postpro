"""
Read flow velocity data from Nortek Vectrino II output (.ntk) files
"""
import numpy as np
import pandas as pd


def read_ascii_file(file_name):
    """Read the contents of a Vectrino II ASCII .dat file. Currently, only the velocity beams 1 to 4 and their SNR is
        parsed. Other parameters like Correlation can be easily added.

    :param str file_name: Path and name of the NTK ASCII files. For example use 'sample-data/VectrinoProfiler.00001' to
                        read 'VectrinoProfiler.00001.ntk.dat' in the sample-data sub-folder.
    :return pd.DataFrame: DataFrame containing the beam velocities and SNR of the four beams
    """
    # initialize lists for data storage
    time_list = []
    velocity_beam_1 = []
    velocity_beam_2 = []
    velocity_beam_3 = []
    velocity_beam_4 = []
    snr_beam_1 = []
    snr_beam_2 = []
    snr_beam_3 = []
    snr_beam_4 = []
    print('   - reading ' + file_name.strip('.ntk.dat') + '.ntk.dat')
    # read file and make sure there is no issue with the file ending
    with open(file_name.strip('.ntk.dat') + '.ntk.dat', 'r') as file:
        current_time = None
        current_velocities = {}
        current_snr = {}

        for line in file:
            # extract time
            if 'Profiles_HostTime_start (s)' in line:
                current_time = float(line.split(':')[-1].strip())

            # check for Beam Velocity lines
            elif 'Profiles_Velocity_Beam_' in line:
                # get beam number
                beam_number = int(line.split('Profiles_Velocity_Beam_')[1].split()[0])
                # Extract the velocities for the current beam
                velocities = line.split(':')[-1].strip().strip('[]').split()
                current_velocities[beam_number] = [float(v) for v in velocities]

            # check for SNR lines
            elif 'Profiles_SNR_Beam_' in line:
                # get beam number
                beam_number = int(line.split('Profiles_SNR_Beam_')[1].split()[0])
                # Extract the velocities for the current beam
                snr = line.split(':')[-1].strip().strip('[]').split()
                current_snr[beam_number] = [float(sig) for sig in snr]

            # append relevant data to the lists
            if len(current_velocities) == 4:
                time_list.append(current_time)
                velocity_beam_1.append(current_velocities[1])
                velocity_beam_2.append(current_velocities[2])
                velocity_beam_3.append(current_velocities[3])
                velocity_beam_4.append(current_velocities[4])
                # reset for the next profile
                current_velocities = {}

                if len(current_snr) == 4:
                    snr_beam_1.append(current_snr[1])
                    snr_beam_2.append(current_snr[2])
                    snr_beam_3.append(current_snr[3])
                    snr_beam_4.append(current_snr[4])
                else:
                    snr_beam_1.append(np.nan)
                    snr_beam_2.append(np.nan)
                    snr_beam_3.append(np.nan)
                    snr_beam_4.append(np.nan)
                # reset for the next profile
                current_snr = {}

    return pd.DataFrame({
        'Time (s)': time_list,
        'Velocity Beam 1 (m/s)': velocity_beam_1,
        'Velocity Beam 2 (m/s)': velocity_beam_2,
        'Velocity Beam 3 (m/s)': velocity_beam_3,
        'Velocity Beam 4 (m/s)': velocity_beam_4,
        'SNR Beam 1 (dB)': velocity_beam_1,
        'SNR Beam 2 (dB)': velocity_beam_2,
        'SNR Beam 3 (dB)': velocity_beam_3,
        'SNR Beam 4 (dB)': velocity_beam_4,
    })


# print(df.head())
# print(df.describe())
# df.to_csv('velocity_profile_data.csv', index=False)


# Display the DataFrame to the user
# import ace_tools as tools;

 #tools.display_dataframe_to_user(name="Velocity Profile Data", dataframe=df)
