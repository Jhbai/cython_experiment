from setuptools import setup, Extension
from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "method",
        sources=["method.pyx"],
        include_dirs=[np.get_include()]
    )
]

setup(
    ext_modules=cythonize(extensions)
)
