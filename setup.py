from setuptools import setup, find_packages

setup(name='nav',
  version='1.0',
  author="Antti Eskelinen",
  scripts=['bin/nav.ps1','bin/nav.cmd','bin/nav.sh'],
  packages=['nav_cli', 'nav_cli/data', 'nav_cli/user_interface'],
  entry_points={
        "console_scripts": [
            "nav_cli = nav_cli.__main__:main",
        ]
    }
  )