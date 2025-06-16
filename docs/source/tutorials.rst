# Tutorials

This section provides in-depth tutorials covering model construction, simulation scheduling, and post-processing analysis with **vdW-Toolkit**.

## Model Construction

Build commensurate and twisted heterostructures step by step:

1. **Find Commensurate Supercell**

   .. code-block:: python

   from vdwtoolkit.builder import CommensurateFinder

   # Initialize with lattice constants for layer A and B

   finder = CommensurateFinder(
   lattice1=(3.16, 3.16),
   lattice2=(2.50, 2.50),
   max\_n=12,
   tol\_strain=1e-3
   )
   candidates = finder.find()
   print(f"Found {len(candidates)} supercell candidates.")

2. **Select a Candidate and Build**

   .. code-block:: python

   # Choose first candidate and generate twist at 10°

   cell\_params, strain = candidates\[0]
   model = finder.build\_model(cell\_params, angle=10)
   model.write\_xyz('twisted\_model.xyz')

3. **Visualize**

   Load `twisted_model.xyz` into visualization tools (e.g., OVITO, VESTA).

## Simulation Scheduling

Run classical MD or DFT simulations directly via CLI:

* **LAMMPS**

  .. code-block:: bash

  vdwtoolkit run&#x20;
  \--engine lammps&#x20;
  \--structure twisted\_model.xyz&#x20;
  \--in-template lammps\_template.in&#x20;
  \--out-dir lammps\_run

* **GPUMD**

  .. code-block:: bash

  vdwtoolkit run&#x20;
  \--engine gpumd&#x20;
  \--structure twisted\_model.xyz&#x20;
  \--parameters gpumd\_params.json&#x20;
  \--out-dir gpumd\_run

* **VASP**

  .. code-block:: bash

  export VASP\_CMD="mpirun -np 16 vasp\_std"
  vdwtoolkit run&#x20;
  \--engine vasp&#x20;
  \--structure POSCAR&#x20;
  \--in-template INCAR&#x20;
  \--kpoints KPOINTS&#x20;
  \--out-dir vasp\_run

## Post-Processing Analysis

Extract structural and thermal metrics from trajectory files:

.. code-block:: python

from vdwtoolkit.analysis import run\_post\_processing

results = run\_post\_processing(
'lammps\_run/traj.lammpstrj',
species=\['C', 'B', 'N'],
compute\_registry=True,
compute\_spectral=True
)

Results include:

* **Bond Length Distribution**
* **Bond Angle Distribution**
* **Out-of-Plane Deformation Field**
* **Registry Index Map**
* **Spectral Heat Flux**

You can save results to JSON or visualize with external plotting tools.
