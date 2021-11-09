.. include:: icons.rst

Variable Rules
--------------

variable_001
############

|phase_4| |error| |indent|

This rule checks the indent of variable declarations.

**Violation**

.. code-block:: vhdl

   proc : process () is

   variable count : integer;
         variable counter : integer;

   begin

**Fix**

.. code-block:: vhdl

   proc : process () is

     variable count : integer;
     variable counter : integer;

   begin

variable_002
############

|phase_6| |error|

This rule checks the **variable** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   VARIABLE count : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_003
############

This rule was depricated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

variable_004
############

|phase_6| |error|

This rule checks the variable name has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   variable COUNT : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_005
############

|phase_2| |error| |whitespace|

This rule checks there is a single space after the colon.

**Violation**

.. code-block:: vhdl

   variable count   :integer;
   variable counter :     integer;

**Fix**

.. code-block:: vhdl

   variable count   : integer;
   variable counter : integer;

variable_006
############

|phase_2| |error|

This rule checks for at least a single space before the colon.

**Violation**

.. code-block:: vhdl

   variable count: integer;
   variable counter : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;
   variable counter : integer;

variable_007
############

|phase_1| |error|

This rule checks for default assignments in variable declarations.

**Violation**

.. code-block:: vhdl

   variable count : integer := 32;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_010
############

|phase_6| |error|

This rule checks the variable type has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   variable count : INTEGER;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_011
############

|phase_6| |error|

This rule checks for consistent capitalization of variable names.

**Violation**

.. code-block:: vhdl

   architecture rtl of entity1 is

     shared variable var1 : std_logic;
     shared variable var2 : std_logic;

   begin

     proc_name : process () is

       variable var3 : std_logic;
       variable var4 : std_logic;

     begin

       Var1 <= '0';

       if (VAR2 = '0') then
         vaR3 <= '1';
       elisif (var2 = '1') then
         VAR4 <= '0';
       end if;

     end process proc_name;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   proc_name : process () is

     variable var1 : std_logic;
     variable var2 : std_logic;
     variable var3 : std_logic;
     variable var4 : std_logic;

   begin

     var1 <= '0';

     if (var2 = '0') then
       var3 <= '1';
     elisif (var2 = '1') then
       var4 <= '0';
     end if;

   end process proc_name;

variable_012
############

|phase_7| |disabled| |error|

This rule checks for valid prefixes on variable identifiers.
The default variable prefix is *v\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   variable my_var : natural;

**Fix**

.. code-block:: vhdl

   variable v_my_var : natural;

variable_600
############

|phase_7| |disabled| |error|

This rule checks for valid suffix on variable identifiers.
The default variable suffix is *\_v*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   variable my_var : natural;

**Fix**

.. code-block:: vhdl

   variable my_var_v : natural;
