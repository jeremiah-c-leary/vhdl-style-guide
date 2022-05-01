.. include:: includes.rst

Record Type Definition Rules
----------------------------

record_type_definition_001
##########################

|phase_1| |error| |structure|

This rule checks the location of the **record** keyword.

The default location is not on a line by itself.

|configuring_move_token_rules_link|

**Violation**

.. code-block:: vhdl

   type t_record is
   record

**Fix**

.. code-block:: vhdl

   type t_record is record

record_type_definition_002
##########################

|phase_1| |error| |structure|

This rule checks for code after the **record** keyword.

**Violation**

.. code-block:: vhdl

   type t_record is record a : std_logic;
     b : std_logic;
   end record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record;

record_type_definition_003
##########################

|phase_1| |error| |structure|

This rule checks the **end** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic; end record;


**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record;

record_type_definition_004
##########################

|phase_1| |error| |structure|

This rule checks the **is** keyword is on the same line as the **block** keyword.

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end
   record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record
   ;

record_type_definition_005
##########################

|phase_1| |error| |structure| |structure_optional|

This rule checks for the optional simple name in the **end record** statement.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record;

record_type_definition_006
##########################

|phase_1| |error| |structure|

This rule checks the optional simple name is on the same line as the **record** keyword.

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record
   t_record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record
   ;

record_type_definition_007
##########################

|phase_1| |error| |structure|

This rule checks the semicolon is on the same line as the **record** keyword.

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record
   ;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record;

record_type_definition_100
##########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end         record t_record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record;

record_type_definition_101
##########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the simple name.

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record    t_record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record;

record_type_definition_200
##########################

|phase_3| |error| |blank_line|

This rule checks for blank lines below the **record** keyword.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   type t_record is record

     a : std_logic;
     b : std_logic;
   end record    t_record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record;

record_type_definition_201
##########################

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **end** keyword.

|configuring_previous_line_rules_link|

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;

   end record    t_record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record;

record_type_definition_300
##########################

|phase_4| |error| |indent|

This rule checks the indent of the **record** keyword if it is on it's own line.

**Violation**

.. code-block:: vhdl

   type t_record is
        record
     a : std_logic;
     b : std_logic;
   end record    t_record;

**Fix**

.. code-block:: vhdl

   type t_record is
   record
     a : std_logic;
     b : std_logic;
   end record t_record;

record_type_definition_301
##########################

|phase_4| |error| |indent|

This rule checks the indent of the **end** keyword.

**Violation**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
       end record t_record;

**Fix**

.. code-block:: vhdl

   type t_record is record
     a : std_logic;
     b : std_logic;
   end record t_record;

