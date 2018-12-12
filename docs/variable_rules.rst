Variable Rules
--------------

variable_001
############

This rule checks the indent of variable declarations.

**Violation**

.. code-block:: vhdl

   PROC : process () is

   variable count : integer;
         variable counter : integer;

   begin

**Fix**

.. code-block:: vhdl

   PROC : process () is

     variable count : integer;
     variable counter : integer;

   begin

variable_002
############

This rule checks the **variable** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   VARIABLE count : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_003
############

This rule checks for a single space after the **variable** keyword.

**Violation**

.. code-block:: vhdl

   variable     count : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_004
############

This rule checks the variable name is lowercase.

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

variable_009
############

This rule checks the alignment of colons over multiple lines in the architecture declarative region.

**Violation**

.. code-block:: vhdl

   architecture ARCH of ENTITY1 is

     variable count : integer;
     variable counter : integer;

   begin

**Fix**

.. code-block:: vhdl

   architecture ARCH of ENTITY1 is

     variable count   : integer;
     variable counter : integer;

   begin

variable_010
############

This rule checks the variable type is lowercase.

**Violation**

.. code-block:: vhdl

   variable count : INTEGER;

**Fix**

.. code-block:: vhdl

   variable count : integer;


variable_011
############

This rule checks the alignment of colons over multiple lines in the process declarative region.
Each process is aligned independently.

**Violation**

.. code-block:: vhdl

   PROC_1 : process (A) is

     variable count : integer;
     variable counter : integer;

   begin

   end process PROC_1:

   PROC_2 : process (B) is

     variable write_enable : integer;
     variable read_enable : integer;

   begin

   end process PROC_2;

**Fix**

.. code-block:: vhdl

   PROC_1 : process (A) is

     variable count   : integer;
     variable counter : integer;

   begin

   end process PROC_1:

   PROC_2 : process (B) is

     variable write_enable : integer;
     variable read_enable  : integer;

   begin

   end process PROC_2;
