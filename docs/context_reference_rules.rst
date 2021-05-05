.. include:: icons.rst

Context Reference Rules
-----------------------

context_ref_001
###############

|phase_4| |error|

This rule checks the indent of the **context** keyword.

**Violation**

.. code-block:: vhdl

   library ieee;
   context c1;

**Fix**

.. code-block:: vhdl

   library ieee;
     context c1;


context_ref_002
###############

|phase_2| |error|

This rule checks for a single space between the **context** keyword and the context selected name.

**Violation**

.. code-block:: vhdl

   context   c1;

**Fix**

.. code-block:: vhdl

   context c1;


context_ref_003
###############

|phase_6| |error|

This rule checks the **context** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   CONTEXT c1;

**Fix**

.. code-block:: vhdl

   context c1;


context_ref_004
###############

|phase_6| |error|

This rule checks the context selected names have proper case in the context reference.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   context C1;

   context CON1, Con2;

**Fix**

.. code-block:: vhdl

   context c1;

   context con1, con2;


context_ref_005
###############

|phase_1| |error|

This rule checks the **context** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   context c1 is library ieee; context con1; end context c1;

   library ieee; context con2;

**Fix**

.. code-block:: vhdl

   context c1 is library ieee;
   context con1; end context c1;

   library ieee;
   context con2;


context_ref_006
###############

This rule checks the semicolon is on the same line as the context selected name.

.. NOTE:: This rule has not been implemented yet.

**Violation**

.. code-block:: vhdl

   context c1
   ;

   context
   c1
   ;

**Fix**

.. code-block:: vhdl

   context c1;

   context
   c1;

context_ref_007
###############

This rule checks for code after the semicolon.

.. NOTE:: This rule has not been implemented yet.

**Violation**

.. code-block:: vhdl

   context c1; -- Comments are allowed

   context c1; library ieee; -- This is not allowed

**Fix**

.. code-block:: vhdl

   context c1; -- Comments are allowed

   context c1;
     library ieee; -- This is not allowed


context_ref_008
###############

This rule checks the context selected name is on the same line as the **context** keyword.

.. NOTE:: This rule has not been implemented yet.

**Violation**

.. code-block:: vhdl

   context
   c1
   ;

**Fix**

.. code-block:: vhdl

   context c1

   ;


context_ref_009
###############

This rule checks for multiple selected names in a single reference.

.. NOTE:: This rule has not been implemented yet.

**Violation**

.. code-block:: vhdl

   context c1, c2, c3; -- Comment 1

   context c1,
           c2,
           c3;

.. code-block:: vhdl

   context c1;
   context c2;
   context c3;

   context c1;
   context c2;
   context c3;
