.. include:: includes.rst

Attribute Rules
---------------

attribute_001
#############

This rule has been superceeded by:

* `attribute_declaration_300 <attribute_declaration_rules.html#attribute-declaration-300>`_
* `attribute_specification_300 <attribute_specification_rules.html#attribute-specification-300>`_

attribute_002
#############

This rule has been superceeded by:

* `attribute_declaration_500 <attribute_declaration_rules.html#attribute-declaration-500>`_
* `attribute_specification_500 <attribute_specification_rules.html#attribute-specification-500>`_

attribute_500
#############

|phase_6| |error| |case| |case_keyword|

This rule checks predefined attributes have the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   signal data : std_logic_vector(g_width'RANGE);

**Fix**

.. code-block:: vhdl

   signal data : std_logic_vector(g_width'range);

