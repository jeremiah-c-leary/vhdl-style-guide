.. include:: icons.rst

Alias Declaration Rules
-----------------------

alias_declaration_001
#####################

|phase_1| |error| |structure|

This rule checks the **alias** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   signal sig1 : std_logic; alias designator is name;

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic;
   alias designator is name;

alias_declaration_100
#####################

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon for the subtype_indication.

**Violation**

.. code-block:: vhdl

   alias alias_designator :    subtype_indication is name;
   alias alias_designator :subtype_indication is name;

**Fix**

.. code-block:: vhdl

   alias alias_designator : subtype_indication is name;
   alias alias_designator : subtype_indication is name;

alias_declaration_101
#####################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **is** keyword if the : is not present.

**Violation**

.. code-block:: vhdl

   alias alias_designator : subtype_indication     is name;
   alias alias_designator   is name;

**Fix**

.. code-block:: vhdl

   alias alias_designator : subtype_indication is name;
   alias alias_designator   is name;

alias_declaration_102
#####################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **is** keyword.

**Violation**

.. code-block:: vhdl

   alias alias_designator is     name;

**Fix**

.. code-block:: vhdl

   alias alias_designator is name;

alias_declaration_300
#####################

|phase_4| |error| |indent|

This rule checks the indent of the **alias** keyword.

**Violation**

.. code-block:: vhdl

   signal sig1 : integer;

     alias is name;

**Fix**

.. code-block:: vhdl

   signal sig1 : integer;

   alias is name;

alias_declaration_500
#####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **alias** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ALIAS alias_designator is name;

**Fix**

.. code-block:: vhdl

   alias alias_designator is name;

alias_declaration_501
#####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   alias alias_designator IS name;

**Fix**

.. code-block:: vhdl

   alias alias_designator is name;

alias_declaration_502
#####################

|phase_6| |error| |case| |case_name|

This rule checks the alias designator has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   alias Alias_Designator is name;

**Fix**

.. code-block:: vhdl

   alias alias_designator is name;

alias_declaration_600
#####################

|phase_7| |disabled| |error| |naming|

This rule checks for valid prefixes on alias designators.

Default prefix is *a\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   alias header is name;
   alias footer is name;

**Fix**

.. code-block:: vhdl

   alias a_header is name;
   alias a_footer is name;

alias_declaration_601
#####################

|phase_7| |disabled| |error| |naming|

This rule checks for valid suffixes on alias designators.

Default prefix is *\_a*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   alias header is name;
   alias footer is name;

**Fix**

.. code-block:: vhdl

   alias header_a is name;
   alias footer_a is name;

