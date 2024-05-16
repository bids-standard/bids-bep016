# Spherical Harmonics

Spherical Harmonics (SH) are continuous functions defined on the surface of the sphere.
They may be used to encode directionally dependent information;
for instance, the distribution of white matter fibre orientations within an image voxel.
This page provides the requisite information on the different basis sets that may be used,
and how coefficients of such functions may be encoded within a data file.

## SH functions

![SH functions](https://latex.codecogs.com/gif.latex?Y_l^m(\theta,\phi)&space;=&space;\sqrt{\frac{(2l&plus;1)}{4\pi}\frac{(l-m)!}{(l&plus;m)!}}&space;P_l^m(\cos&space;\theta)&space;e^{im\phi}")

for integer *order* *l*, *phase* *m*, associated Legendre polynomials *P*.

## Truncated basis coefficients

![SH basis coefficients](https://latex.codecogs.com/gif.latex?f(\theta,\phi)&space;=&space;\sum_{l=0}^{l_\text{max}}&space;\sum_{m=-l}^{l}&space;c_l^m&space;Y_l^m(\theta,\phi)")

for *maximum* spherical harmonic order *l<sub>max</sub>*.

## Real-valuedness

All functions represented using a spherical harmonics basis are assumed to be real.
This implies conjugate symmetry;
that is: *Y*(*l*,-*m*) = *Y*(*l*,*m*)\*,
where \* denotes the complex conjugate.

## Antipodal symmetry

All functions represented using a spherical harmonics based are assumed to be antipodally symmetric.
This implies that all basis functions with odd degree are zero.

## Bases

### `mrtrix3`

![MRtrix3 SH basis](https://latex.codecogs.com/gif.latex?Y_{lm}(\theta,\phi)=\begin{Bmatrix}&space;0&\text{if&space;}l\text{&space;is&space;odd},\\&space;\sqrt{2}\times\text{Im}\left[Y_l^{-m}(\theta,\phi)\right]&\text{if&space;}m<0,\\&space;Y_l^0(\theta,\phi)&\text{if&space;}m=0,\\&space;\sqrt{2}\times\text{Re}\left[Y_l^m(\theta,\phi)\right]&\text{if&space;}m>0\\&space;\end{Bmatrix})

### `descoteaux`

![Descoteaux SH basis functions](https://latex.codecogs.com/gif.latex?Y_{lm}(\theta,\phi)=\begin{Bmatrix}&space;0&\text{if&space;}l\text{&space;is&space;odd},\\&space;\sqrt{2}\times\text{Re}\left[Y_l^{-m}(\theta,\phi)\right]&\text{if&space;}m<0,\\&space;Y_l^0(\theta,\phi)&\text{if&space;}m=0,\\&space;\sqrt{2}\times\text{Im}\left[Y_l^m(\theta,\phi)\right]&\text{if&space;}m>0\\&space;\end{Bmatrix})

## Zonal Spherical Harmonics

*Zonal* Spherical Harmonics (ZSH) refer to spherical harmonic functions for which all coefficients
of non-zero order *m* are zero.
These functions are therefore invariant under rotation about some zenith axis.

![ZSH](https://latex.codecogs.com/gif.latex?Z_{l}(\theta,\phi)=Z_{l}(\theta)=Y_{l0})

## Serialization and deserialization

This is used to, for instance,
store coefficients in a spherical harmonic basis within volumes of a 4D NIfTI image.

### SH serialiszation and deserialization

For coefficient index *n* and spherical harmonic basis function coefficient *Y<sub>l,m</sub>*:

*n<sub>l,m</sub>* = (*l*(*l*+1) / 2) + *m*

| ***n*** | **Coefficient**    |
| ------- | ------------------ |
| 0       | *Y<sub>0,0</sub>*  |
| 1       | *Y<sub>2,-2</sub>* |
| 2       | *Y<sub>2,-1</sub>* |
| 3       | *Y<sub>2,0</sub>*  |
| 4       | *Y<sub>2,1</sub>*  |
| 5       | *Y<sub>2,2</sub>*  |
| 6       | *Y<sub>4,-4</sub>* |
| 7       | *Y<sub>4,-3</sub>* |
| ...     | ...                |

Relationship between maximal spherical harmonic degree *l<sub>max</sub>*
and total number of coefficients *N*:

*N* = ((*l<sub>max</sub>*+1) x (*l<sub>max</sub>*+2)) / 2

| ***l<sub>max</sub>*** | 0 | 2 | 4  | 6  | 8  | 10 | ... |
| --------------------- |--:|--:|--: |--: |--: |--: | :--: |
| ***N***               | 1 | 6 | 15 | 28 | 45 | 66 | ... |

### ZSH serialization and deserialization

For coefficient index *n* and zonal spherical harmonic basis function coefficient *Z<sub>l</sub>*:

*n<sub>l</sub>* = *l* / 2

| ***n*** | **Coefficient**  |
| ------- | ---------------- |
| 0       | *Z<sub>0</sub>*  |
| 1       | *Z<sub>2</sub>*  |
| 2       | *Z<sub>4</sub>*  |
| 3       | *Z<sub>6</sub>*  |
| 4       | *Z<sub>8</sub>*  |
| 5       | *Z<sub>10</sub>* |
| ...     | ...              |

Relationship between maximal zonal spherical harmonic degree *l<sub>max</sub>*
and total number of coefficients *N*:

*N* = 1 + *l*/2

| ***l<sub>max</sub>*** | 0 | 2 | 4 | 6 | 8 | 10 | ... |
| --------------------- |--:|--:|--:|--:|--:|--: | :--: |
| ***N***               | 1 | 2 | 3 | 4 | 5 | 6  | ... |
