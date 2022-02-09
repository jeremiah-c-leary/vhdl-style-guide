
.. _configuring-type-of-instantiations:

Configuring Type of Instantiations
----------------------------------

There are two methods to instantiate components:  component or entity.

VSG can check which method is being used and throw a violation if the incorrect method is detected.

Overriding Type of Instantiation
################################

The default setting is **component** instantiation.
We can use the following configuration to change it to **entity** instantiation.

.. code-block:: yaml

   ---

   rule :
     instantiation_034:
        method: 'entity'

Rules Enforcing Type of Instantiations
######################################

* `instantiation_034 <instantiation_rules.html#instantiation-034>`_
