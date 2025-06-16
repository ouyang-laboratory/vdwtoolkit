Usage
=====

.. _usage:

Installation
------------

To install **vdW-Toolkit**, use **pip**:

.. code-block:: console

   (.venv) $ pip install vdwtoolkit

Quick Example
-------------

After installation, you can invoke the toolkit in Python:

.. code-block:: python

   >>> import vdwtoolkit
   >>> # e.g. fast_build() will automatically construct a common bilayer model
   >>> structure = vdwtoolkit.fast_build(
   ...     material_a="graphene",
   ...     material_b="MoS2",
   ...     twist_angle=5.0,
   ...     max_n=6
   ... )
   >>> print(structure)  # displays basic cell parameters

Or run from the command line:

.. code-block:: bash

   $ vdwtoolkit run \
       --engine lammps \
       --structure my_model.xyz \
       --in-template lammps_template.in \
       --out-dir lammps_output

API Shortcut
------------

The `vdwtoolkit.fast_build()` helper wraps common steps:

- **Search** for commensurate supercells  
- **Build** a twisted heterostructure  
- **Write** output files (`.xyz`, `POSCAR`)

Use this for rapid prototyping or scripting workflows.```
