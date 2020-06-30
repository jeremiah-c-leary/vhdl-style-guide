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

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END package fifo_pkg;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

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

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end package FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

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

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   package FIFO_PKG is

**Fix**

.. code-block:: vhdl

   package fifo_pkg is

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

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   package fifo_pkg IS

**Fix**

.. code-block:: vhdl

   package fifo_pkg is

package_014
###########

This rule checks the package name exists on the same line as the **end package** keywords.

**Violation**

.. code-block:: vhdl

   end package;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

package_015
###########

This rule checks the indent of the end package declaration.

**Violation**

.. code-block:: vhdl

   package FIFO_PKG is
 
      end package fifo_pkg;

**Fix**

.. code-block:: vhdl

   package fifo_pkg is

   end package fifo_pkg;

package_016
###########

This rule checks for valid suffixes on package identifiers.
The default package suffix is *_pkg*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   package foo is

**Fix**

.. code-block:: vhdl

   package foo_pkg is


package_017
###########

This rule checks for valid prefixes on package identifiers.
The default package prefix is *pkg_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   package foo is

**Fix**

.. code-block:: vhdl

   package pkg_foo is

package_018
###########

This rule checks the **package** keyword in the **end package* has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end PACKAGE fifo_pkg;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

package_019
###########

This rule checks the identifiers for all declarations are aligned in the package declarative region.

Refer to the section `Configuring Identifier Alignment Rules <configuring_declaration_identifier_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   variable var1 : natural;
   signal sig1 : natural;
   constant c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   signal   sig1     : natural;
   constant c_period : time;
