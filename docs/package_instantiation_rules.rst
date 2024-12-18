.. include:: includes.rst

Package Instantiation Rules
---------------------------

package_instantiation_001
#########################

|phase_1| |error| |structure|

This rule checks the new package identifier is on the same line as the **package** keyword.

**Violation**

.. code-block:: vhdl

   package
   my_pkg is new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_002
#########################

|phase_1| |error| |structure|

This rule checks the **is** keyword is on the same line as the new package identifier.

**Violation**

.. code-block:: vhdl

   package my_pkg
   is new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_003
#########################

|phase_1| |error| |structure|

This rule checks the **new** keyword is on the same line as the **is** keyword.

**Violation**

.. code-block:: vhdl

   package my_pkg is
   new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_004
#########################

|phase_1| |error| |structure|

This rule checks the uninstantiated package name is on the same line as the **new** keyword.

**Violation**

.. code-block:: vhdl

   package my_pkg is new
   my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_100
#########################

|phase_2| |error| |whitespace|

This rule checks for a single space between the **package** keyword and the new package identifier.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   package    my_pkg is new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_101
#########################

|phase_2| |error| |whitespace|

This rule checks for a single space between the new package identifier and the **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   package my_pkg    is new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_102
#########################

|phase_2| |error| |whitespace|

This rule checks for a single space between the **is** keyword and the **new** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   package my_pkg is    new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_103
#########################

|phase_2| |error| |whitespace|

This rule checks for a single space between **new** keyword and the uninstantiated package name.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   package my_pkg is new    my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_500
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the package keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   PACKAGE my_pkg is new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_501
#########################

|phase_6| |error| |case| |case_name|

This rule checks the instantiated package name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   package MY_PKG is new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_502
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   package my_pkg IS new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_503
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **new** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   package my_pkg is NEW my_generic_pkg

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_504
#########################

|phase_6| |error| |case| |case_name|

This rule checks the uninstantiated package name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   package my_pkg is new MY_GENERIC_PKG

**Fix**

.. code-block:: vhdl

   package my_pkg is new my_generic_pkg

package_instantiation_600
#########################

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on package identifiers.
The default package suffix is *_pkg*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   package foo is new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package foo_pkg is new my_generic_pkg

package_instantiation_601
#########################

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on instantiated package identifiers.
The default package prefix is *pkg_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   package foo is new my_generic_pkg

**Fix**

.. code-block:: vhdl

   package pkg_foo is new my_generic_pkg
