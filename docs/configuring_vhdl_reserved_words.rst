
.. _configuring-vhdl-reserved-words:

Configuring VHDL Reserved Words
-------------------------------

The VHDL Language Reference Manual (LRM) has a section listed reserved words.
The use of these words are restricted in identifiers and names.

There are rules which can check for use of reserved words where they should not be used.
These rules provide the following options:

.. |standard_option| replace::
   :code:`standard`

.. |standard__1987| replace::
   :code:`1987` = Use reserved keywords from 1987 standard

.. |standard__1993| replace::
   :code:`1993` = Use reserved keywords from 1993 standard

.. |standard__2000| replace::
   :code:`2000` = Use reserved keywords from 2000 standard

.. |standard__2002| replace::
   :code:`2002` = Use reserved keywords from 2002 standard

.. |standard__2008| replace::
   :code:`2008` = Use reserved keywords from 2008 standard

.. |standard__2019| replace::
   :code:`2019` = Use reserved keywords from 2019 standard

.. |standard__all| replace::
   :code:`all` = Use reserved keywords from all standards

.. |values| replace::
   :code:`1987`, :code:`1993`, :code:`2000`, :code:`2002`, :code:`2008`, :code:`2019`

.. |default_value| replace::
   :code:`all`

+----------------------+----------+-----------------+----------------------------+
| Option               | Values   | Default Value   | Description                |
+======================+==========+=================+============================+
| |standard_option|    | |values| | |default_value| | * |standard__1987|         |
|                      |          |                 | * |standard__1993|         |
|                      |          |                 | * |standard__2000|         |
|                      |          |                 | * |standard__2002|         |
|                      |          |                 | * |standard__2008|         |
|                      |          |                 | * |standard__2019|         |
|                      |          |                 | * |standard__all|          |
+----------------------+----------+-----------------+----------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     reserved_001:
        standard: 'all'

.. NOTE:: The following examples are using rule reserved_001.

Example: |standard_option| set to :code:`1987`
##############################################

The :code:`null` keyword is a reserved word in the 1987 standard.

    **Violation**

    .. code-block:: yaml

       entity null is
       end entity;

Example: |standard_option| set to :code:`1993`
##############################################

The :code:`rol` keyword is a reserved word in the 1993 standard.

    **Violation**

    .. code-block:: yaml

       entity rol is
       end entity;


Example: |standard_option| set to :code:`2008`
##############################################

The :code:`context` keyword is a reserved word in the 2008 standard.

    **Violation**

    .. code-block:: yaml

       entity context is
       end entity;


Example: |standard_option| set to :code:`2019`
##############################################

The :code:`private` keyword is a reserved word in the 2019 standard.

    **Violation**

    .. code-block:: yaml

       entity private is
       end entity;


Rules Enforcing Optional Items
##############################

* `reserved_001 <reserved_rules.html#reserved-001>`_
