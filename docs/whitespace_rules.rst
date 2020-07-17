Whitespace Rules
----------------

whitespace_001
##############

This rule checks for spaces at the end of lines.

**Violation**

.. code-block:: vhdl

   entity fifo is    

**Fix**

.. code-block:: vhdl

   entity fifo is

whitespace_002
##############

This rule checks for tabs.

**Violation**

.. code-block:: vhdl

   port (
       wr_en : in    std_logic;

**Fix**

.. code-block:: vhdl

   port (
     wr_en : in    std_logic;

whitespace_003
##############

This rule checks for spaces before semicolons.

**Violation**

.. code-block:: vhdl

   wr_en : in    std_logic      ;

**Fix**

.. code-block:: vhdl

   wr_en : in    std_logic;

whitespace_004
##############

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

This rule checks for spaces after a comma.

**Violation**

.. code-block:: vhdl

   proc : process (wr_en,rd_en,overflow) is

**Fix**

.. code-block:: vhdl

   proc : process (wr_en, rd_en, overflow) is

whitespace_008
##############

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

This rule checks for spaces before and after the concate (&) operator.

**Violation**

.. code-block:: vhdl

   a <= b&c;

**Fix**

.. code-block:: vhdl

   a <= b & c;

whitespace_011
##############

This rule checks for spaces before and after math operators +, -, /, and \*.

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

This rule enforces a maximum number of consecutive blank lines.

**Violation**

.. code-block:: vhdl

  a <= b;


  c <= d;

**Fix**

.. code-block:: vhdl

  a <= b;

  c <= d;

.. NOTE::

  The default is set to 1.
  This can be changed by setting the *numBlankLines* attribute to another number.

  .. code-block:: json
  
     {
         "rule":{
             "whitespace_012":{
                 "numBlankLines":3
             }
         }
     }

whitespace_013
##############

This rule checks for spaces before and after logical operators.

**Violation**

.. code-block:: vhdl

  if (a = '1')and(b = '0')
  if (a = '0')or (b = '1')

**Fix**

.. code-block:: vhdl

  if (a = '1') and (b = '0')
  if (a = '0') or (b = '1')
