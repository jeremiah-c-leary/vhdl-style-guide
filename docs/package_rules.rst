Package Rules
-------------

package_001
###########

This rule checks the indent of the package declaration.

**Violation**

.. code-block:: vhdl

   library ieee;

     package FIFO_PKG is

**Fix**

.. code-block:: vhdl

   library ieee;

   package FIFO_PKG is

package_002
###########

This rule checks for a single space between **package** and **is** keywords.

**Violation**

.. code-block:: vhdl

   package   FIFO_PKG   is

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

package_003
###########

This rule checks for a blank line above the **package** keyword.

**Violation**

.. code-block:: vhdl

   library ieee;
   package FIFO_PKG is

**Fix**

.. code-block:: vhdl

   library ieee;

   package FIFO_PKG is

package_004
###########

This rule checks the package keyword has proper case.

.. NOTE::  The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   PACKAGE FIFO_PKG is

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

package_005
###########

This rule checks the **is** keyword is on the same line as the **package** keyword.

**Violation**

.. code-block:: vhdl

   package FIFO_PKG
   is

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

package_006
###########

This rule checks the **end package** keywords have proper case.

.. NOTE::  The default is lowercase.

**Violation**

.. code-block:: vhdl

   END PACKAGE FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package FIFO_PKG;

package_007
###########

This rule checks for the **package** keyword on the end package declaration.

**Violation**

.. code-block:: vhdl

   end FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package FIFO_PKG;

package_008
###########

This rule checks the package name has proper case on the end package declaration.

.. NOTE::  The default is uppercase.

**Violation**

.. code-block:: vhdl

   end package fifo_pkg;

**Fix**

.. code-block:: vhdl

   end package FIFO_PKG;

package_009
###########

This rule checks for a single space between the **end** and **package** keywords and package name.

**Violation**

.. code-block:: vhdl

   end   package   FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package FIFO_PKG;

package_010
###########

This rule checks the package name has proper case in the package declaration.

.. NOTE::  The default is uppercase.

**Violation**

.. code-block:: vhdl

   package fifo_pkg is

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

package_011
###########

This rule checks for a blank line below the **package** keyword.

**Violation**

.. code-block:: vhdl

   package FIFO_PKG is
     constant width : integer := 32;

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

     constant width : integer := 32;

package_012
###########

This rule checks for a blank line above the **end package** keyword.

**Violation**

.. code-block:: vhdl

     constant depth : integer := 512;
   end package FIFO_PKG;

**Fix**

.. code-block:: vhdl

     constant depth : integer := 512;

   end package FIFO_PKG;

package_013
###########

This rule checks the **is** keyword has proper case.

.. NOTE::  The default is lowercase.

**Violation**

.. code-block:: vhdl

   package FIFO_PKG IS

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

package_014
###########

This rule checks the package name exists on the same line as the **end package** keywords.

**Violation**

.. code-block:: vhdl

   end package; 

**Fix**

.. code-block:: vhdl

   end package FIFO_PKG;

package_015
###########

This rule checks the indent of the end package declaration.

**Violation**

.. code-block:: vhdl

   package FIFO_PKG is
 
      end package FIFO_PKG;

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

   end package FIFO_PKG;

