Python Orbit
============

🪐 Light Orbit API wrapper written in Python

|Latest Version| |codecov| |Build Status| |License: MIT|

⚠️ This project is WIP

Install
-------

.. code:: sh

   pip install python-orbit

Usage
-----

If you need some code ready to use,
`spike.py <https://github.com/astagi/python-orbit/blob/master/spike.py>`__
is a good starting point

Execute queries
~~~~~~~~~~~~~~~

Python Orbit client allows you to use `Orbit
API <https://docs.orbit.love/reference>`__ with Python.

.. code:: py

   from orbit import Orbit


   client = Orbit(auth="YourAuthKey")

   print (client.get_workspaces())

Deal with errors
~~~~~~~~~~~~~~~~

If there’s an error in your query, a ``OrbitException`` will be raised

.. code:: py

   from orbit import Orbit, OrbitException


   client = Orbit(auth="YourAuthKey")
   try:
       client.get_workspaces()
   except OrbitException as ex:
       print (ex)

Run tests
---------

.. code:: sh

   pip install -r requirements-dev.txt
   make test

.. |Latest Version| image:: https://img.shields.io/pypi/v/python-orbit.svg
   :target: https://pypi.python.org/pypi/python-orbit/
.. |codecov| image:: https://codecov.io/gh/astagi/python-orbit/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/astagi/python-orbit
.. |Build Status| image:: https://travis-ci.org/astagi/python-orbit.svg?branch=master
   :target: https://travis-ci.org/astagi/python-orbit
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/astagi/python-orbit/blob/master/LICENSE
