.. include:: includes.rst

Range Rules
-----------

These rules cover the range definitions in signals, constants, ports and other cases where ranges are defined.

range_001
#########

|phase_6| |error| |case| |case_keyword|

This rule checks the case of the **downto** keyword.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   signal sig1 : std_logic_vector(3 DOWNTO 0);
   signal sig2 : std_logic_vector(16 downTO 1);

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic_vector(3 downto 0);
   signal sig2 : std_logic_vector(16 downTO 1);

range_002
#########

|phase_6| |error| |case| |case_keyword|

This rule checks the case of the **to** keyword.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   signal sig1 : std_logic_vector(3 TO 0);
   signal sig2 : std_logic_vector(16 tO 1);

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic_vector(3 to 0);
   signal sig2 : std_logic_vector(16 to 1);

