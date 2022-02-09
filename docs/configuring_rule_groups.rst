
.. _configuring-rule-groups:

Configuring Rule Groups
-----------------------

A rule group can be configured using the **group** option.

The following example configures the rules to:

* lower case vhdl keywords
* upper case labels
* upper case non-vhdl keywords
* disable length rules
* disable naming rules

.. code-block:: yaml

   rule:
     group:
        case::keyword:
          case: 'lower'
        case::label:
          case: 'upper'
        case::name:
          case: 'upper'
        length:
          disable: True
        naming:
          disable: Tue

