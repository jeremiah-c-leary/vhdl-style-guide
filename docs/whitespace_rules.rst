.. include:: includes.rst

Whitespace Rules
----------------

whitespace_001
##############

|phase_1| |error| |whitespace|

This rule check for trailing spaces.

**Violation**

Where periods indicate spaces:

.. code-block:: vhdl

    library ieee;....

**Fix**

.. code-block:: vhdl

    library ieee;

whitespace_002
##############

|phase_1| |error| |whitespace|

This rule will check for the existence of tabs in the middle of a line.

**Violation**

.. code-block:: text

   \t\tsignal wr_en\t:\tstd_logic;  --\tWrite Enable

**Fix**

.. code-block:: text

   \t\tsignal wr_en : std_logic;  -- Write Enable

whitespace_003
##############

|phase_2| |error| |whitespace|

This rule checks for spaces before semicolons.

**Violation**

.. code-block:: vhdl

   wr_en : in    std_logic      ;

**Fix**

.. code-block:: vhdl

   wr_en : in    std_logic;

whitespace_004
##############

|phase_2| |error| |whitespace|

This rule checks for spaces before commas.

**Violation**

.. code-block:: vhdl

   wr_en => wr_en    ,
   rd_en => rd_en,

**Fix**

.. code-block:: vhdl

   wr_en => wr_en,
   rd_en => rd_en,

whitespace_005
##############

|phase_2| |error| |whitespace|

This rule checks for spaces after an open parenthesis.

.. NOTE::
   Spaces before numbers are allowed.

**Violation**

.. code-block:: vhdl

   signal data        : std_logic_vector(31 downto 0);
   signal byte_enable : std_logic_vector( 3 downto 0);
   signal width       : std_logic_vector(  g_width - 1 downto 0);

**Fix**

.. code-block:: vhdl

   signal data        : std_logic_vector(31 downto 0);
   signal byte_enable : std_logic_vector( 3 downto 0);
   signal width       : std_logic_vector(g_width - 1 downto 0);

whitespace_006
##############

|phase_2| |error| |whitespace|

This rule checks for spaces before a close parenthesis.

**Violation**

.. code-block:: vhdl

   signal data        : std_logic_vector(31 downto 0    );
   signal byte_enable : std_logic_vector( 3 downto 0 );
   signal width       : std_logic_vector(g_width - 1 downto 0);

**Fix**

.. code-block:: vhdl

   signal data        : std_logic_vector(31 downto 0);
   signal byte_enable : std_logic_vector( 3 downto 0);
   signal width       : std_logic_vector(g_width - 1 downto 0);

whitespace_007
##############

|phase_2| |error| |whitespace|

This rule checks for spaces after a comma.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   proc : process (wr_en,rd_en,overflow) is

**Fix**

.. code-block:: vhdl

   proc : process (wr_en, rd_en, overflow) is

whitespace_008
##############

|phase_2| |error| |whitespace|

This rule checks for spaces after the **std_logic_vector** keyword.

**Violation**

.. code-block:: vhdl

   signal data    : std_logic_vector (7 downto 0);
   signal counter : std_logic_vector    (7 downto 0);

**Fix**

.. code-block:: vhdl

   signal data    : std_logic_vector(7 downto 0);
   signal counter : std_logic_vector(7 downto 0);

whitespace_010
##############

|phase_2| |error| |whitespace|

This rule checks for spaces before and after the concate (&) operator.

**Violation**

.. code-block:: vhdl

   a <= b&c;

**Fix**

.. code-block:: vhdl

   a <= b & c;

whitespace_011
##############

|phase_2| |error| |whitespace|

This rule checks for at least a single space before and after math operators +, -, /, * and **.

**Violation**

.. code-block:: vhdl

   a <= b+c;
   a <= b-c;
   a <= b/c;
   a <= b*c;
   a <= b**c;
   a <= (b+c)-(d-e);

**Fix**

.. code-block:: vhdl

   a <= b + c;
   a <= b - c;
   a <= b / c;
   a <= b * c;
   a <= b ** c;
   a <= (b + c) - (d - e);

whitespace_012
##############

This rule was a duplicate of whitespace_200 and has been removed.

whitespace_013
##############

|phase_2| |error| |whitespace|

This rule checks for at least a single space before and after logical operators.

**Violation**

.. code-block:: vhdl

  if (a = '1')and(b = '0')
  if (a = '0')or (b = '1')

**Fix**

.. code-block:: vhdl

  if (a = '1') and (b = '0')
  if (a = '0') or (b = '1')

whitespace_200
##############

|phase_3| |error| |blank_line|

This rule enforces a maximum number of consecutive blank lines.

|configuring_consecutive_blank_line_rules|

**Violation**

.. code-block:: vhdl

   a <= b;


   c <= d;

**Fix**

.. code-block:: vhdl

   a <= b;

   c <= d;
