Configuring Disabled Rules
--------------------------

There are several rules which are disabled by default.
These are typically naming convention rules.
They can be enabled by setting the `disable` option to `False` in a configuration.

.. code-block:: yaml

   rule :
     <rule_id>:
         disable: False

Rules Which are Disabled by Default
###################################

* :any:`after_001`
* :any:`after_002`
* :any:`after_003`

