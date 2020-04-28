pip uninstall dist\nav-1.0-py3-none-any.whl -y
py setup.py bdist_wheel
pip install dist\nav-1.0-py3-none-any.whl