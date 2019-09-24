===========================
lying - run a fake terminal
===========================
I need this for a other project. So it is still in develop.


Install
-------
::

  pip install lying


Development
-----------
Some information for crazy developers. Virtual environment windows::

  python -m venv venv
  venv\Scripts\activate

Virtual environment linux::

  python3 -m venv venv
  source venv/bin/activate

Setup project::

  python -m pip install --upgrade pip wheel setuptools twine tox flake8 pylint coverage
  python setup.py develop

Run some test::

  tox
  coverage run --source lying setup.py test
  coverage report -m

Create package::

  python setup.py sdist bdist_wheel

Upload package::

  twine upload dist/*
