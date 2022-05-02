.. include:: includes.rst

Alias Declaration Rules
-----------------------

alias_declaration_001
#####################

|phase_1| |error| |structure|

This rule checks the **alias** keyword is on its own line.

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

This rule checks for a single space before the **is** keyword if the : is present.

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

|configuring_uppercase_and_lowercase_rules_link|

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

|configuring_uppercase_and_lowercase_rules_link|

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

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   alias Alias_Designator is name;

**Fix**

.. code-block:: vhdl

   alias alias_designator is name;

alias_declaration_503
#####################

|phase_6| |error| |case|

This rule checks for consistent capitalization of alias designators.

**Violation**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     signal instructure : bit_vector(15 downto 0);
     alias opcode : bit_vector(3 downto 0) is instructure(15 downto 12);

     signal data : std_logic_vector(OPCODE'range);

   begin

     data <= OpCode;

     PROC_NAME : process () is
     begin

       data <= OpCOde;

       if (opCODE = "0110") then
         data <= oPCode;
       end if;

     end process PROC_NAME;

   end architecture RTL;

**Fix**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     signal instructure : bit_vector(15 downto 0);
     alias opcode : bit_vector(3 downto 0) is instructure(15 downto 12);

     signal data : std_logic_vector(opcode'range);

   begin

     data <= opcode;

     PROC_NAME : process () is
     begin

       data <= opcode;

       if (opcode = "0110") then
         data <= opcode;
       end if;

     end process PROC_NAME;

   end architecture RTL;

alias_declaration_600
#####################

|phase_7| |disabled| |error| |naming|

This rule checks for valid prefixes on alias designators.

Default prefix is *a\_*.

|configuring_prefix_and_suffix_rules_link|

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

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   alias header is name;
   alias footer is name;

**Fix**

.. code-block:: vhdl

   alias header_a is name;
   alias footer_a is name;

