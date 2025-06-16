.. _faq:

FAQ
===

This section addresses common issues and questions when using **vdW-Toolkit**.

Q1. **Why does the `commensurate` command return no candidates?**

- Ensure that the lattice constants are in the correct order and units (Å).
- Increase `--max-n` to search larger supercells.
- Loosen `--tol-strain` if small strain is unavoidable.

Q2. **How do I specify a custom LAMMPS input template?**

- Use the `--in-template` flag with the path to your LAMMPS input file.
- Place variables like ``{structure}`` and ``{parameters}`` in the template; they will be replaced automatically.

Q3. **I get “command not found” for `vdwtoolkit`.**

- Verify that the installation directory (e.g., ``~/.local/bin`` or your virtualenv’s ``bin/``) is in your ``PATH``.
- If installed in editable mode, ensure the environment is activated.

Q4. **The VASP simulation fails due to missing POTCAR.**

- Download the appropriate POTCAR files for your elements and place them in the working directory.
- Or set the ``VASP_POTPATH`` environment variable to point to your POTCAR repository.

Q5. **Memory errors during post-processing large trajectories.**

- Split trajectories into smaller chunks.
- Increase available memory or run on a node with more RAM.
- Use the ``chunk_size`` parameter in ``run_post_processing`` to limit frames loaded at once.

Q6. **How can I add support for a new file format?**

- Implement a new reader or writer in the ``vdwtoolkit.io`` module following existing patterns.
- Register the format in ``vdwtoolkit.io.file_format.py`` and update the CLI options accordingly.

For further questions, please open an issue on the GitHub repository.  
