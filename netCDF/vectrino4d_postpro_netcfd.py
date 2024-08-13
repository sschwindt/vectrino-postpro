import netCDF4 as nc
import numpy as np


def inspect_netCDF(nc_dataset):
    """ Inspect the structure of a netCDF4 file
    :param netCDF4.Dataset nc_dataset: download from Vectrino II device and load in Python with netCDF4 library
    :return:
    """
    print("File structure:")
    print(nc_dataset)
    # List all groups
    print("Groups:")
    for group_name in dataset.groups:
        print(f"  {group_name}")


def inspect_nc_groups(nc_dataset, group_name='Config'):
    """Print the device config to console

    :param netCDF4.Dataset nc_dataset: download from Vectrino II device and load in Python with netCDF4 library
    :param str group_name: provide the group name to be inspected; the default inspection group is 'Config'. Note that a
                            Vectrino II netCDF file holds two groups, namely 'Config' and 'Data'. The 'Data' group has
                            multiple subgroups.
    :return:
    """
    nc_group = nc_dataset.groups[group_name]
    # print the structure of the group
    print("\n" + str(group_name) + " Group Structure:")
    print(nc_group)
    # print global config attributes
    print("\nAttributes in " + str(group_name) + " Group:")
    for attr in nc_group.ncattrs():
        print(f"{attr}: {getattr(nc_group, attr)}")
    print("\nVariables in " + str(group_name) + " Group:")
    for var_name, var in nc_group.variables.items():
        print(f"{var_name}: {var.dimensions}")
        # Optionally, access the data from a specific variable
        if var_name == 'variable_name':  # replace 'variable_name' with your actual variable name
            data = var[:]
            print(f"Data in '{var_name}':", data)


def print_variable_stats(nc_variable):
    """ Write the statistical attributes of a variable in a netCFD dataset to the console.

    :param netCFD4.Dataset.variables['<NAME>'] nc_variable: The nc variable to examine.
    :return: None
    """

    print("\nVariable Info:")
    print(velocity_range_var)
    # data from the '<NAME>' variable
    range_data = velocity_range_var[:]
    print("\nRange Data (type:" + str(type(range_data)) + "):")
    print(range_data)

    print("\nRange Data Statistics:")
    print(f"Min: {range_data.min()}, Max: {range_data.max()}")
    print(f"Mean: {range_data.mean()}")
    print(f"Shape: {range_data.shape}")
    print(f"First 5 entries: {range_data.flatten()[:5]}")


# load NetCDF file
netcdf_file_path = 'data/HB.192.24.Vectrino Profiler.00001.nc'


with nc.Dataset(netcdf_file_path, 'r') as dataset:
    # Data inspection
    data_inspection = False
    data_group = dataset.groups['Data']
    data_profiles = data_group.groups['Profiles']
    if data_inspection:
        inspect_nc_groups(dataset, 'Data')
        inspect_nc_groups(data_group, 'Profiles')

    # extract relevant variables
    velocity_range_var = data_profiles.variables['Velocity Range']
    velocity_beam1 = data_profiles.variables['VelocityBeam1']
    print_variable_stats(velocity_beam1)








# inspect_nc_groups(data_group, 'Profiles')


    # Optionally, access the data from a specific variable
    # For example, if the variable name is 'temperature'
    # if var_name == 'temperature':  # replace 'temperature' with your variable name
    #     temperature_data = var[:]
    #     print("Temperature data:", temperature_data)

# Access a specific variable (example)
# Assuming the NetCDF file contains a variable named 'temperature'
# if 'temperature' in dataset.variables:
#     temperature = dataset.variables['temperature'][:]
#     print("\nTemperature Data Shape:", temperature.shape)
#     print("Temperature Data Example (first 5 entries):", temperature.flatten()[:5])
