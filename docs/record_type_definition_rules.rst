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

