Variable Rules
--------------

variable_001
############

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

This rule checks the **variable** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   VARIABLE count : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_003
############

This rule was depricated and replaced with rules:  function_015, package_019, procedure_010, architecture_029 and process_037.

variable_004
############

This rule checks the variable name has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   variable COUNT : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_005
############

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

This rule checks for default assignments in variable declarations.

**Violation**

.. code-block:: vhdl

   variable count : integer := 32;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_010
############

This rule checks the variable type has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   variable count : INTEGER;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_011
############

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

This rule checks for valid prefixes on variable identifiers.
The default variable prefix is *v\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   variable my_var : natural;

**Fix**

.. code-block:: vhdl

   variable v_my_var : natural;
