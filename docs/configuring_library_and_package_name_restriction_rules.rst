
.. _configuring-library-and-package-name-restriction-rules:

Configuring Library and Package Name Restriction Rules
------------------------------------------------------

There are rules which will check for invalid package names in library and use clauses.
These rules are disabled by default and must be enabled before they will perform any checks.

There is one option for these rules:

.. |names| replace::
   :code:`names`

.. |default| replace::
   :code:`std_logic_arith`

.. |values__names| replace::
   List of strings

.. |action__names| replace::
   Search for libraries and packages with the user defined names

+--------------------------------------+-----------------+-----------+------------------------------------------------+
| Option                               |   Values        | Default   | Description                                    |
+======================================+=================+===========+================================================+
| |names|                              | |values__names| | |default| | * |action__names|                              |
+--------------------------------------+-----------------+-----------+------------------------------------------------+

This is an example of how to configure the option.

.. code-block:: yaml

   rule :
     library_012:
        names:
          - "work"
          - "std_logic_arith"

.. NOTE:: All examples below are using the rule **port_map_004**.

Example: |names| set to list ["std_logic_arith"]
################################################

The following code would fail with this option:

.. code-Block:: vhdl

   library ieee;
     use ieee.std_logic_arith.all;

Example: |names| set to ["work", "my_package"]
##############################################

The following code would fail three times with this option:

.. code-block:: vhdl

   library work;
     use work.my_package.all;


Rules Enforcing Valid Names
###########################

* `library_012 <library_rules.html#library-012>`_
* `use_clause_001 <use_clause_rules.html#use-clause-001>`_
