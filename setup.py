from distutils.core import setup

setup(
  name = 'depedit',
  packages = ['depedit'],
  version = '2.1.2',
  description = 'A simple configurable tool for manipulating dependency trees',
  author = 'Amir Zeldes',
  author_email = 'amir.zeldes@georgetown.edu',
  url = 'https://github.com/amir-zeldes/depedit', 
  license='Apache License, Version 2.0',
  download_url = 'https://github.com/amir-zeldes/depedit/releases/tag/2.1.2',
  keywords = ['NLP', 'parsing', 'syntax', 'dependencies', 'dependency', 'tree', 'treebank', 'conll', 'conllu', 'ud'],
  classifiers = ['Programming Language :: Python',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 3',
'License :: OSI Approved :: Apache Software License',
'Operating System :: OS Independent'],
)