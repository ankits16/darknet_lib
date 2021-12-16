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
     build_ext_command = self.distribution.get_command_obj("build_ext")
     build_ext_command.debug = 1
     protoc_command = ["make"]
     # protoc_command = ["echo **************** ankit"]
     os.system('echo **************** ankit pwd before')
     os.system('pwd')
     os.system('echo **************** ankit pwd before')
     os.system('echo **************** ankit pwd after')
     os.chdir('./src/darknet')
     os.system('pwd')
     os.system('echo **************** ankit pwd after')
     os.system('echo **************** ankit test')
     if subprocess.call(protoc_command) != 0:
         sys.exit(-1)
     os.chdir('../..')
     os.system('echo **************** ankit pwd after make')
     os.system('pwd')
     os.system('echo **************** ankit pwd after make')
     print("mini pwd after ")
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