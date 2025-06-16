Tutorials
=========

This section provides in-depth tutorials covering model construction, simulation scheduling, and post-processing analysis with **vdW-Toolkit**.

Model Construction
------------------

Build commensurate and twisted heterostructures step by step:

1. **Find Commensurate Supercell**

   .. code-block:: python

      from vdwtoolkit.builder import CommensurateFinder

      # Initialize with lattice constants for layer A and B
      finder = CommensurateFinder(
          lattice1=(3.16, 3.16),
          lattice2=(2.50, 2.50),
          max_n=12,
          tol_strain=1e-3
      )
      candidates = finder.find()
      print(f"Found {len(candidates)} supercell candidates.")

2. **Select a Candidate and Build**

   .. code-block:: python

      # Choose first candidate and generate twist at 10°
      cell_params, strain = candidates[0]
      model = finder.build_model(cell_params, angle=10)
      model.write_xyz('twisted_model.xyz')

3. **Visualize**

   Load ``twisted_model.xyz`` into visualization tools (e.g., OVITO, VESTA).

Simulation Scheduling
---------------------

Run classical MD or DFT simulations directly via the CLI:

**LAMMPS**

.. code-block:: bash

   vdwtoolkit run \
       --engine lammps \
       --structure twisted_model.xyz \
       --in-template lammps_template.in \
       --out-dir lammps_run

**GPUMD**

.. code-block:: bash

   vdwtoolkit run \
       --engine gpumd \
       --structure twisted_model.xyz \
       --parameters gpumd_params.json \
       --out-dir gpumd_run

**VASP**

.. code-block:: bash

   export VASP_CMD="mpirun -np 16 vasp_std"
   vdwtoolkit run \
       --engine vasp \
       --structure POSCAR \
       --in-template INCAR \
       --kpoints KPOINTS \
       --out-dir vasp_run

Post-Processing Analysis
------------------------

Extract structural and thermal metrics from trajectory files:

.. code-block:: python

   from vdwtoolkit.analysis import run_post_processing

   results = run_post_processing(
       'lammps_run/traj.lammpstrj',
       species=['C', 'B', 'N'],
       compute_registry=True,
       compute_spectral=True
   )

Results include:

- **Bond Length Distribution**  
- **Bond Angle Distribution**  
- **Out-of-Plane Deformation Field**  
- **Registry Index Map**  
- **Spectral Heat Flux**

You can save results to JSON or visualize with external plotting tools.```
