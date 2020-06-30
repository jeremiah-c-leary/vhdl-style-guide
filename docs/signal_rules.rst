Signal Rules
------------

signal_001
##########

This rule checks the indent of signal declarations.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

   signal wr_en : std_logic;
        signal rd_en : std_logic;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     signal wr_en : std_logic;
     signal rd_en : std_logic;

   begin

signal_002
##########

This rule checks the **signal** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   SIGNAL wr_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

signal_003
##########

This rule was depricated and replaced with rules:  function_015, package_019, procedure_010, architecture_029 and process_037.

signal_004
##########

This rule checks the signal name has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   signal WR_EN : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

signal_005
##########

This rule checks for a single space after the colon.

**Violation**

.. code-block:: vhdl

   signal wr_en :    std_logic;
   signal rd_en :std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en : std_logic;

signal_006
##########

This rule checks for at least a single space before the colon.

**Violation**

.. code-block:: vhdl

   signal wr_en: std_logic;
   signal rd_en   : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en   : std_logic;

signal_007
##########

This rule checks for default assignments in signal declarations.

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic := '0';

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

signal_008
##########

This rule checks for valid prefixes on signal identifiers.
Default signal prefix is *s\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal s_wr_en : std_logic;
   signal s_rd_en : std_logic;

signal_010
##########

This rule checks the signal type has proper case if it is a VHDL keyword.

.. NOTE:: This rule is disabled by default.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   signal wr_en   : STD_LOGIC;
   signal rd_en   : Std_logic;
   signal cs_f    : t_User_Defined_Type;

**Fix**

.. code-block:: vhdl

   signal wr_en   : std_logic;
   signal rd_en   : std_logic;
   signal cs_f    : t_User_Defined_Type;

signal_011
##########

This rule checks the signal type has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   signal wr_en   : STD_LOGIC;
   signal rd_en   : Std_logic;
   signal cs_f    : t_User_Defined_Type;

**Fix**

.. code-block:: vhdl

   signal wr_en   : std_logic;
   signal rd_en   : std_logic;
   signal cs_f    : t_user_defined_type;

signal_012
##########

This rule checks multiple signal assignments on a single line are column aligned.

.. NOTE::
    The :'s will be aligned with rule *signal_009*.
    This rule will only cover two signals on a single line.

**Violation**

.. code-block:: vhdl

   signal wr_en, wr_en_f             : std_logic;
   signal rd_en_f, rd_en             : std_logic;
   signal chip_select, chip_select_f : t_user_defined_type;

**Fix**

.. code-block:: vhdl

   signal wr_en,       wr_en_f       : std_logic;
   signal rd_en_f,     rd_en         : std_logic;
   signal chip_select, chip_select_f : t_user_defined_type;

signal_014
##########

This rule checks for consistent capitalization of signal names.

**Violation**

.. code-block:: vhdl

   architecture rtl of entity1 is

     signal sig1 : std_logic;
     signal sig2 : std_logic;

   begin

     proc_name : process (siG2) is
     begin

       siG1 <= '0';

       if (SIG2 = '0') then
         sIg1 <= '1';
       elisif (SiG2 = '1') then
         SIg1 <= '0';
       end if;

     end process proc_name;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   architecture rtl of entity1 is

     signal sig1 : std_logic;
     signal sig2 : std_logic;

     proc_name : process (sig2) is
     begin

       sig1 <= '0';

       if (sig2 = '0') then
         sig1 <= '1';
       elisif (sig2 = '1') then
         sig1 <= '0';
       end if;

     end process proc_name;

   end architecture rtl;

signal_015
==========

This rule checks for multiple signal names defined in a single signal declaration.
By default, this rule will only flag more than two signal declarations.

Refer to the section `Configuring Number of Signals in Signal Declaration <configuring_number_of_signals.html>`_ for information on changing the default.

**Violation**

.. code-block:: vhdl

   signal sig1, sig2
     sig3, sig4,
     sig5
     : std_logic;

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic;
   signal sig2 : std_logic;
   signal sig3 : std_logic;
   signal sig4 : std_logic;
   signal sig5 : std_logic;
   
signal_016
==========

This rule checks the signal declaration is on a single line.

**Violation**

.. code-block:: vhdl

   signal sig1
     : std_logic;

   signal sig2 :
     std_logic;

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic;

   signal sig2 : std_logic;
