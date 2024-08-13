.. documentation parent file.


Vectrino II ASCII Post-Processing
=================================

The codes in this repository are for post-processing measurements with a Vectrino II ADV. It takes ``.ntk.dat`` and ``.ntk.hdr`` ASCII files exported from a Nortek Vectrino II device (see the `developer's manual <https://www.nortekgroup.com/assets/software/N3015-030-Comprehensive-Manual-Velocimeters_1118.pdf>`_), reads the beam velocities, and applies a transformation matrix to convert the beam velocities from the four proms to Cartesian u, v, and w velocities (in m/s). It also extracts the SNR for the four beams, and writes all outputs to a CSV file. In principle, any raw parameters in the ``.ntk`` files could be added to this export, but I only did what was relevant for my analysis at this time. But I want to emphasize that any contribution is very welcome!

To work with the code, download or clone it from `https://github.com/sschwindt/vectrino-postpro <https://github.com/sschwindt/vectrino-postpro>`_:

.. code::

    git clone https://github.com/sschwindt/vectrino-postpro


Requirements
++++++++++++

The code was developped and tested with Python 3.10. To get detailed installation instructions for Python, visit `https://hydro-informatics.com/python-basics/pyinstall.html <https://hydro-informatics.com/python-basics/pyinstall.html>`_ or use your preferred search engine/AI.

.. code::

    numpy
    pandas


Run
+++ 

An example can be see by running ``vectrino_ascii_postpro.py``:

.. code::

    python vectrino_ascii_postpro.py

Another post-processing option is the extraction of turbulent kinetic energy, for example with my codes at `https://tke-calculator.readthedocs.io <https://tke-calculator.readthedocs.io/>`_. However, this will require some tweaking from vna/vno files to csv files.



.. toctree::
    :hidden:

    About <self>

.. toctree::
    :hidden:

    Background <vectrino>
    
.. toctree::
    :hidden:

    Code docs <codes>

.. toctree::
    :hidden:

    License <license>
