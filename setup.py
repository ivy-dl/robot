# lint as: python3
# Copyright 2021 The Ivy Authors. All Rights Reserved.
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
# limitations under the License..
# ==============================================================================
from distutils.core import setup
import setuptools

setup(name='ivy-robot',
      version='1.1.4',
      author='Ivy Team',
      author_email='ivydl.team@gmail.com',
      description='Functions and classes for gradient-based robot motion planning, written in Ivy.',
      long_description="""# What is Ivy Robot?\n\nIvy robot provides functions and classes for gradient-based motion
      planning and trajectory optimization. Classes are provided both for mobile robots and robot manipulators.
      Ivy currently supports Jax, TensorFlow, PyTorch, MXNet and Numpy. Check out the [docs](https://ivy-dl.org/robot) for more info!""",
      long_description_content_type='text/markdown',
      url='https://ivy-dl.org/robot',
      project_urls={
            'Docs': 'https://ivy-dl.org/robot/',
            'Source': 'https://github.com/ivy-dl/robot',
      },
      packages=setuptools.find_packages(),
      install_requires=['ivy-core', 'ivy-mech'],
      classifiers=['License :: OSI Approved :: Apache Software License'],
      license='Apache 2.0'
      )
