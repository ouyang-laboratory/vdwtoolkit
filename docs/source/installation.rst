# Installation

This section describes how to install **vdW-Toolkit**, including system requirements and troubleshooting tips.

## System Requirements

* Python 3.8 or later
* A virtual environment is recommended (venv, conda, etc.)

## Dependencies

* **Typer**: for command-line interface
* **ASE**: for atomic structure handling
* **NumPy**: for numerical operations

## Installation Steps

1. **Install from PyPI:**

   .. code-block:: bash

   pip install typer\[all] ase numpy
   pip install vdwtoolkit

2. **Install in editable mode from source:**

   .. code-block:: bash

   git clone [https://github.com/yourusername/vdwtoolkit.git](https://github.com/yourusername/vdwtoolkit.git)
   cd vdwtoolkit
   pip install -e .

## Optional Components

* **VASP Interface:** Ensure VASP executables are installed and set the `VASP_CMD` environment variable.
* **LAMMPS Interface:** Install LAMMPS and add the `lmp` command to your `PATH`.
* **GPUMD Interface:** Install GPUMD and add its executable to your `PATH`.

## Troubleshooting

* **Dependency conflicts:** Upgrade dependencies:

  .. code-block:: bash

  pip install --upgrade typer ase numpy

* **Command not found:** Activate your virtual environment or add the executable paths to `PATH`.

* **Permission denied:** Use `--user` flag or a virtual environment; avoid global sudo installation.

* **Build errors:** Install system build tools (e.g., `build-essential`, `gcc`, `python3-dev`).

If issues persist, please consult the GitHub repository issues or contact the maintainers.
