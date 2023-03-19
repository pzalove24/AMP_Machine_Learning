This is a machine learning project and reserach for AMP lab at Mahidol University

To install the virtual environment package using pipenv

1. pip install pipenv #dont forget to look in PATH on system#
2. open folder
3. pipenv shell
4. pipenv lock
5. pipenv install <package name>

To upgrade pipenv at anytime
1. pip install --user --upgrade pipenv

The main commands are install, uninstall, and lock, which generates a Pipfile.lock. These are intended to replace $ pip install usage, as well as manual virtualenv management 
(to activate a virtualenv, run $ pipenv shell)