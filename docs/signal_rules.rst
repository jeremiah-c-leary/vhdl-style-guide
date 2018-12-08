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

This rule checks for a single space after the **signal** keyword.

**Violation**

.. code-block:: vhdl

   signal     wr_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

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

This rule checks the colons are aligned for all signals in the architecture declarative region.

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en   : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en   : std_logic;
   signal rd_en   : std_logic;

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
