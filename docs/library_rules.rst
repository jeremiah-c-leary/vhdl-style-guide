.. include:: includes.rst

Library Rules
-------------

library_001
###########

|phase_4| |error| |indent|

This rule checks the indent of the **library** keyword.
Indenting helps in comprehending the code.


**Violation**

.. code-block:: vhdl

   library ieee;
      library fifo_dsn;

**Fix**

.. code-block:: vhdl

   library ieee;
   library fifo_dsn;

library_002
###########

|phase_2| |error| |whitespace|

This rule checks for excessive spaces after the **library** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   library    ieee;

**Fix**

.. code-block:: vhdl

   library ieee;

library_003
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **library** keyword.

|configuring_previous_line_rules_link|

There is an additional :code:`allow_library_clause` option which can be set.
Refer to section :ref:`reporting-single-rule-configuration` for details on finding configuration options for individual rules.

allow_library_clause
^^^^^^^^^^^^^^^^^^^^

When set to :code:`yes`, it allows consecutive library clauses.

**Violation**

.. code-block:: vhdl

   library ieee;
     use ieee.std_logic_1164.all;
   library top_dsn;
   library fifo_dsn;

**Fix**

.. code-block:: vhdl

   library ieee;
     use ieee.std_logic_1164.all;

   library top_dsn;
   library fifo_dsn;

library_004
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **library** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   Library ieee;

   LIBRARY fifo_dsn;

**Fix**

.. code-block:: vhdl

   library ieee;

   library fifo_dsn;

library_005
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **use** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   library ieee;
     USE ieee.std_logic_1164.all;
     Use ieee.std_logic_unsigned.all;

**Fix**

.. code-block:: vhdl

   library ieee;
     use ieee.std_logic_1164.all;
     use ieee.std_logic_unsigned.all;

library_006
###########

|phase_2| |error| |whitespace|

This rule checks for excessive spaces after the **use** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   library ieee;
     use    ieee.std_logic_1164.all;
     use   ieee.std_logic_unsigned.all;

**Fix**

.. code-block:: vhdl

   library ieee;
     use ieee.std_logic_1164.all;
     use ieee.std_logic_unsigned.all;

library_007
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **use** declaration.

|configuring_previous_line_rules_link|

The default style is :code:`no_blank_line`.

**Violation**

.. code-block:: vhdl

   library ieee;

     use ieee.std_logic_1164.all;

     use ieee.std_logic_unsigned.all;

**Fix**

.. code-block:: vhdl

   library ieee;
     use ieee.std_logic_1164.all;
     use ieee.std_logic_unsigned.all;

library_008
###########

|phase_4| |error| |indent|

This rule checks the indent of the **use** keyword.

|configuring_use_clause_indenting_link|

**Violation**

.. code-block:: vhdl

   library ieee;
   use ieee.std_logic_1164.all;
        use ieee.std_logic_unsigned.all;

**Fix**

.. code-block:: vhdl

   library ieee;
     use ieee.std_logic_1164.all;
     use ieee.std_logic_unsigned.all;

library_009
###########

|phase_4| |error| |alignment|

This rule checks alignment of comments above library use statements.

**Violation**

.. code-block:: vhdl

    library ieee;
    -- Use standard logic library
      use ieee.std_logic_1164.all;

**Fix**

.. code-block:: vhdl

    library ieee;
      -- Use standard logic library
      use ieee.std_logic_1164.all;

library_010
###########

|phase_1| |error| |structure|

This rule checks the **library** keyword is on its own line.

**Violation**

.. code-block:: vhdl

   context c1 is library ieee; use ieee.std_logic_1164.all; end context c1;

**Fix**

.. code-block:: vhdl

   context c1 is
     library ieee; use ieee.std_logic_1164.all; end context c1;

library_011
###########

|phase_1| |error| |structure|

This rule checks the **use** keyword is on its own line.

**Violation**

.. code-block:: vhdl

   context c1 is library ieee; use ieee.std_logic_1164.all; end context c1;

**Fix**

.. code-block:: vhdl

   context c1 is library ieee;
       use ieee.std_logic_1164.all; end context c1;

library_012
###########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for libraries that have been restricted by the user.

.. NOTE:: This rule is disabled by default.

**Violation**

.. code-block:: vhdl

   library bad_lib;

library_500
###########

|phase_6| |error| |case| |case_name|

This rule checks the logical_name in a library_clause has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   library IEEE;

   library FIFO_dsn;

**Fix**

.. code-block:: vhdl

   library ieee;

   library fifo_dsn;

library_600
###########

This rule has been moved to library_500.
