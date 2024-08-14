"""
This is a code example for a dataset that is not contained within the sample-data folder, containing 11 .ntk.dat and
.ntk.hdr file sets.

The code implements the following workflow:
    * Check for coherent file patterns in the defined data_directory
    * For each pair of .ntk.dat and .ntk.hdr files:
        1. Retrieve the data contents from .ntk.dat
        2. Get the transformation matrix from .ntk.hdr
        3. Transform the beam velocities to Cartesian coordinate-based velocities
        4. Store the resulting pandas.DataFrame in the data_directory as .CSV file with the same name as the ASCII files
"""
import os
from get_ascii_data import read_ascii_file
from transformation import get_transformation_matrix, apply_transformation


# START USER INPUT -----------------------------------------------------------------------------------------------------
# define file the (relative) path to the folder containing pairs of .ntk.dat and .ntk.hdr files
data_directory = 'data/lhm/'
# END USER INPUT (modify the below code only if you know what you are doing) -------------------------------------------

# get all unique files in the directory
unique_names = []
for filename in os.listdir(data_directory):
    if filename.endswith(".ntk.dat") or filename.endswith(".ntk.hdr"):
        unique_names.append(filename.split('.ntk')[0])

# save the current working directory and temporarily switch to the data directory
original_directory = os.getcwd()
os.chdir(data_directory)

for ascii_file in unique_names:
    print('* processing ' + str(ascii_file) + ' ...')
    # get ascii data
    vectrino_data = read_ascii_file(ascii_file)
    # get transformation matrix
    M = get_transformation_matrix(ascii_file, scaling_factor=4096)
    # apply transformation and append Cartesian velocities u, v, and w
    vectrino_data = apply_transformation(vectrino_data, transformation_matrix=M)
    # write to CSV file
    vectrino_data.to_csv(ascii_file + '.csv', index=False)

# go back to the original working directory
os.chdir(original_directory)
