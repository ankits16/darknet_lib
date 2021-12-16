from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages
import os
import subprocess
import sys


class Build(build_ext):
 """Customized setuptools build command - builds protos on build."""
 def run(self):
     protoc_command = ["make"]
     # protoc_command = ["echo **************** ankit"]
     os.chdir('./src/darknet')
     os.system('echo **************** ankit')
     if subprocess.call(protoc_command) != 0:
         sys.exit(-1)
     os.chdir('.')

     build_ext.run(self)


setup(
 name='ar_darknet_lib',
 version='1.0',
 description='Darknet lib for inference',
 packages=find_packages(),
 has_ext_modules=lambda: True,
 cmdclass={
     'build_ext': Build,
 },
)