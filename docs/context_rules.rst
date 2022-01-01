.. include:: icons.rst

Context Rules
-------------

context_001
###########

|phase_4| |error| |indent|

This rule checks the indent of the **context** keyword.

**Violation**

.. code-block:: vhdl

     context c1 is

     library ieee;

**Fix**

.. code-block:: vhdl

   context c1 is

     library ieee;

context_002
###########

|phase_2| |error| |whitespace|

This rule checks for a single space between the **context** keyword and the context identifier.

**Violation**

.. code-block:: vhdl

   context   c1 is

**Fix**

.. code-block:: vhdl

   context c1 is

context_003
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **context** keyword.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

   library ieee;
   context c1 is

   --Some Comment
   context c1 is

**Fix**

.. code-block:: vhdl

   library ieee;

   context c1 is

   --Some Comment
   context c1 is

context_004
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **context** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   CONTEXT c1 is

**Fix**

.. code-block:: vhdl

   context c1 is

context_005
###########

|phase_1| |error| |structure|

This rule checks the context identifier is on the same line as the **context** keyword.

**Violation**

.. code-block:: vhdl

   context
   c1
     is

**Fix**

.. code-block:: vhdl

   context c1
     is

context_006
###########

|phase_1| |error| |structure|

This rule checks the **is** keyword is on the same line as the context identifier.

**Violation**

.. code-block:: vhdl

   context c1
     is

**Fix**

.. code-block:: vhdl

   context c1 is

context_007
###########

|phase_1| |error| |structure|

This rule checks for code after the **is** keyword.

**Violation**

.. code-block:: vhdl

   context c1 is -- Comments are allowed

   context c1 is library ieee; -- This is not allowed

**Fix**

.. code-block:: vhdl

   context c1 is -- Comments are allowed

   context c1 is
     library ieee; -- This is not allowed

context_008
###########

|phase_1| |error| |structure|

This rule checks the **end** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   context c1 is library ieee; end context c1;

   context c1 is library ieee; end;

**Fix**

.. code-block:: vhdl

   context c1 is library ieee;
   end context c1;

   context c1 is library ieee;
   end;

context_009
###########

|phase_1| |error| |structure|

This rule checks the **context** keyword is on the same line as the end context keyword.

**Violation**

.. code-block:: vhdl

   end
   context c1;

**Fix**

.. code-block:: vhdl

   end context
     c1;

context_010
###########

|phase_1| |error| |structure|

This rule checks the context identifier is on the same line as the end context keyword.

**Violation**

.. code-block:: vhdl

   end context
   c1;

**Fix**

.. code-block:: vhdl

   end context c1;

context_011
###########

|phase_1| |error| |structure|

This rule checks the semicolon is on the same line as the **end** keyword.

**Violation**

.. code-block:: vhdl

   end
   ;

   end context
   ;

   end context c1
   ;


**Fix**

.. code-block:: vhdl

   end;

   end context;

   end context c1;

context_012
###########

|phase_6| |error| |case| |case_name|

This rule checks the context identifier has proper case in the context declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   context C1 is

**Fix**

.. code-block:: vhdl

   context c1 is

context_013
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case in the context declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   context c1 IS

**Fix**

.. code-block:: vhdl

   context c1 is

context_014
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   End;

   END context;

**Fix**

.. code-block:: vhdl

   end;

   end context;

context_015
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the context keyword has proper case in the end context declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end CONTEXT;

**Fix**

.. code-block:: vhdl

   end context;

context_016
###########

|phase_6| |error| |case| |case_name|

This rule checks the context identifier has proper case in the end context declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end context C1;

**Fix**

.. code-block:: vhdl

   end context c1;

context_017
###########

|phase_2| |error| |whitespace|

This rule checks for a single space between the context identifier and the **is** keyword.

**Violation**

.. code-block:: vhdl

   context c1    is

**Fix**

.. code-block:: vhdl

   context c1 is

context_018
###########

|phase_2| |error| |whitespace|

This rule checks for a single space between the **end** keyword and the **context** keyword.

**Violation**

.. code-block:: vhdl

   end;

   end   context;

**Fix**

.. code-block:: vhdl

   end;

   end context;

context_019
###########

|phase_2| |error| |whitespace|

This rule checks for a single space between the **context** keyword and the context identifier.

**Violation**

.. code-block:: vhdl

   end context;

   end context    c1;

**Fix**

.. code-block:: vhdl

   end context;

   end context c1;

context_020
###########

|phase_4| |error| |indent|

This rule checks the indent of the **end** keyword.

**Violation**

.. code-block:: vhdl

   context c1 is
      end context c1;

**Fix**

.. code-block:: vhdl

   context c1 is
   end context c1;

context_021
###########

|phase_1| |error| |structure| |structure_optional|

This rule checks for the keyword **context** in the **end context** statement.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   end c1;

   end;

**Fix**

.. code-block:: vhdl

   end context c1;

   end context;

context_022
###########

|phase_1| |error| |structure| |structure_optional|

This rule checks for the context name in the **end context** statement.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   end context;

**Fix**

.. code-block:: vhdl

   end context c1;

context_023
###########

|phase_3| |error| |blank_line|

This rule adds a blank line below the **is** keyword.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   context c1 is
     library IEEE;

**Fix**

.. code-block:: vhdl

   context c1 is

     library IEEE;

context_024
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **end** keyword.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

     use ieee.std_logic_1164.all;
   end context;

**Fix**

.. code-block:: vhdl

     use ieee.std_logic_1164.all;

   end context;

context_025
###########

|phase_3| |error| |blank_line|

This rule adds a blank line below the context semicolon.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   end context;
   entity fifo is

**Fix**

.. code-block:: vhdl

   end context;

   entity fifo is

context_026
###########

|phase_3| |error| |blank_line|

This rule ensures a single blank line after the **context** keword.

**Violation**

.. code-block:: vhdl

   context c1 is



     library ieee;

**Fix**

.. code-block:: vhdl

   context c1 is

     library ieee;

context_027
###########

|phase_3| |error| |blank_line|

This rule ensures a single blank line before the **end** keword.

**Violation**

.. code-block:: vhdl

     use ieee.std_logic_1164.all;



   end context;

**Fix**

.. code-block:: vhdl

     use ieee.std_logic_1164.all;

   end context;

context_028
###########

.. NOTE:: This rule has not been implemented yet.

This rule checks for alignment of inline comments in the context declaration.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   context c1 is                       -- Some comment
     library ieee;                        -- Other comment
       use ieee.std_logic_1164.all;   -- Comment 3
   end context c1;  -- Comment 4

**Fix**

.. code-block:: vhdl

   context c1 is                    -- Some comment
     library ieee;                  -- Other comment
       use ieee.std_logic_1164.all; -- Comment 3
   end context c1;                  -- Comment 4

