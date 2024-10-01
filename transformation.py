"""Retrieve transformation matrix to transform beam signals into velocities with Cartesian coordinates"""
import numpy as np
import pandas as pd


def get_transformation_matrix(ntk_file_name, scaling_factor=4096):
    """ Read the transformation matrix as numpy array from the

    :param str ntk_file_name: Path and name of a Vectrino II ntk file. For example 'data/VectrinoProfiler.00001' when
                            the header file is 'VectrinoProfiler.00001.ntk.hdr' (see 'sample-data/' directory).
    :param int scaling_factor: This number can be found in the hdr file on line 186 (or so) and is typically device
                                specific.
    :return np.array M: The transformation matrix.
    """
    # initialize hBeamToXYZ
    hBeamToXYZ = []
    # retrieve hBeamToXYZ values from header file
    with open(ntk_file_name.strip('.ntk.hdr') + '.ntk.hdr', 'r') as file:
        for line in file:
            if 'Probe_hBeamToXYZ' in line:
                # extract probe transformation
                line_str_list = line.split(':')
                if len(line_str_list) > 1:
                    # this is required to avoid that the description lower in the header file is mistaken as transformation
                    Probe_hBeamToXYZ = line_str_list[-1].strip().strip('[]').split()
                    hBeamToXYZ = [float(e) for e in Probe_hBeamToXYZ]

    if len(hBeamToXYZ) > 0:
        # convert hBeamToXYZ list into a 4x4 np.array (matrix) by dividing each element by the scaling factor
        return np.array(hBeamToXYZ).reshape(4, 4) / scaling_factor
    else:
        # error!
        print('ERROR: Could not read transformation matrix from the header file.')
        return -1


def apply_transformation(
        df,
        transformation_matrix,
        relevant_point_ids=(0, 1, 2),
):
    """Apply a transformation matrix to a pandas DataFrame containing Vectrino II ASCII data.

    :param pd.DataFrame df: This DataFrame must have the following column headers with lists of floats:
                            Velocity Beam 1 (m/s), Velocity Beam 2 (m/s), Velocity Beam 3 (m/s), Velocity Beam 4 (m/s);
                            The DataFrame can be created with get_ascii_data.read_ascii_file(file_name).
    :param np.array(4x4) transformation_matrix: Provide the transformation matrix calculated with the
                            get_transformation_matrix(file_name) function.
    :param tuple relevant_point_ids: Specify a tuple of relevant point IDs from each measurement time step. The default
                        is (0,1,2) and  forces the function to use point IDs 0, 1, and 2. Note that counting starts at 0
                        and using more IDs or IDs beyond the number of measured points will cause an error that will
                        stop the script.
    :return pd.DataFrame: Returns the input DataFrame with 3d u, v, and w flow velocity components appended.
    """
    if len(relevant_point_ids) == 0:
        raise ValueError('ERROR: Invalid argument for list relevant_point_ids provided.')

    points_per_measurement = len(df.loc[0, 'Velocity Beam 1 (m/s)'])
    print('   - found ' + str(points_per_measurement) + ' points per measurement')
    print('   - applying transformation...')
    # initiate Cartesian velocity vectors as lists
    u = []
    v = []
    w1 = []
    w2 = []

    for i in range(len(df)):
        # read beam velocities
        beam_velocities_1 = df.loc[i, 'Velocity Beam 1 (m/s)']
        beam_velocities_2 = df.loc[i, 'Velocity Beam 2 (m/s)']
        beam_velocities_3 = df.loc[i, 'Velocity Beam 3 (m/s)']
        beam_velocities_4 = df.loc[i, 'Velocity Beam 4 (m/s)']

        # initialize lists to collect the three u, v, w values for each measurement
        u_values = []
        v_values = []
        w1_values = []
        w2_values = []

        # loop over the three values in each list
        for j in range(points_per_measurement):
            beam_velocities = np.array([
                beam_velocities_1[j],
                beam_velocities_2[j],
                beam_velocities_3[j],
                beam_velocities_4[j]
            ])

            # calculate the Cartesian velocities using only the first 3 rows of M, which correspond to u, v, w1
            cartesian_velocities = np.dot(transformation_matrix[:4, :], beam_velocities)

            # print(beam_velocities)
            # print('------------------')

            # append the scalar values to the temporary lists
            u_values.append(cartesian_velocities[0])
            v_values.append(cartesian_velocities[1])
            w1_values.append(cartesian_velocities[2])
            w2_values.append(cartesian_velocities[3])

        # Compute the average for u, v, w for this row
        u.append(np.mean([u_values[i] for i in relevant_point_ids]))
        v.append(np.mean([v_values[i] for i in relevant_point_ids]))
        w1.append(np.mean([w1_values[i] for i in relevant_point_ids]))
        w2.append(np.mean([w2_values[i] for i in relevant_point_ids]))


    # add Cartesian velocities to the DataFrame
    df['u (m/s)'] = u
    df['v (m/s)'] = v
    df['w1 (m/s)'] = w1
    df['w2 (m/s)'] = w2

    return df
