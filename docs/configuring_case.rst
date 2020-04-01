Configuring Uppercase and Lowercase Rules
-----------------------------------------

There are several rules that enforce either uppercase or lowercase.
The default for all such rules is :code:`lowercase`.
The decision was motivated by the fact, that the VHDL language is case insensitive.
Having the same default for all case rules also results in less documentation and code to maintain.
The default value for each of these case rules can be overridden using a configuration.

Overriding Default Lowercase Enforcement
########################################

The default lowercase setting can be changed using a configuration.

For example the rule constant_002 can be changed to enforce uppercase using the following configuration:

.. code-block:: yaml

   ---

   rule :
     constant_002 :
        case : 'upper'

Changing Multiple Case Rules
############################

If there are a lot of case rules you want to change, you can use the global option to reduce the size of the configuration.
For example, if you want to uppercase everything except the entity name, you could write the following configuration:

.. code-block:: yaml

   ---

   rule :
     global :
       case : 'upper'
     entity_008 :
       case : 'lower'
