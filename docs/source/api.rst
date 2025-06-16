# API Reference

This section provides detailed documentation of core classes and functions in **vdW-Toolkit**, including constructor signatures, parameters, methods, and return values.

## Builder Module

.. autoclass:: vdwtoolkit.builder.CommensurateFinder
\:members:
\:show-inheritance:

**Constructor**::

```
  CommensurateFinder(
    lattice1: Tuple[float, float],
    lattice2: Tuple[float, float],
    max_n: int = 10,
    tol_strain: float = 1e-3
  )
```

**Parameters**:

* `lattice1`: Lattice constants (a, b) for layer 1.
* `lattice2`: Lattice constants (a, b) for layer 2.
* `max_n`: Maximum multiplier for supercell size.
* `tol_strain`: Maximum allowed strain (fractional).

**Methods**:

* `find() -> List[Tuple[Tuple[int, int, int, int], float]]`

  * Returns a list of (cell parameters, strain) pairs.

* `build_model(cell_params: Tuple[int, int, int, int], angle: float, offset: Tuple[float, float] = (0, 0)) -> Structure`

  * Builds a twisted heterostructure with given cell parameters, twist angle, and lateral offset.

## Analysis Module

.. autosummary::
\:toctree: api/analysis

vdwtoolkit.analysis.bond\_angle
vdwtoolkit.analysis.bond\_length
vdwtoolkit.analysis.deformation
vdwtoolkit.analysis.neighbor
vdwtoolkit.analysis.registry\_index
vdwtoolkit.analysis.post\_process

## Simulator Module

.. autoclass:: vdwtoolkit.simulator.Simulator
\:members:
\:show-inheritance:

.. autoclass:: vdwtoolkit.simulator.lammps.LAMMPS
\:members:

.. autoclass:: vdwtoolkit.simulator.gpumd.GPUMDRunner
\:members:

.. autoclass:: vdwtoolkit.simulator.vasp.VaspRunner
\:members:

## I/O Module

.. autosummary::
\:toctree: api/io

vdwtoolkit.io.file\_format
vdwtoolkit.io.reader
vdwtoolkit.io.writer

## Utilities Module

.. autoclass:: vdwtoolkit.utils.constant
\:members:

.. autoclass:: vdwtoolkit.utils.frame.Frame
\:members:

.. autoclass:: vdwtoolkit.utils.materials
\:members:

.. autoclass:: vdwtoolkit.utils.timer.Timer
\:members:

## Note

API pages are auto-generated with Sphinx `autodoc`. Use `make html` in the `docs` directory to build full documentation.
