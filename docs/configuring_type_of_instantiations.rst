
.. _configuring-type-of-instantiations:

Configuring Type of Instantiations
----------------------------------

There are two methods to instantiate components:  component or entity.

VSG can check which method is being used and throw a violation if the incorrect method is detected.

.. |method| replace::
   :code:`method`

.. |component_option| replace::
   :code:`component`

.. |entity_option| replace::
   :code:`entity`

.. |method__component| replace::
   :code:`component` = Enforce component instantiation

.. |method__entity| replace::
   :code:`entity` = Enforce entity instantiation

.. |values| replace::
   :code:`component`, :code:`entity`

.. |default_value| replace::
   :code:`component`

+----------------------+----------+-----------------+----------------------------+
| Option               | Values   | Default Value   | Description                |
+======================+==========+=================+============================+
| |method|             | |values| | |default_value| | * |method__component|      |
|                      |          |                 | * |method__entity|         |
+----------------------+----------+-----------------+----------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     instantiation_034:
        method: 'component'

Example: |method| set to |component_option|
###########################################

The following code snippet would fail:

.. code-block:: vhdl

   U_FIFO : entity fifo_dsn.FIFO(RTL)

Example: |method| set to |entity_option|
########################################

The following code snippet would fail:

.. code-block:: vhdl

   U_FIFO : FIFO

Rules Enforcing Type of Instantiations
######################################

* `instantiation_034 <instantiation_rules.html#instantiation-034>`_
