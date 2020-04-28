from setuptools import setup, find_packages

setup(name='nav',
  version='1.0',
  author="Antti Eskelinen",
  scripts=['nav/bin/nav.ps1','nav/bin/nav.bat','nav/bin/nav.sh'],
  packages=['nav', 'nav/data', 'nav/user_interface'],
  entry_points={
        "console_scripts": [
            "nav_cli = nav.__main__:main",
        ]
    }
  )