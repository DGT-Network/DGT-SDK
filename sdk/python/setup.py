# Copyright 2019 NTRLab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

from __future__ import print_function

import os
import subprocess

from setuptools import setup, find_packages


if os.name == 'nt':
    conf_dir = "C:\\Program Files (x86)\\Intel\\dgt\\conf"
    data_dir = "C:\\Program Files (x86)\\Intel\\dgt\\data"
    log_dir = "C:\\Program Files (x86)\\Intel\\dgt\\logs"
else:
    conf_dir = "/etc/dgt"
    data_dir = "/var/lib/dgt"
    log_dir = "/var/log/dgt"

data_files = [
    (conf_dir, []),
    (os.path.join(conf_dir, "keys"), []),
    (data_dir, []),
    (log_dir, []),
]

setup(
    name='dgt-sdk',
    version=subprocess.check_output(
        ['../../bin/get_version']).decode('utf-8').strip(),
    description='Dgt Python SDK',
    author='Hyperledger Sawtooth-dgt',
    url='https://github.com/hyperledger/sawtooth-core',
    packages=find_packages(),
    data_files=data_files,
    install_requires=[
        "colorlog",
        "sawtooth-signing",
        "protobuf",
        "pyzmq",
        "toml",
        "PyYAML",
    ])
