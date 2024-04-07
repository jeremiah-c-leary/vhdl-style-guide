.. include:: includes.rst

Package Rules
-------------

package_001
###########

|phase_4| |error| |indent|

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

|phase_2| |error| |whitespace|

This rule checks for a single space between **package** and **is** keywords.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   package   FIFO_PKG   is

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

package_003
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **package** keyword.

|configuring_previous_line_rules_link|

The default style is :code:`no_code`.

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

|phase_6| |error| |case| |case_keyword|

This rule checks the package keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   PACKAGE FIFO_PKG is

**Fix**

.. code-block:: vhdl

   package FIFO_PKG is

package_005
###########

|phase_1| |error| |structure|

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

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END package fifo_pkg;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

package_007
###########

|phase_1| |error| |structure| |structure_optional|

This rule checks for the **package** keyword on the end package declaration.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   end FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package FIFO_PKG;

package_008
###########

|phase_6| |error| |case| |case_name|

This rule checks the package name has proper case on the end package declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end package FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

package_009
###########

|phase_2| |error| |whitespace|

This rule checks for a single space between the **end** and **package** keywords and package name.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   end   package   FIFO_PKG;

**Fix**

.. code-block:: vhdl

   end package FIFO_PKG;

package_010
###########

|phase_6| |error| |case| |case_name|

This rule checks the package name has proper case in the package declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   package FIFO_PKG is

**Fix**

.. code-block:: vhdl

   package fifo_pkg is

package_011
###########

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **package** keyword.

|configuring_blank_lines_link|

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

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **end package** keyword.

|configuring_blank_lines_link|

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

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   package fifo_pkg IS

**Fix**

.. code-block:: vhdl

   package fifo_pkg is

package_014
###########

|phase_1| |error| |structure| |structure_optional|

This rule checks the package name exists on the same line as the **end package** keywords.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   end package;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

package_015
###########

|phase_4| |error| |indent|

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

|phase_7| |disabled| |error| |naming|

This rule checks for valid suffixes on package identifiers.
The default package suffix is *_pkg*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   package foo is

**Fix**

.. code-block:: vhdl

   package foo_pkg is

package_017
###########

|phase_7| |disabled| |error| |naming|

This rule checks for valid prefixes on package identifiers.
The default package prefix is *pkg_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   package foo is

**Fix**

.. code-block:: vhdl

   package pkg_foo is

package_018
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **package** keyword in the **end package** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end PACKAGE fifo_pkg;

**Fix**

.. code-block:: vhdl

   end package fifo_pkg;

package_019
###########

|phase_5| |error| |alignment|

This rule checks the identifiers for all declarations are aligned in the package declarative region.

|configuring_identifier_alignment_rules_link|

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

package_400
###########

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the package declarative part.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   package my_package is

     signal   wr_en : std_logic;
     signal   rd_en   : std_logic;
     constant c_period : time;

   end package my_package;

**Fix**

.. code-block:: vhdl

   package my_package is

     signal   wr_en    : std_logic;
     signal   rd_en    : std_logic;
     constant c_period : time;

   end package my_package;

package_401
###########

|phase_5| |error| |alignment|

This rule checks the alignment of inline comments in the package declarative part.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   package my_package is

     signal   wr_en    : std_logic;  -- Comment 1
     signal   rd_en    : std_logic;     -- Comment 2
     constant c_period : time; -- Comment 3

   end package my_package;

**Fix**

.. code-block:: vhdl

   package my_package is

     signal   wr_en    : std_logic; -- Comment 1
     signal   rd_en    : std_logic; -- Comment 2
     constant c_period : time;      -- Comment 3

   end package my_package;

package_402
###########

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all attribute specifications.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

     attribute mark_debug of wr_en : signal is "true";
     attribute mark_debug of almost_empty : signal is "true";
     attribute mark_debug of full : signal is "true";

**Fix**

.. code-block:: vhdl

     attribute mark_debug of wr_en        : signal is "true";
     attribute mark_debug of almost_empty : signal is "true";
     attribute mark_debug of full         : signal is "true";
