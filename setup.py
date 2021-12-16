from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages
import os
import subprocess
import sys
from distutils.command.install import install as _install

class Build(build_ext):
 """Customized setuptools build command - builds protos on build."""
 def run(self):
     build_ext_command = self.distribution.get_command_obj("build_ext")
     build_ext_command.debug = 1
     protoc_command = ["make"]
     # protoc_command = ["echo **************** ankit"]

     print(f'************************ cwd  before make {os.getcwd()}')
     os.chdir('./src/darknet_alex')
     # build/lib/src/darknet
     print(f'************* is darknet folder there before make {os.path.isdir(" src/darknet_alex/")}')
     print(f'************* is darknet there before make {os.path.isfile("darknet")}')
     print(f'************************ cwd after chage directory before make {os.getcwd()}')
     if subprocess.call(protoc_command) != 0:
         sys.exit(-1)
     print(f'************************ cwd before chage directory after make {os.getcwd()}')
     print(f'************* is darknet there {os.path.isfile("darknet")}')
     for file in os.listdir(os.getcwd()):
         print(f'<<<<<<<<<<<<<<<<<<<<<<<< {file}')
     os.chdir('../..')
     print(f'************************ cwd after chage directory after make {os.getcwd()}')
     build_ext.run(self)


setup(
 name='ar_darknet_lib',
 version='1.0',
 description='Darknet lib for inference',

 has_ext_modules=lambda: True,
 cmdclass={
     'build_ext': Build,
 },
 package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["darknet_compiled", 'darknet_pre_compiled', "Makefile", "*.sh"],
        # And include any *.msg files found in the "hello" package, too:
 },
 packages=find_packages(),
)