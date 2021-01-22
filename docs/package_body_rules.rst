Package Body Rules
------------------

Structural Rules
################

package_body_001
^^^^^^^^^^^^^^^^

This rule checks the **is** keyword is on the same line as the **package** keyword.

**Violation**

.. code-block:: vhdl

   package body FIFO_PKG
   is

**Fix**

.. code-block:: vhdl

   package body FIFO_PKG is

package_body_002
^^^^^^^^^^^^^^^^

This rule checks for the optional **package body** keywords on the end package body declaration.

Refer to the section `Configuring Optional Items <configuring_optional_items.html>`_ for options.

**Violation**

.. code-block:: vhdl

   end FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package body FIFO_PKG;

package_body_003
^^^^^^^^^^^^^^^^

This rule checks the package name exists in the closing of the package body declaration.

Refer to the section `Configuring Optional Items <configuring_optional_items.html>`_ for options.

**Violation**

.. code-block:: vhdl

   end package body;

**Fix**

.. code-block:: vhdl

   end package body fifo_pkg;

Whitespacing Rules
##################

package_body_100
^^^^^^^^^^^^^^^^

This rule checks for a single space between **package**, **body** and **is** keywords.

**Violation**

.. code-block:: vhdl

   package    body  FIFO_PKG   is

**Fix**

.. code-block:: vhdl

   package body FIFO_PKG is

package_body_101
^^^^^^^^^^^^^^^^

This rule checks for a single space between the **end**, **package** and **body** keywords and package name.

**Violation**

.. code-block:: vhdl

   end   package   body    FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package  body   FIFO_PKG;

Vertical Spacing Rules
######################

package_body_200
^^^^^^^^^^^^^^^^

This rule checks for blank lines or comments above the **package** keyword.

Refer to `Configuring Previous Line Rules <configuring_previous_line_rules.html>`_ for options.

**Violation**

.. code-block:: vhdl

   library ieee;
   package body FIFO_PKG is

**Fix**

.. code-block:: vhdl

   library ieee;

   package body FIFO_PKG is

package_body_201
^^^^^^^^^^^^^^^^

This rule checks for a blank line below the **package** keyword.

Refer to the section `Configuring Blank Lines <configuring_blank_lines.html>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   package body FIFO_PKG is
     constant width : integer := 32;

**Fix**

.. code-block:: vhdl

   package body FIFO_PKG is

     constant width : integer := 32;

package_body_202
^^^^^^^^^^^^^^^^

This rule checks for blank lines or comments above the **end package** keyword.

Refer to `Configuring Previous Line Rules <configuring_previous_line_rules.html>`_ for options.

**Violation**

.. code-block:: vhdl

     constant depth : integer := 512;
   end package body FIFO_PKG;

**Fix**

.. code-block:: vhdl

     constant depth : integer := 512;

   end package body FIFO_PKG;

package_body_203
^^^^^^^^^^^^^^^^

This rule checks for a blank line below the **end package** keyword.

Refer to the section `Configuring Blank Lines <configuring_blank_lines.html>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   end package body FIFO_PKG;
   library ieee;

**Fix**

.. code-block:: vhdl

   end package body FIFO_PKG;

Indentation Rules
#################

package_body_300
^^^^^^^^^^^^^^^^

This rule checks the indent of the package body keyword.

**Violation**

.. code-block:: vhdl

   library ieee;

     package body FIFO_PKG is

**Fix**

.. code-block:: vhdl

   library ieee;

   package body FIFO_PKG is

package_body_301
^^^^^^^^^^^^^^^^

This rule checks the indent of the end package declaration.

**Violation**

.. code-block:: vhdl

   package body FIFO_PKG is

      end package body fifo_pkg;

**Fix**

.. code-block:: vhdl

   package body fifo_pkg is

   end package body fifo_pkg;

Alignment Rules
###############

package_body_400
^^^^^^^^^^^^^^^^

This rule checks the identifiers for all declarations are aligned in the package body declarative region.

Refer to the section `Configuring Identifier Alignment Rules <configuring_declaration_identifier_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   variable    var1 : natural;
   constant  c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   constant c_period : time;

Captialization Rules
####################

package_body_500
^^^^^^^^^^^^^^^^

This rule checks the **package** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   PACKAGE body FIFO_PKG is

**Fix**

.. code-block:: vhdl

   package body FIFO_PKG is

package_body_501
^^^^^^^^^^^^^^^^

This rule checks the **body** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   package BODY FIFO_PKG is

**Fix**

.. code-block:: vhdl

   package body FIFO_PKG is

package_body_502
^^^^^^^^^^^^^^^^

This rule checks the package name has proper case in the package declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   package body FIFO_PKG is

**Fix**

.. code-block:: vhdl

   package body fifo_pkg is

package_body_503
^^^^^^^^^^^^^^^^

This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   package fifo_pkg IS

**Fix**

.. code-block:: vhdl

   package fifo_pkg is

package_body_504
^^^^^^^^^^^^^^^^

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END package fifo_pkg;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

package_body_505
^^^^^^^^^^^^^^^^

This rule checks the **package** keyword in the **end package body** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end PACKAGE body fifo_pkg;

**Fix**

.. code-block:: vhdl

   end package body fifo_pkg;

package_body_506
^^^^^^^^^^^^^^^^

This rule checks the **body** keyword in the **end package body** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end package BODY fifo_pkg;

**Fix**

.. code-block:: vhdl

   end package body fifo_pkg;

package_body_507
^^^^^^^^^^^^^^^^

This rule checks the package name has proper case on the end package declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end package body FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

Naming Convention Rules
#######################

package_body_600
^^^^^^^^^^^^^^^^

This rule checks for valid suffixes on package body identifiers.
The default package suffix is *_pkg*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   package body foo is

**Fix**

.. code-block:: vhdl

   package body foo_pkg is

package_body_601
^^^^^^^^^^^^^^^^

This rule checks for valid prefixes on package body identifiers.
The default package prefix is *pkg_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   package body foo is

**Fix**

.. code-block:: vhdl

   package body pkg_foo is

