.. include:: includes.rst

IEEE Rules
-----------

IEEE_500
########

|phase_6| |error| |case| |case_keyword|

This rule checks IEEE types have the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    STD_LOGIC;
     RD_EN    : in    STD_logic;
     DATA     : inout STD_LOGIC_VECTOR(31 downto 0)
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     DATA     : inout std_logic_vector(31 downto 0)
   );
