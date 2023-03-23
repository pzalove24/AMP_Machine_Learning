This is a machine learning project and reserach for AMP lab at Mahidol University

To install the virtual environment package using pipenv
install python 3.8.10 64 bit from python software foundation and at to PATH using Windows installer (64-bit)
https://www.python.org/downloads/release/python-3810/

1. pip install pipenv #dont forget to look in PATH on system#
2. open folder for working
3. pipenv shell
4. pipenv lock # if do not see Pipfile.lock #
5. pipenv install #package# --dev

To upgrade pipenv at anytime
1. pip install --user --upgrade pipenv

piplock and pipfile should not be changed unless you install new package not from install dev-dependency

The main commands are install, uninstall, and lock, which generates a Pipfile.lock. These are intended to replace $ pip install usage, as well as manual virtualenv management 

(to activate a virtualenv, run $ pipenv shell)