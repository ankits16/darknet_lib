from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages
import os
class Build(build_ext):
 """Customized setuptools build command - builds protos on build."""
 def run(self):
     protoc_command = ["make"]
     protoc_command = ["echo **************** ankit"]
     os.chdir('./src/ai_darknet_reshaped')
     os.system('echo **************** ankit')
     # if subprocess.call(protoc_command) != 0:
     #     sys.exit(-1)
     os.chdir('.')

     build_ext.run(self)


setup(
 name='ar_darknet_lib',
 version='1.0',
 description='Darknet lib for inference',
 packages=find_packages(where='src'),
 # packages=['src/commons'],
 # package_dir={'': 'src'},
 # packages=find_packages(where='src'),
 # packages= find_packages(where='darknet_src/ai_darknet_reshaped'),
                    # find_packages ['ai_darknet_reshaped'],
 # has_ext_modules=lambda: True,
 # cmdclass={
 #     'build_ext': Build,
 # },
 # include_package_data=True,
 # # packages=['src', 'src/ai_darknet_reshaped'],
 # package_data={
 #        # If any package contains *.txt or *.rst files, include them:
 #        "": ["darknet", "*.rst"],
 #        # And include any *.msg files found in the "hello" package, too:
 #        "ai_darknet_reshaped": ["darknet"],
 #    },
)