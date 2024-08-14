..  documentation

Codes
=====


Transformation
~~~~~~~~~~~~~~

.. automodule:: transformation
    :members:
    :undoc-members:
    :show-inheritance:


Get ASCII data
~~~~~~~~~~~~~~

.. automodule:: get_ascii_data
    :members:
    :undoc-members:
    :show-inheritance:


Prostprocessing Head (Example)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: vectrino_ascii_postpro
    :members:
    :undoc-members:
    :show-inheritance:


This is a code template for loading and analyzing multiple files stored in a directory within the code repository.

To run this, make sure that the folder contains .ntk.dat and .ntk.hdr files, defining a complete Vectrino ASCII output
dataset.

The code implements the following workflow:
* Check for coherent file patterns in the defined data_directory
* For each pair of .ntk.dat and .ntk.hdr files:
	1. Retrieve the data contents from .ntk.dat
	2. Get the transformation matrix from .ntk.hdr
	3. Transform the beam velocities to Cartesian coordinate-based velocities
	4. Store the resulting pandas.DataFrame in the data_directory as .CSV file with the same name as the ASCII files
