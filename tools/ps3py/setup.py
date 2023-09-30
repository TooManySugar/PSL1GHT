import sys
if sys.version_info >= (3, 10):
	from setuptools import setup, Extension
else:
	from distutils.core import setup, Extension

module1 = Extension('pkgcrypt', sources = ['crypt.c'])

setup (name = 'pkgcrypt',
       version = '1.0',
       description = 'C implementation of the crypt function from pkg.py',
       ext_modules = [module1])
