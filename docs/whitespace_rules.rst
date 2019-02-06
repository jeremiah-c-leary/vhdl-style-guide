Whitespace Rules
----------------

whitespace_001
##############

This rule checks for spaces at the end of lines.

**Violation**

.. code-block:: vhdl

   entity FIFO is    

**Fix**

.. code-block:: vhdl

   entity FIFO is

whitespace_002
##############

This rule checks for tabs.

**Violation**

.. code-block:: vhdl

   port (
       WR_EN : in    std_logic;

**Fix**

.. code-block:: vhdl

   port (
     WR_EN : in    std_logic;

whitespace_003
##############

This rule checks for spaces before semicolons.

**Violation**

.. code-block:: vhdl

   WR_EN : in    std_logic      ;

**Fix**

.. code-block:: vhdl

   WR_EN : in    std_logic;

whitespace_004
##############

This rule checks for spaces before commas.

**Violation**

.. code-block:: vhdl

   WR_EN => wr_en    ,
   RD_EN => rd_en,

**Fix**

.. code-block:: vhdl

   WR_EN => wr_en,
   RD_EN => rd_en,

whitespace_005
##############

This rule checks for spaces after an open parenthesis.

.. NOTE::
   Spaces before numbers are allowed.

**Violation**

.. code-block:: vhdl

   signal data        : std_logic_vector(31 downto 0);
   signal byte_enable : std_logic_vector( 3 downto 0);
   signal width       : std_logic_vector(  G_WIDTH - 1 downto 0);

**Fix**

.. code-block:: vhdl

   signal data        : std_logic_vector(31 downto 0);
   signal byte_enable : std_logic_vector( 3 downto 0);
   signal width       : std_logic_vector(G_WIDTH - 1 downto 0);

whitespace_006
##############

This rule checks for spaces before a close parenthesis.

**Violation**

.. code-block:: vhdl

   signal data        : std_logic_vector(31 downto 0    );
   signal byte_enable : std_logic_vector( 3 downto 0 );
   signal width       : std_logic_vector(G_WIDTH - 1 downto 0);

**Fix**

.. code-block:: vhdl

   signal data        : std_logic_vector(31 downto 0);
   signal byte_enable : std_logic_vector( 3 downto 0);
   signal width       : std_logic_vector(G_WIDTH - 1 downto 0);

whitespace_007
##############

This rule checks for spaces after a comma.

**Violation**

.. code-block:: vhdl

   PROC : process (wr_en,rd_en,overflow) is

**Fix**

.. code-block:: vhdl

   PROC : process (wr_en, rd_en, overflow) is

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

whitespace_009
##############

This rule checks for spaces before the concate (&) operator.

**Violation**

.. code-block:: vhdl

   a <= b& c;

**Fix**

.. code-block:: vhdl

   a <= b & c;

whitespace_010
##############

This rule checks for spaces after the concate (&) operator.

**Violation**

.. code-block:: vhdl

   a <= b &c;

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

  a <= b;


  c <= d;

**Fix**

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
