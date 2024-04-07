Development Environment
-----------------------

Follow these steps to setup the development environment.

Clone the repo
##############

Clone the repo with the following command:

.. code-block:: bash

   $ git clone https://github.com/jeremiah-c-leary/vhdl-style-guide.git

Setup alias
###########

Set an alias to VSG as follows:

.. code-block:: bash

   $ set alias vsg='python3 <path_to_clone_directory>/bin/vsg'

This allows you to execute VSG without installing it.

Install prerequisites
#####################

.. code-block:: bash

   $ pip install PyYAML
   $ pip install tox

Build locally, artifacts will appear in ``dist`` directory.

.. code-block:: bash

   tox
