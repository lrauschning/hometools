from setuptools import setup, find_packages

setup(name="hometools",
      version='0.1',
      description='Collections of command-line functions to perform common pre-processing and analysis functions',
      author='Manish Goel',
      author_email='goel@mpipz.mpg.de',
      license='MIT License',
      license_files=('LICENSE',),
      packages=['hometools'],
      # py_modules=["hometools.classes",
      #             "hometools.hometools"],
      scripts=['bin/hometools'],
      long_description=open('README').read(),
      )