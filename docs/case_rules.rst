.. include:: icons.rst

Case Rules
----------

case_001
########

|phase_4| |error| |indent|

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

|phase_2| |error| |whitespace|

This rule checks for a single space after the **case** keyword.

**Violation**

.. code-block:: vhdl

   case    data is


**Fix**

.. code-block:: vhdl

   case data is

case_003
########

|phase_2| |error| |whitespace|

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   case data    is

**Fix**

.. code-block:: vhdl

   case data is

case_004
########

|phase_2| |error| |whitespace|

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

|phase_2| |error| |whitespace|

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

|phase_2| |error| |whitespace|

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

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **case** keyword.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

   a <= '1';
   case data is


   -- This is a comment
   case data is

**Fix**

.. code-block:: vhdl

   a <= '1';

   case data is


   -- This is a comment
   case data is

case_008
########

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **is** keyword.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

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

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **end** keyword.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

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

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **end case** keywords.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

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

|phase_4| |error| |alignment|

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

|phase_1| |error| |structure|

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

|phase_4| |error| |indent|

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

case_014
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **case** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

     CASE address is

     Case address is

     case address is

**Fix**

.. code-block:: vhdl

     case address is

     case address is

     case address is

case_015
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

     case address IS

     case address Is

     case address iS

**Fix**

.. code-block:: vhdl

     case address is

     case address is

     case address is

case_016
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **when** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

     WHEN a =>
     When b =>
     when c =>

**Fix**

.. code-block:: vhdl

     when a =>
     when b =>
     when c =>

case_017
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword in the **end case** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

      End case;
      END case;
      end case;

**Fix**

.. code-block:: vhdl

      end case;
      end case;
      end case;

case_018
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **case** keyword has proper case in the **end case**.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

      end CASE;
      end CAse;
      end case;

**Fix**

.. code-block:: vhdl

      end case;
      end case;
      end case;

case_019
########

|phase_1| |error| |structure|

This rule checks for labels before the **case** keyword.
The label should be removed.
The preference is to have comments above the case statement.

**Violation**

.. code-block:: vhdl

      CASE_LABEL : case address is
      CASE_LABEL: case address is
      case address is

**Fix**

.. code-block:: vhdl

      case address is
      case address is
      case address is

case_020
########

|phase_1| |error| |structure|

This rule checks for labels after the **end case** keywords.
The label should be removed.
The preference is to have comments above the case statement.

**Violation**

.. code-block:: vhdl

      end case CASE_LABEL;
      end case;

**Fix**

.. code-block:: vhdl

      end case;
      end case;

case_021
########

|phase_4| |error| |alignment|

This rule aligns consecutive comment only lines above a **when** keyword in a case statement with the **when** keyword.

**Violation**

.. code-block:: vhdl

       -- comment 1
 -- comment 2
    -- comment 3
   when wr_en =>
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   -- comment 1
   -- comment 2
   -- comment 3
   when wr_en =>
     rd_en <= '0';

