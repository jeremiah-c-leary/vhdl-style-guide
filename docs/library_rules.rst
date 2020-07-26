Library Rules
-------------

library_001
###########

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

This rule checks for excessive spaces after the **library** keyword.

**Violation**

.. code-block:: vhdl

   library    ieee;

**Fix**

.. code-block:: vhdl

   library ieee;

library_003
###########

This rule checks for a blank line above the **library** keyword.

**Violation**

.. code-block:: vhdl

   library ieee;
   library fifo_dsn;

**Fix**

.. code-block:: vhdl

   library ieee;

   library fifo_dsn;

library_004
###########

This rule checks the **library** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks the **use** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks for excessive spaces after the **use** keyword.

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

This rule removes blank lines above the **use** keyword.

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

This rule checks the indent of the **use** keyword.

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

