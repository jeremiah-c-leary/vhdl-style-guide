Installation
============

There are two methods to install VSG.

PIP
---

The most recent released version is hosted on PyPI.
It can be installed using **pip**.

.. code-block:: bash

  pip install vsg --use-pep517

This is the preferred method for installing VSG.

GitHub
------

The latest development version can be cloned from the GitHub repo.

.. code-block:: bash

  git clone https://github.com/jeremiah-c-leary/vhdl-style-guide.git

Install prerequisites.

.. code-block:: bash

  pip install tox

Build locally, artifacts will appear in ``dist`` directory.

.. code-block:: bash

  tox
