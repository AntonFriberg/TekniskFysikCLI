TekniskFysikCLI
=========

*A tool to download material from tekniskfysik.org*


Purpose
-------

This is a simple CLI tool that downloads pdf material from `tekniskfysik.org <http://tekniskfysik.org/>`_.
It puts all the pdfs into course folders for easy organisation. 


Usage
-----

If you've cloned this project, and want to install the library, the command
you'll want to run is::

    $ pip install -e .

In order to download all the pdfs into the current directory you then simply run::

    $ TekniskFysikCLI entire

Developer Information
_____________________

If you want to install the development libraries aswell, the command you'll
want to run is::

    $ pip install -e '.[test]'

If you'd like to run all tests for this project, you would run the following
command::

    $ python setup.py test

This will trigger `py.test <http://pytest.org/latest/>`_, along with its popular
`coverage <https://pypi.python.org/pypi/pytest-cov>`_ plugin.

Lastly, if you'd like to cut a new release of this CLI tool, and publish it to
the Python Package Index (`PyPI <https://pypi.python.org/pypi>`_), you can do so
by running::

    $ python setup.py sdist bdist_wheel
    $ twine upload dist/*

This will build both a source tarball of your CLI tool, as well as a newer wheel
build (*and this will, by default, run on all platforms*).

The ``twine upload`` command (which requires you to install the `twine
<https://pypi.python.org/pypi/twine>`_ tool) will then securely upload your
new package to PyPI so everyone in the world can use it!

Credits
-------
Based on information provided at `stormpath.com <https://stormpath.com/blog/building-simple-cli-interfaces-in-python>`_
Utilizes python libraries "Docopt" and "BeautifulSoup" for CLI functionality.
Testing tools provided by python libraries "Coverage", "Pytest" and "Pytest-cov".
