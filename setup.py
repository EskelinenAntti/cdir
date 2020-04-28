from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
  name='cdir',
  version='1.3',
  author="Antti Eskelinen",
  author_email='antti.eskelinen3@gmail.com',
  description='A faster way to navigate folders and browse files in Windows and Linux shells.',
  long_description = long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/EskelinenAntti/cdir",
  scripts=['bin/cdir.ps1','bin/cdir.cmd','bin/cdir.sh'],
  packages=['cdir_cli', 'cdir_cli/data', 'cdir_cli/user_interface'],
  entry_points={
        "console_scripts": [
            "cdir_cli = cdir_cli.__main__:main",
        ]
    },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  install_requires=[
   "windows_curses >= 2.1.0;platform_system=='Windows'"
  ]
  )