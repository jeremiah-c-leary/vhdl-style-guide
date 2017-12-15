Case Rules
----------

case_001
########

This rule checks the indent of **case**, **when**, and **end case** keywords.

**Violation**

.. code-block:: vhdl


   case data is
 
       when 0 =>
   when 1 =>
           when 3 =>
 
  end case;

**Fix**

.. code-block:: vhdl

  case data is
 
    when 0 =>
    when 1 =>
    when 3 =>
 
  end case;

case_002
########

This rule checks for a single space after the **case** keyword.

**Violation**

.. code-block:: vhdl

   case    data is


**Fix**

.. code-block:: vhdl

   case data is

case_003
########

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   case data    is

**Fix**

.. code-block:: vhdl

   case data is

case_004
########

This rule checks for a single space after the **when** keyword.

**Violation**

.. code-block:: vhdl

  case data is

    when   3 =>

**Fix**

.. code-block:: vhdl

  case data is

    when 3 =>

case_005
########

This rule checks for a single space before the **=>** operator.

**Violation**

.. code-block:: vhdl

  case data is

    when 3   =>

**Fix**

.. code-block:: vhdl

  case data is

    when 3 =>

case_006
########

This rule checks for a single space between the **end** and **case** keywords.

**Violation**

.. code-block:: vhdl

  case data is

  end    case;

**Fix**

.. code-block:: vhdl

  case data is

  end case;

case_007
########

This rule checks for a blank line before the **case** keyword.

**Violation**

.. code-block:: vhdl

   a <= '1';
   case data is

**Fix**

.. code-block:: vhdl

   a <= '1';

   case data is

case_008
########

This rule checks for a blank line below the **case** keyword.

**Violation**

.. code-block:: vhdl

   case data is
     when 0 =>

**Fix**

.. code-block:: vhdl

   case data is

     when 0 =>

case_009
########

This rule checks for a blank line above the **end case** keywords.

**Violation**

.. code-block:: vhdl

     when others =>
       null;
   end case;

**Fix**

.. code-block:: vhdl

     when others =>
       null;

   end case;

case_010
########

This rule checks for a blank line below the **end case** keywords.

**Violation**

.. code-block:: vhdl

   end case;
   a <= '1';

**Fix**

.. code-block:: vhdl

   end case;

   a <= '1';

case_011
########

This rule checks the alignment of multiline **when** statements.

**Violation**

.. code-block:: vhdl

   case data is

     when 0 | 1 | 2 | 3
      4 | 5 | 7 =>

**Fix**

.. code-block:: vhdl

   case data is

     when 0 | 1 | 2 | 3
          4 | 5 | 7 =>

case_012
########

This rule checks for code after the **=>** operator.

**Violation**

.. code-block:: vhdl

   when 0 => a <= '1';

**Fix**

.. code-block:: vhdl

   when 0 =>
     a <= '1';

case_013
########

This rule checks the indent of the **null** keyword.

**Violation**

.. code-block:: vhdl

     when others =>
        null;
  
     when others =>
   null;

**Fix**

.. code-block:: vhdl

   when others =>
     null;

   when others =>
     null;
