pygments-json
=============

Pygments_ is a syntax highlighting tool that supports a wide range of
languages and data formats.  However, pygments does not provide a JSON highlighter.  JSON can,
of course, be parsed by the Javascript lexer, but the resulting output looks very plain and
really provides almost no value over non-highlighted text.

pygments-json_ attempts to provide more interesting syntax highlighting which correctly distinguishes
between attribute names and values.  I'm new to pygments and to python packaging, so please don't hesitate
to tell me if I've done something wrong or if the JSON parsing doesn't quite work for you.


Install
--------

Until I learn a bit more about python packaging, I'm not going to create a PyPI_ project for
this.  And perhaps by the time I do figure out how to do that, the JSON lexer will be included
in pygments.  In the meantime, installation is straightforward.  I use pip_, which will allow
you to install pygments-json directly from github:

  $ pip install -e git+https://github.com/orb/pygments-json.git#egg=pygments-json

Usage
-------

Pygment json highlighting is available without any further customization from code as well
as from the pygementize command:

   $ pygmentize your-file.json
   ... beatifully formatted json will flow here
   ... or at least, it will be better than it was before


Norman Richards
   orb@nostacktrace.com

.. _Pygments: http://pygments.org/
.. _pygments-json: https://github.com/orb/pygments-json
.. _PyPI: http://pypi.python.org/pypi
.. _pip: http://www.pip-installer.org/
