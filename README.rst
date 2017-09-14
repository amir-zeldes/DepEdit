=======
DepEdit
=======

A simple configurable tool for manipulating dependency trees.

DepEdit reads and writes files encoded in the CoNLLX or CoNLLU dependency format (10 columns). 
It's a simple Python script which can change token attributes, token text, part of speech
dependency function and other columns, as well as rewiring dependency graphs based on rules.
You can also use it to add annotations to each sentence based on properties of the subgraph 
(see the English example of tagging rough sentence type in examples/)

To use the script, either copy the file *depedit/depedit.py* into your project, or install it from PyPI:

.. code-block:: bash

  pip install depedit

For more information see https://corpling.uis.georgetown.edu/depedit/