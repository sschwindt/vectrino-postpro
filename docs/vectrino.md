## Vectrino background

The Vectrino II is an acoustic Doppler velocimeter (ADV) for measuring three-dimensional water velocity profiles. It uses multiple acoustic beams to measure the Doppler shift, from which it calculates velocity components. The Vectrino II typically has four beams, oriented in different directions. Each beam measures flow velocity along the line of sight of each beam, referred to as the beam velocities. In this context, **Beam 1 to Beam 4** are the raw velocities measured along the direction of each beam, which are not aligned with the standard Cartesian coordinate system `(x, y, z)` and require conversion.

### Conversion to Cartesian coordinates

To obtain the actual velocity field in the standard Cartesian coordinate system `(u, v, w)`, we need to convert the beam velocities `(B1, B2, B3, B4)` into Cartesian velocities using a transformation matrix. The transformation matrix depends on the orientation of the beams, which is typically provided in the instrument documentation and header files.

The general form of the transformation from beam coordinates to Cartesian coordinates is:


\begin{align}
\begin{pmatrix}
u \\
v \\
w \\
q
\end{pmatrix}
&=
\mathbf{M}
\begin{pmatrix}
B1 \\
B2 \\
B3 \\
B4
\end{pmatrix}
\end{align}


where **u, v, w** are the Cartesian velocity components (in the x, y, z directions); **q** is an error (quality) metric; and **M** is the transformation matrix.

In the Vectrino II header files (e.g., `Vectrino-Profiler.00010.ntk.dat`), this information is accessible in the `Probe_hBeamToXYZ` variable. In addition, the descriptions of this variable (e.g., `Probe_hBeamToXYZ Beam to XYZ transformation matrix (scaled by 4096)`) provide the `scale_factor`, which is necessary to derive the transformation matrix from `Probe_hBeamToXYZ`. In this package, the transformation matrix is calculated based on this information as follows, assuming an exemplary value for `hBeamToXYZ`. Note that this value is automatically inferred from the `.ntk.hdr` file in the `get_transformation.get_transformation_matrix(<header_file_name>)` function.

```python

hBeamToXYZ = [8168, 70, -8153, -75, -73, 8126, 72, -8126, 2085, 0, 2146, 0, 9, 2116, -9, 2116]
scaling_factor = 4096

# convert array into a 4x4 matrix by dividing each element by the scaling factor
M = np.array(hBeamToXYZ).reshape(4, 4) / scaling_factor

print("Transformation Matrix M:")
print(M)
```

The following matrix multiplication is used to apply the transformation matrix `M` to convert the beam velocities into Cartesian velocities. Note that in this example, the beam velocities are stored in a pandas DataFrame called `df`:


```python
# exemplary transformation matrix M
M = np.array([
    [-0.5, -0.5, 0.5, 0.5],
    [0.5, -0.5, -0.5, 0.5],
    [0.7071, 0.7071, 0.7071, 0.7071],
    [0.0, 0.0, 0.0, 0.0]
])

# initiate lists to store each row of beam velocities in Cartesian velocities
u = []
v = []
w = []

for i in range(len(df)):
    # get beam velocities
    beam_velocities = np.array([
        df.loc[i, 'Velocity Beam 1 (m/s)'],
        df.loc[i, 'Velocity Beam 2 (m/s)'],
        df.loc[i, 'Velocity Beam 3 (m/s)'],
        df.loc[i, 'Velocity Beam 4 (m/s)']
    ])
    
    # convert to cartesian velocities
    cartesian_velocities = np.dot(M, beam_velocities)
    u.append(cartesian_velocities[0])
    v.append(cartesian_velocities[1])
    w.append(cartesian_velocities[2])

```

More information can be found in the [Vectrino II manual](https://www.nortekgroup.com/assets/software/N3015-030-Comprehensive-Manual-Velocimeters_1118.pdf).

### Quality considerations

Ensure your instrument is **correctly calibrated**, as incorrect calibration affects the transformation matrix and, thus, leads to wrong Cartesian velocities.

Check the quality of the velocity data, as noise or errors in the beam data can propagate through the transformation. For instance, the Signal-to-Noise Ratio (SNR) should be generally larger than 20.






