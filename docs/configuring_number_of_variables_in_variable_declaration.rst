
.. _configuring-number-of-variables-in-variable-declaration:

Configuring Number of Variables in Variable Declaration
-------------------------------------------------------

VHDL allows of any number of variables to be declared within a single variable declaration.
While this may be allowed, in practice there are limits imposed by the designers.
Limiting the number of variables declared improves the readability of VHDL code.

The default number of variables allowed, 2, can be set by configuring rule **variable_015**.

Overriding Number of variables
##############################

The default setting can be changed using a configuration.
We can use the following configuration to change the number of variables allowed to 1.

.. code-block:: yaml

   ---

   rule :
     variable_015 :
        consecutive : 1

Rules Enforcing Number of variables
#################################

* `variable_015 <variable_rules.html#variable-015>`_
