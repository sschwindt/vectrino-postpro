.. documentation parent file.


Vectrino II ASCII Post-Processing
=================================

The codes in this repository are for post-processing measurements with a Vectrino II ADV. It takes ``.ntk.dat`` and ``.ntk.hdr`` ASCII files exported from a Nortek Vectrino II device (see the `developer's manual <https://www.nortekgroup.com/assets/software/N3015-030-Comprehensive-Manual-Velocimeters_1118.pdf>`_), reads the beam velocities, and applies a transformation matrix to convert the beam velocities from the four proms to Cartesian u, v, and w velocities (in m/s). It also extracts the SNR for the four beams, and writes all outputs to a CSV file. In principle, any raw parameters in the ``.ntk`` files could be added to this export, but I only did what was relevant for my analysis at this time. But I want to emphasize that any contribution is very welcome!

To work with the code, download or clone it from `https://github.com/sschwindt/vectrino-postpro <https://github.com/sschwindt/vectrino-postpro>`_:

.. code::

    git clone https://github.com/sschwindt/vectrino-postpro


Requirements
++++++++++++

The code was developped and tested with Python 3.10. To get detailed installation instructions for Python, visit `https://hydro-informatics.com/python-basics/pyinstall.html <https://hydro-informatics.com/python-basics/pyinstall.html>`_ or use your preferred search engine/AI. The following libraries are required:

.. code::

    numpy
    pandas


Run
+++ 

An example can be see by running ``vectrino_ascii_postpro.py``:

.. code::

    python vectrino_ascii_postpro.py

Another post-processing option is the extraction of turbulent kinetic energy, for example with my codes at `https://tke-calculator.readthedocs.io <https://tke-calculator.readthedocs.io/>`_. However, this will require some tweaking from vna/vno files to csv files.


Output
++++++

The code outputs a CSV file containing the time series data from the Vectrino Profiler measurements, transformed into stream coordinate velocities *u(x)*, *v(y)*, and *w(z)*, lists of the original velocities measured along four beams, and signal-to-noise ratio (SNR) values. The CSV dataset is structured as follows:


+-----------------------+----------------------------------------+
| **Column Name**       | **Description**                        |
+=======================+========================================+
| Time (s)              | Time of measurement in seconds.        |
+-----------------------+----------------------------------------+
| Velocity Beam 1 (m/s) | List of velocity measurements (m/s)    |
|                       | along Beam 1.                          |
+-----------------------+----------------------------------------+
| Velocity Beam 2 (m/s) | List of velocity measurements (m/s)    |
|                       | along Beam 2.                          |
+-----------------------+----------------------------------------+
| Velocity Beam 3 (m/s) | List of velocity measurements (m/s)    |
|                       | along Beam 3.                          |
+-----------------------+----------------------------------------+
| Velocity Beam 4 (m/s) | List of velocity measurements (m/s)    |
|                       | along Beam 4.                          |
+-----------------------+----------------------------------------+
| SNR Beam 1 (dB)       | Signal-to-Noise Ratio (dB) for Beam 1. |
+-----------------------+----------------------------------------+
| SNR Beam 2 (dB)       | Signal-to-Noise Ratio (dB) for Beam 2. |
+-----------------------+----------------------------------------+
| SNR Beam 3 (dB)       | Signal-to-Noise Ratio (dB) for Beam 3. |
+-----------------------+----------------------------------------+
| SNR Beam 4 (dB)       | Signal-to-Noise Ratio (dB) for Beam 4. |
+-----------------------+----------------------------------------+
| u (m/s)               | Flow velocity component in the x-axis. |
+-----------------------+----------------------------------------+
| v (m/s)               | Flow velocity component in the y-axis. |
+-----------------------+----------------------------------------+
| w (m/s)               | Flow velocity component in the z-axis. |
+-----------------------+----------------------------------------+

Each row represents a snapshot of the measured velocities from the four beams at a given time. The velocities for each beam are logged as arrays. The SNR values provide information about the reliability of the velocity measurements, with higher SNR values indicating better signal quality relative to the background noise. The SNR is typically measured in decibels (dB) and the signal quality can be considered as follows (caution, this is only a suggestion):

- **SNR > 40 dB** is considered excellent quality. In this range, the signal is strong compared to the noise and measurements are highly reliable.
- **30 dB < SNR ≤ 40 dB** is good quality. Although not as strong as an SNR above 40, the measurements are still reliable and accurate.
- **20 dB < SNR ≤ 30 dB** indicates moderate quality. While the signal is distinguishable from the noise, the measurements may begin to show variability and caution should be used in interpreting the data.
- **SNR ≤ 20 dB** should be considered poor quality. The signal is weak relative to the noise and the measurements are not reliable. Significant noise interference may affect the data and these values should be disregarded.

For Vectrino data, an SNR of at least **30 dB** is generally considered a good threshold for reliable measurements. Values below this threshold may require further investigation or may indicate the need to exclude that data from further analysis.


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
