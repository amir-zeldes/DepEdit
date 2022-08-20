# DepEdit

A simple configurable tool for manipulating dependency trees.

DepEdit reads and writes files encoded in the CoNLL-U or CoNLL-X dependency format (10 columns).  It's a simple Python script which can change token attributes, token text, part of speech dependency function and other columns, as well as rewiring dependency graphs based on rules. You can also use it to add annotations to each sentence based on properties of the subgraph (see the English example of tagging rough sentence type in examples/)

To use the script, either copy the file `depedit/depedit.py` into your project, or install it from PyPI:

```
pip install depedit
```

You can then run it directly or as a module:

```
If depedit is in the current directory:

> python depedit.py -c CONFIG.ini INFILE.conllu

Or if installed via pip or setup.py, then in any directory:

> python -m depedit -c CONFIG.ini INFILE.conllu
```

## Basic usage

```
usage: depedit.py [-h] [-c CONFIG] [-d] [-s] [-k {supertoks,comments,both}]
                  [-q] [--stepwise] [-o OUTDIR] [-e EXTENSION] [-i INFIX]
                  [--version]
                  file

positional arguments:
  file                  Input single file name or glob pattern to process a
                        batch (e.g. *.conllu)

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Configuration file defining transformation
  -d, --docname         Begin output with # newdoc id =...
  -s, --sent_id         Add running sentence ID comments
  -t, --text            Add # text =...
  -k {supertoks,comments,both}, --kill {supertoks,comments,both}
                        Remove supertokens or commments from output
  -q, --quiet           Do not output warnings and messages
  --stepwise            Output sentence repeatedly after each step (useful for
                        debugging)
  --version             show program's version number and exit

Batch mode options:
  -o OUTDIR, --outdir OUTDIR
                        Output directory in batch mode
  -e EXTENSION, --extension EXTENSION
                        Extension for output files in batch mode
  -i INFIX, --infix INFIX
                        Infix to denote edited files in batch mode (default:
                        .depedit)
```

For more information see https://gucorpling.org/depedit/ and read the included User Guide PDF in doc/.

## Citing

If you are using DepEdit in a scholarly paper, please cite the following reference:

```
 @InProceedings{PengZeldes2020,
   author    = {Siyao Peng and Amir Zeldes},
   title     = {All Roads Lead to {UD}: Converting {S}tanford and {P}enn Parses to {E}nglish {U}niversal {D}ependencies with Multilayer Annotations},
   booktitle = {Proceedings of the Joint Workshop on Linguistic Annotation, Multiword Expressions and Constructions ({LAW}-{MWE}-{C}x{G}-2018)},
   year      = {2018},
   pages     = {167--177},
   address   = {Santa Fe, NM},
   url       = {https://www.aclweb.org/anthology/W18-4918}
 }
 ```