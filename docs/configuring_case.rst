Configuring Uppercase and Lowercase Rules
-----------------------------------------

There are several rules that enforce either uppercase or lowercase.
They are noted in the documentation for each rule what the default is.
The example violation and fixes are in reference to the default setting.

The default value for each of these case rules can be overridden using a configuration.

Overriding Default Case Enforcement
###################################

The default setting can be changed using a configuration.
For example the rule constant_002 defaults to lowercase.
We can use the following configuration to change the case to upper:

.. code-block:: yaml

   ---

   rule :
     constant_002 :
        case : 'upper'

Conversley, rule entity_008 defaults to uppercase.
We can use the following configuration to change the case to lower:

.. code-block:: yaml

   ---

   rule :
     entity_008 :
        case : 'lower'

Changing Multiple Case Rules
############################

If there are a lot of case rules you want to change, you can use the global option to reduce the size of the configuration.
For example, if we want to uppercase everything except the entity name, we could write the following configuration:

.. code-block:: yaml

   ---

   rule :
     global :
       case : 'upper'
     entity_008 :
       case : 'lower'

