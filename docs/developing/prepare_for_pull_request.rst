Prepare for pull request
------------------------

Before creating a pull request use tox to perform all checks against the code base:

.. code-block:: bash

   $ tox

This will run code style checks, unittests against multiple versions of python and attempt to perform a build.
When this passes create a pull request.

.. NOTE:: Issue 1157 https://github.com/jeremiah-c-leary/vhdl-style-guide/issues/1157 is still being resolved and should not gate any PR creation.
