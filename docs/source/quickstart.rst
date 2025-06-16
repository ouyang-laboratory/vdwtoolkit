# Quick Start

This section provides minimal examples to get started with **vdW-Toolkit** using both the command-line interface (CLI) and the Python API.

## Command-Line Interface

After installation, the CLI tool `vdwtoolkit` is available. Common commands include:

1. **Search Commensurate Supercells**

   ```bash
   vdwtoolkit commensurate \
     --a 3.16:3.16,2.50:2.50 \
     --max-n 12 \
     --tol-strain 1e-3
   ```

   This command finds supercells matching lattice parameters `3.16:3.16` (layer 1) and `2.50:2.50` (layer 2), within a maximum cell size of 12 and a strain tolerance of 0.1%.

2. **Build Twisted Heterostructure**

   ```bash
   vdwtoolkit build \
     --component gr,hbn \
     --cell 24:24,24:24 \
     --angle 10 \
     --output twist.xyz
   ```

   This creates a graphene/h-BN heterostructure with 10° twist and cell dimensions 24×24 for each layer, writing the result to `twist.xyz`.

3. **Post-Process Trajectory**

   ```bash
   vdwtoolkit post-process \
     --input traj.lammpstrj \
     --species C B N \
     --output analysis.json
   ```

   Processes `traj.lammpstrj` using species C, B, N and outputs structural metrics and registry data to `analysis.json`.

## Python API

For more complex workflows, import the package in Python:

```python
from vdwtoolkit.builder import CommensurateFinder
from vdwtoolkit.simulator.lammps import LAMMPS
from vdwtoolkit.analysis import run_post_processing

# 1. Find commensurate supercells
finder = CommensurateFinder(
    lattice1=(3.16, 3.16), lattice2=(2.50, 2.50), max_n=12, tol_strain=1e-3
)
supercells = finder.find()
print(f"Found {len(supercells)} candidates")

# 2. Build a twisted model for the first candidate
model = finder.build_model(supercells[0], angle=10)
model.write_xyz('twist.xyz')

# 3. Run LAMMPS simulation
lmp = LAMMPS()
lmp.prepare_input(model, temperature=300)
lmp.run()
results = lmp.parse_output()

# 4. Post-process
analysis = run_post_processing(
    'trajectory.lammpstrj', species=['C','B','N']
)
print(analysis)
```

These examples illustrate the core workflow: **model generation**, **simulation execution**, and **data analysis**. Refer to the **API Reference** for detailed class and function documentation.
