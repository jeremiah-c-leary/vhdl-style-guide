.. include:: includes.rst

Protected Type Body Rules
-------------------------

protected_type_body_400
#######################

|phase_5| |error| |alignment|

This rule checks the identifiers for all declarations are aligned in the protected type body declarative region.

|configuring_identifier_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   variable    var1 : natural;
   constant  c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   constant c_period : time;

protected_type_body_401
#######################

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the protected type body declarative part.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   type my_type protected body is

     signal   wr_en : std_logic;
     signal   rd_en   : std_logic;
     constant c_period : time;

   end protected body;

**Fix**

.. code-block:: vhdl

   type my_type protected body is

     signal   wr_en    : std_logic;
     signal   rd_en    : std_logic;
     constant c_period : time;

   end protected body;

protected_type_body_402
#######################

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

protected_type_body_500
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **protected** keyword in **protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type sharedcounter is PROTECTED body

**Fix**

.. code-block:: vhdl

   type sharedcounter is protected body

protected_type_body_501
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **body** keyword in **protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type sharedcounter is protected BODY

**Fix**

.. code-block:: vhdl

   type sharedcounter is protected body

protected_type_body_502
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword in **end protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END protected body sharedcounter;

**Fix**

.. code-block:: vhdl

   end protected body sharedcounter;

protected_type_body_503
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **protected** keyword in **end protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end PROTECTED body sharedcounter;

**Fix**

.. code-block:: vhdl

   end protected body sharedcounter;

protected_type_body_504
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **body** keyword in **end protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end protected BODY sharedcounter;

**Fix**

.. code-block:: vhdl

   end protected body sharedcounter;
