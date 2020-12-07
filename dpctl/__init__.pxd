# ===------------ __init__.pxd - dpctl module --------*- Cython -*----------===#
#
#                      Data Parallel Control (dpCtl)
#
# Copyright 2020 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ===-----------------------------------------------------------------------===#
#
# \file
# This file declares the extension types and functions for the Cython API
# implemented in sycl_core.pyx.
#
# ===-----------------------------------------------------------------------===#

# distutils: language = c++
# cython: language_level=3

from dpctl._sycl_core cimport *
from dpctl._memory import *
from dpctl.dptensor.dparray import *

