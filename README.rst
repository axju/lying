===========================
lying - run a fake terminal
===========================

.. image:: https://img.shields.io/pypi/v/lying
   :alt: PyPI
   :target: https://pypi.org/project/lying/

.. image:: https://img.shields.io/pypi/pyversions/lying
   :alt: Python Version
   :target: https://pypi.org/project/lying/

.. image:: https://img.shields.io/pypi/l/lying
   :alt: License
   :target: https://pypi.org/project/lying/

.. image:: https://img.shields.io/jenkins/build/https/jenkins.axju.de/job/axju/job/lying/job/master
   :alt: Jenkins
   :target: https://jenkins.axju.de/job/axju/job/lying/

.. image:: https://img.shields.io/jenkins/coverage/cobertura/https/jenkins.axju.de/job/axju/job/lying/job/master
   :alt: Jenkins Coverage
   :target: https://jenkins.axju.de/job/axju/job/lying/

.. image:: https://github.com/axju/lying/blob/develop/ext/video.gif
   :alt: alternate text
   :align: right

This small project create a fake terminal, run fake commands and display fake
results. So, yes it's lying.


Install
-------
From source::

  pip install git+https://github.com/axju/lying.git

From Pypi::

  pip install lying

Do not forget to use a virtual environment.


How to use
----------
Relay simple, just create the instruction file and then run::

  lying run examples/instruction.json

To create the instruction file, take a look at the example folder. There is
also a setup function to interactively create the file::

  lying setup filename.json

If you want to record the result, you can use ffmpeg. The following commands
can help you::

  ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0+0,0 ext/video.mp4 -y

Create a gif::

  ffmpeg -i ext/video.mp4 -filter_complex "[0:v] palettegen" palette.png -y
  ffmpeg -i ext/video.mp4 -i palette.png -filter_complex "[0:v][1:v] paletteuse" ext/video.gif

Development
-----------
Some information for crazy developers. Virtual environment windows::

  python -m venv venv
  venv\Scripts\activate

Virtual environment linux::

  python3 -m venv venv
  source venv/bin/activate

Setup project::

  python -m pip install --upgrade pip wheel setuptools twine tox flake8 pylint coverage pytest rstcheck
  python -m pip install -e .

Run some test::

  tox
  python -m coverage run --source lying -m pytest
  python -m coverage report -m

Create package::

  python setup.py sdist bdist_wheel

Publish package::

  rstcheck README.rst
  python setup.py --version
  python setup.py check
  python setup.py sdist bdist_wheel
  twine upload dist/*
  git push origin 0.1.1
