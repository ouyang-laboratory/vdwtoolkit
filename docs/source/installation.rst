.. _installation:

Installation
============

This section describes how to install **vdW-Toolkit**, including system requirements and troubleshooting tips.

System Requirements
-------------------

- **Python** 3.8 or later  
- A virtual environment is recommended (e.g., `venv`, `conda`)

Dependencies
------------

- **Typer**: command-line interface  
- **ASE**: atomic structure handling  
- **NumPy**: numerical operations  

Installation Steps
------------------

1. **Install from PyPI**:

   .. code-block:: bash

      pip install "typer[all]" ase numpy
      pip install vdwtoolkit

2. **Install in editable mode from source**:

   .. code-block:: bash

      git clone https://github.com/yourusername/vdwtoolkit.git
      cd vdwtoolkit
      pip install -e .

Optional Components
-------------------

- **VASP Interface**  
  Ensure VASP executables are installed and that the `VASP_CMD` environment variable is set, for example:

  .. code-block:: bash

     export VASP_CMD="mpirun -np 16 vasp_std"

- **LAMMPS Interface**  
  Install LAMMPS and add the `lmp` executable to your `PATH`.

- **GPUMD Interface**  
  Install GPUMD and add its executable to your `PATH`.

Troubleshooting
---------------

- **Dependency conflicts**  
  Upgrade dependencies:

  .. code-block:: bash

     pip install --upgrade "typer[all]" ase numpy

- **Command not found**  
  Activate your virtual environment or add the toolkit’s scripts directory to your `PATH`.

- **Permission denied**  
  Use the `--user` flag or work inside a virtual environment; avoid global `sudo` installs.

- **Build errors**  
  Install system build tools (e.g., `build-essential`, `gcc`, `python3-dev`).

If issues persist, please consult the GitHub repository’s [issue tracker](https://github.com/yourusername/vdwtoolkit/issues) or contact the maintainers.  
