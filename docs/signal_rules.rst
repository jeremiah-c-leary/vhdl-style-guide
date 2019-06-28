Signal Rules
------------

signal_001
##########

This rule checks the indent of signal declarations.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

   signal wr_en : std_logic;
        signal rd_en : std_logic;

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     signal wr_en : std_logic;
     signal rd_en : std_logic;

   begin

signal_002
##########

This rule checks the **signal** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   SIGNAL wr_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

signal_003
##########

This rule checks for spaces after the **signal** keyword.

**Violation**

.. code-block:: vhdl

   signal     wr_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

.. NOTE:: The number of spaces after the **signal** keyword is configurable.
   Use the following YAML file example to change the default number of spaces.

   .. code-block:: yaml

   rule:
     signal_003:
         spaces: 3 

signal_004
##########

This rule checks the signal name is lowercase.

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

This rule checks for valid prefixes on signal names.

.. NOTE::

   Prefixes are disabled by default.
   To enable prefixes, set the prefixes attribute on the rule.

   Example JSON configuration:

   .. code-block:: json
   
      {
        "rule":{
          "signal_008":{
             "prefixes":[
                "w_", "q_", "d_"
             ]
          }
        }
      }

**Violation**

.. code-block:: vhdl

   signal wr_en   : std_logic;
   signal rd_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal q_wr_en : std_logic;
   signal w_rd_en : std_logic;

signal_009
##########

This rule has be renumbered signal_013.

signal_010
##########

This rule checks the signal type is lowercase if it is a VHDL keyword.

.. NOTE:: This rule is disabled by default.

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

This rule checks the signal type is lowercase.

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

signal_013
##########

This rule checks the colons are aligned for all signals in the architecture declarative region.

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en   : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en   : std_logic;
   signal rd_en   : std_logic;

signal_014
##########

This rule checks for consistent capitalization of signal names.

**Violation**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     signal sig1 : std_logic;
     signal sig2 : std_logic;

   begin

     PROC_NAME : process (siG2) is
     begin

       siG1 <= '0';

       if (SIG2 = '0') then
         sIg1 <= '1';
       elisif (SiG2 = '1') then
         SIg1 <= '0';
       end if;

     end process PROC_NAME;

   end architecture RTL;

**Fix**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     signal sig1 : std_logic;
     signal sig2 : std_logic;

     PROC_NAME : process (sig2) is
     begin

       sig1 <= '0';

       if (sig2 = '0') then
         sig1 <= '1';
       elisif (sig2 = '1') then
         sig1 <= '0';
       end if;

     end process PROC_NAME;

   end architecture RTL;
