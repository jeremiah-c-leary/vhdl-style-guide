Architecture Rules
------------------

architecture_001
################

This rule checks for blank spaces before the **architecture** keyword.

**Violation**

.. code-block:: vhdl

     architecture RTL of FIFO is
   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin

architecture_002
################

This rule checks for a single space between **architecture**, **of**, and **is** keywords.

**Violation**

.. code-block:: vhdl

   architecture  RTL  of    FIFO   is

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

architecture_003
################

This rule check for a blank line above the **architecture** declaration.

**Violation**

.. code-block:: vhdl

   library ieee;
   architecture RTL of FIFO is

**Fix**

.. code-block:: vhdl

   library ieee;

   architecture RTL of FIFO is

architecture_004
################

This rule checks the proper case of the **architecture** keyword in the architecture declaration.

.. NOTE:: The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ARCHITECTURE RTL of FIFO is

.. code-block:: vhdl

   architecture RTL of FIFO is

architecture_005
################

This rule checks the **of** keyword is on the same line as the **architecture** keyword.

**Violation**

.. code-block:: vhdl

   architecture RTL
     of FIFO is

**Fix**

.. code-block:: vhdl

   architecture RTL of
   FIFO is

architecture_006
################

This rule checks the **is** keyword is on the same line as the **architecture** keyword.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO
     is

   architecture RTL of FIFO

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

   architecture RTL of FIFO is

architecture_007
################

This rule checks for spaces before the **begin** keyword.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is
     begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin

architecture_008
################

This rule checks for spaces before the **end architecture** keywords.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin
     end architecture

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin
   end architecture

architecture_009
################

This rule checks the **end** and **architecture** keywords have proper case.

.. NOTE:: The default is lowercase.

**Violation**

.. code-block:: vhdl

   END architecture;

   end Architecture;

**Fix**

.. code-block:: vhdl

   end architecture;

   end architecture;

architecture_010
################

This rule checks for the keyword **architecture** in the **end architecture** statement.
It is clearer to the reader to state what is ending.

**Violation**

.. code-block:: vhdl

   end ARCHITECTURE_NAME;

**Fix**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;

architecture_011
################

This rule checks the architecture name case in the **end architecture** statement.

.. NOTE:: The default is uppercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.


**Violation**

.. code-block:: vhdl

   end architecture architecture_name;

**Fix**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;

architecture_012
################

This rule checks for a single space between **end** and **architecture** keywords.

**Violation**

.. code-block:: vhdl

   end    architecture ARCHITECTURE_NAME;

**Fix**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;
 
architecture_013
################

This rule checks the case of the architecture name in the architecture declaration.

.. NOTE:: The default is uppercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture rtl of FIFO is

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is


architecture_014
################

This rule checks the case of the entity name in the architecture declaration.

.. NOTE:: The default is uppercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture RTL of fifo is

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

architecture_015
################

This rule check for a blank line below the architecture declaration.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is
     signal wr_en : std_logic;
   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     signal wr_en : std_logic;
   begin


architecture_016
################

This rule checks for a blank line above the **begin** keyword.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

     signal wr_en : std_logic;
   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     signal wr_en : std_logic;

   begin


architecture_017
################

This rule checks for a blank line below the **begin** keyword.

**Violation**

.. code-block:: vhdl

   begin
     wr_en <= '0';

**Fix**

.. code-block:: vhdl

   begin

     wr_en <= '0';

architecture_018
################

This rule checks for a blank line above the **end architecture** declaration.

**Violation**

.. code-block:: vhdl

     rd_en <= '1';
   end architecture RTL;

**Fix**

.. code-block:: vhdl

     rd_en <= '1';

   end architecture RTL;

architecture_019
################

This rule checks the proper case of the **of** keyword in the architecture declaration.

.. NOTE:: The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture RTL OF FIFO is

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

architecture_020
################

This rule checks the proper case of the **is** keyword in the architecture declaration.

.. NOTE:: The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO IS

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

architecture_021
################

This rule checks the proper case of the **begin** keyword.

.. NOTE:: The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is
   BEGIN

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin
 
architecture_022
################

This rule checks for a single space before the entity name in the end architecture declaration.

**Violation**

.. code-block:: vhdl

   end architecture    FIFO;

**Fix**

.. code-block:: vhdl

   end architecture FIFO;
 
architecture_023
################

This rule ensures the inline comments are aligned between the architecture declaration and the **begin** keyword.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

     signal wr_en : std_logic;   -- Enables writes to FIFO
     signal rd_en : std_logic;  -- Enables reads from FIFO
     signal overflow : std_logic;    -- Indicates the FIFO has overflowed when asserted

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     signal wr_en : std_logic;       -- Enables writes to FIFO
     signal rd_en : std_logic;       -- Enables reads from FIFO
     signal overflow : std_logic;    -- Indicates the FIFO has overflowed when asserted

   begin
 
architecture_024
################

This rule checks for the architecture name in the **end architecture** statement.
It is clearer to the reader to state which architecture the end statement is closing.

**Violation**

.. code-block:: vhdl

   end architecture;

**Fix**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;

architecture_025
################

This rule checks for valid names for the architecture.
Typical architecture names are:  RTL, EMPTY, and BEHAVE.
This rule allows the user to restrict what can be used for an architecture name.

.. NOTE:: This rule is disabled by default.
   You can enable and configure the names using the following configuration.

   .. code-block:: yaml

      ---

      rule :
        architecture_025 :
          disabled : False
          names :
            - rtl
            - empty
            - behave

**Violation**

.. code-block:: vhdl

   architecture SOME_INVALID_ARCH_NAME of ENTITY1 is

**Fix**

The user is required to decide which is the correct architecture name.
