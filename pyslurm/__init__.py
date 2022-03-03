"""
PySlurm: Python bindings for the Slurm C API
============================================

PySlurm is a Cython wrapper around Slurm C API functions.

More information about Slurm can be found at https://slurm.schedmd.com.
"""
from __future__ import absolute_import

import ctypes
import sys

# From dlfcn.h
RTLD_DEEPBIND = 8

sys.setdlopenflags(sys.getdlopenflags() | ctypes.RTLD_GLOBAL | RTLD_DEEPBIND)

from .pyslurm import *
from .__version__ import __version__


def version():
    return __version__
