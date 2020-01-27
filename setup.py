#!/usr/bin/python

from setuptools import setup

setup(name='pygments-algo-lexer',
      version='1.0.1',
      description='Pygments algo lexer for French language.',
      keywords='pygments algo lexer french',
      license='BSD',

      author='Alizée Penel',
      author_email='alizee@lse.epita.fr',

      url='https://github.com/kynzie/pygments-algo-fr',

      packages=['pygments_algo_lexer'],
      install_requires=['pygments>=2.0.2'],

      entry_points='''[pygments.lexers]
                      AlgoLexer=pygments_algo_lexer:AlgoLexer''',

      classifiers=[
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
