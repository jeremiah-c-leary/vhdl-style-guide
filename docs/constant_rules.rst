.. include:: icons.rst

Constant Rules
--------------

constant_001
############

|phase_4| |error|

This rule checks the indent of a constant declaration.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

   constant size : integer := 1;
       constant width : integer := 32

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     constant size : integer := 1;
     constant width : integer := 32


constant_002
############

|phase_6| |error|

This rule checks the **constant** keyword is has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   CONSTANT size : integer := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_003
############

This rule was depricated and replaced with rules:  function_015, package_019, procedure_010, architecture_029 and process_037.

constant_004
############

|phase_6| |error|

This rule checks the constant identifier has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   constant SIZE : integer := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_005
############

|phase_2| |error|

This rule checks for a single space after the colon.

**Violation**

.. code-block:: vhdl

   constant size  :integer := 1;
   constant wdith :     integer := 32;

**Fix**

.. code-block:: vhdl

   constant size  : integer := 1;
   constant width : integer := 32;

constant_006
############

|phase_2| |error|

This rule checks for at least a single space before the colon.

**Violation**

.. code-block:: vhdl

   constant size: integer := 1;
   constant width     : integer := 32;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;
   constant width     : integer := 32;

constant_007
############

|phase_1| |error|

This rule checks the **:=** is on the same line at the **constant** keyword.

**Violation**

.. code-block:: vhdl

   constant size : integer
      := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

**Fix**

.. code-block:: vhdl

   constant size    : integer := 1;
   constant width   : integer := 32


constant_010
############

|phase_2| |error|

This rule checks for a single space before the := keyword in constant declarations.
Having a space makes it clearer where the assignment occurs on the line.

**Violation**

.. code-block:: vhdl

   constant size : integer:= 1;
   constant width : integer   := 10;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;
   constant width : integer := 10;

constant_011
############

|phase_6| |error|

This rule checks the constant type has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   constant size : INTEGER := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_012
############

|phase_4| |error|

This rule checks the indent of multiline constants that contain arrays.

Refer to section `Configuring Multiline Indent Rules <configuring.html#configuring-multiline-indent-rules>`_ for options.

.. NOTE:: The structure of multiline array constants is handled by the rule `constant_016 <constant_rules.html#constant-016>`_.

**Violation**

.. code-block:: vhdl

   constant rom : romq_type :=
   (
            0,
        65535,
        32768
     );

**Fix**

.. code-block:: vhdl

   constant rom : romq_type :=
   (
     0,
     65535,
     32768
   );

constant_013
############

|phase_6| |error|

This rule checks for consistent capitalization of constant names.

**Violation**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     constant c_size  : integer := 5;
     constant c_ones  : std_logic_vector(c_size - 1 downto 0) := (others => '1');
     constant c_zeros : std_logic_vector(c_size - 1 downto 0) := (others => '0');

     signal data : std_logic_vector(c_size - 1 downto 0);

   begin

     data <= C_ONES;

     PROC_NAME : process () is
     begin

       data <= C_ones;

       if (sig2 = '0') then
         data <= c_Zeros;
       end if;

     end process PROC_NAME;

   end architecture RTL;

**Fix**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     constant c_size  : integer := 5;
     constant c_ones  : std_logic_vector(c_size - 1 downto 0) := (others => '1');
     constant c_zeros : std_logic_vector(c_size - 1 downto 0) := (others => '0');

     signal data : std_logic_vector(c_size - 1 downto 0);

   begin

     data <= c_ones;

     PROC_NAME : process () is
     begin

       data <= c_ones;

       if (sig2 = '0') then
         data <= c_zeros;
       end if;

     end process PROC_NAME;

   end architecture RTL;

constant_014
############

|phase_5| |error|

This rule checks the indent of multiline constants that do not contain arrays.

**Violation**

.. code-block:: vhdl

   constant width : integer := a + b +
     c + d;

**Fix**

.. code-block:: vhdl

   constant width : integer := a + b +
                               c + d;

constant_015
############

|phase_7| |disabled| |error|

This rule checks for valid prefixes on constant identifiers.
The default constant prefix is *c\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   constant my_const : integer;

**Fix**

.. code-block:: vhdl

   constant c_my_const : integer;

constant_016
############

|phase_1| |error|

This rule checks the structure of multiline constants that contain arrays.

Refer to section `Configuring Multiline Structure Rules <configuring.html#configuring-multiline-structure-rules>`_ for options.

.. NOTE:: The indenting of multiline array constants is handled by the rule `constant_012 <constant_rules.html#constant-012>`_.

**Violation**

.. code-block:: vhdl

   constant rom : romq_type := (0, 65535, 32768);

**Fix**

.. code-block:: vhdl

   constant rom : romq_type :=
   (
     0,
     65535,
     32768
   );

Naming Convention Rules (600 - 699)
###################################

constant_600
############

|phase_7| |disabled| |error|

This rule checks for valid suffixes on constant identifiers.
The default constant prefix is *\_c*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   constant my_const : integer;

**Fix**

.. code-block:: vhdl

   constant my_const_c : integer;


