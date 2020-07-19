Context Rules
-------------

context_001
###########

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

This rule checks for a single space after the **context** keyword.

**Violation**

.. code-block:: vhdl

   context   c1 is

**Fix**

.. code-block:: vhdl

   context c1 is

context_003
###########

This rule checks for a blank line above the **context** keyword.

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

This rule checks the **context** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   CONTEXT c1 is

**Fix**

.. code-block:: vhdl

   context c1 is

context_005
###########

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

context_005
###########

This rule checks the **is** keyword is on the same line as the **context** keyword.

**Violation**

.. code-block:: vhdl

   context c1 
     is

**Fix**

.. code-block:: vhdl

   context c1 is

context_006
###########

This rule checks the **is** keyword has proper case in the context declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   context c1 IS

**Fix**

.. code-block:: vhdl

   context c1 is

context_007
###########

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   context c1    is

**Fix**

.. code-block:: vhdl

   context c1 is

context_008
###########

This rule checks the context name has proper case in the context declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   context C1 is 

**Fix**

.. code-block:: vhdl

   context c1 is 

context_009
###########

This rule checks the indent of the **end** keyword.

**Violation**

.. code-block:: vhdl

   use ieee.numeric_std.all;
   end context c1;

**Fix**

.. code-block:: vhdl

     use ieee.numeric_std.all;
   end context c1;

context_010
###########

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END context c1;

**Fix**

.. code-block:: vhdl

   end context c1;

context_011
###########

This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end   context c1;

**Fix**

.. code-block:: vhdl

   end context c1;

context_012
###########

This rule checks the case of the context name in the **end context** statement.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end context C1;

**Fix**

.. code-block:: vhdl

   end context c1;

context_013
###########

This rule checks for a single space after the **context** keyword in the closing of the context declaration.

**Violation**

.. code-block:: vhdl

   end context    c1;

**Fix**

.. code-block:: vhdl

   end context c1;

context_014
###########

This rule checks the **context** keyword has proper case in the closing of the context declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end CONTEXT c1;

**Fix**

.. code-block:: vhdl

   end context c1;

context_015
###########

This rule checks for the keyword **context** in the **end context** statement.

**Violation**

.. code-block:: vhdl

   end c1;

   end;

**Fix**

.. code-block:: vhdl

   end context c1;

   end context;

context_016
###########

This rule checks for blank lines above the **end context** keywords.

**Violation**

.. code-block:: vhdl

     use ieee.std_logic.all; 

   end context c1;


**Fix**

.. code-block:: vhdl

     use ieee.std_logic.all; 

   end context c1;

context_017
###########

This rule checks for the context name in the **end context** statement.

**Violation**

.. code-block:: vhdl

   end context;

**Fix**

.. code-block:: vhdl

   end context c1;

context_018
###########

This rule checks for alignment of inline comments in the context declaration.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

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

