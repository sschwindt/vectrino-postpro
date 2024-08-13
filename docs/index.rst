.. documentation parent file.


Vectrino II ASCII Post-Processing
=================================

The codes in this repository are for post-processing measurements with a Vectrino II ADV. It takes ``.ntk.dat`` and ``.ntk.hdr`` ASCII files exported from a Nortek Vectrino II device (see the `developer's manual <https://www.nortekgroup.com/assets/software/N3015-030-Comprehensive-Manual-Velocimeters_1118.pdf>`_), reads the beam velocities, and applies a transformation matrix to convert the beam velocities from the four proms to Cartesian u, v, and w velocities (in m/s). It also extracts the SNR for the four beams, and writes all outputs to a CSV file. In principle, any raw parameters in the ``.ntk`` files could be added to this export, but I only did what was relevant for my analysis at this time. But I want to emphasize that any contribution is very welcome!


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

A further post-processing option is the extraction of turbulent kinetic energy, for example with my codes at `https://tke-calculator.readthedocs.io <https://tke-calculator.readthedocs.io/>`_. However, this might need some tweaking from vna/vno files to csv files.

.. important::

    Follow the installation instructions on `hydro-informatics.com <https://hydro-informatics.com/python-basics/pyinstall.html>`_ to make sure that GDAL works on your computer as desired (there are version issues because of numpy2, which requires GDAL>=3.9.1, which cannot be easily installed on Ubuntu derivates currently.

Currently, *flusstools* comes with the following modules:

* *bedanalyst* - for plotting and numeric analysis of riverbed characteristic to identify, for instance, clogging (developers: `Beatriz Negreiros`_, and `Ricardo Barros`_).
* *geotools* - versatile functions for processing spatial data for fluvial ecosystem analyses based on `gdal`_ and other open source libraries (developers: `Kilian Mouris`_, `Beatriz Negreiros`_, and `Sebastian Schwindt`_). The functions are explained with the geospatial Python `tutorials on hydro-informatics.com <https://hydro-informatics.com/jupyter/geo-shp.html>`_ and the `HydroMorphodynamics YouTube channel <https://www.youtube.com/@hydroinformatics>`_.
* *fuzzycorr* - a map comparison toolkit that builds on fuzzy sets to assess the accuracy of (numerical) river models (principal developer: `Beatriz Negreiros`_).
* *lidartools* - *Python* wrappers for `lastools`_ (forked and modified from `Kenny Larrieu`_).

.. admonition:: How to cite FlussTools

    If our codes helped you to accomplish your work, we won't ask you for a coffee, but to cite and spread the utility of our code - Thank you!

    .. code::

        @software{flussteam_tools_2024,
                  author       = {Sebastian Schwindt and
                                  Beatriz Negreiros and
                                  Ricardo Barros and
                                  Niklas Henning and
                                  Kilian Mouris},
                  title        = {FlussTools},
                  year         = 2024,
                  publisher    = {GitHub \& Center for Open Science (OSF)},
                  version      = {v1.1.8},
                  doi          = {10.17605/OSF.IO/G7K52},
                  url          = {https://doi.org/10.17605/OSF.IO/G7K52}
                }


The documentation is also as available as `style-adapted PDF <https://flusstools.readthedocs.io/_/downloads/en/latest/pdf/>`_.


.. toctree::
    :hidden:

    About <self>

.. toctree::
    :hidden:

    Installation <getstarted>

.. toctree::
    :hidden:

    Riverbed Analyst (BedAnalyst) <bedanalyst>

.. toctree::
    :hidden:

    Geospatial Analyst (GeoTools) <geotools>

.. toctree::
    :hidden:

    Map Correlation (FuzzyCorr) <fuzzycorr>

.. toctree::
    :hidden:

    Lidar Tools (LasPy/LasTools) <lidartools>

.. toctree::
    :hidden:

    Contributing <contribute>

.. toctree::
    :hidden:

    Disclaimer and License <license>

More information and examples are available in the docs of every *flusstools* module.

.. _Institute for Modelling Hydraulic and Environmental Systems: https://www.iws.uni-stuttgart.de/en/lww/
.. _Beatriz Negreiros: https://beatriznegreiros.github.io/
.. _gdal: https://gdal.org/
.. _Kilian Mouris: https://www.iws.uni-stuttgart.de/en/institute/team/Mouris/
.. _Kenny Larrieu: https://klarrieu.github.io/
.. _lastools: https://rapidlasso.com/lastools/
.. _QGIS: https://qgis.org/en/site/
.. _Ricardo Barros: https://ricardovobarros.github.io/
.. _Sebastian Schwindt: https://sebastian-schwindt.org/
