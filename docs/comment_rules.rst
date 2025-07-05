.. include:: includes.rst

Comment Rules
-------------

comment_004
###########

|phase_2| |error| |whitespace|

This rule checks for at least a single space before inline comments.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '1';--Write data
   rd_en <= '1';   -- Read data

**Fix**

.. code-block:: vhdl

   wr_en <= '1'; --Write data
   rd_en <= '1';   -- Read data

comment_010
###########

|phase_4| |error| |indent|

This rule checks the indent lines starting with comments.

|configuring_comment_indenting_link|

**Violation**

.. code-block:: vhdl

       -- Libraries
   library ieee;

    -- Define architecture
   architecture rtl of fifo is

   -- Define signals
     signal wr_en : std_logic;
     signal rd_en : std_Logic;

   begin

**Fix**

.. code-block:: vhdl

   -- Libraries
   library ieee;

   -- Define architecture
   architecture rtl of fifo is

     -- Define signals
     signal wr_en : std_logic;
     signal rd_en : std_Logic;

   begin

comment_011
###########

|phase_1| |disabled| |error| |structure|

This rule checks for in-line comments and moves them to the line above.
The indent of the comment will be set to the indent of the current line.

.. NOTE:: This rule is disabled by default.

**Violation**

.. code-block:: vhdl

   a <= b; -- Assign signal

**Fix**

.. code-block:: vhdl

   -- Assign signal
   a <= b;

comment_012
###########

|phase_1| |disabled| |warning| |unfixable| |structure|

This rule checks for user defined keywords in comments.

.. NOTE:: This rule is disabled by default.

|configuring_comment_keywords_link|

**Violation**

.. code-block:: vhdl

   -- TODO:  Refactor the section below
   -- FIXME: Update

**Fix**

This is a reporting only rule.

comment_100
###########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **--**.

|configuring_whitespace_after_comment_rules_link|

**Violation**

.. code-block:: vhdl

   --Comment 1
   --|Comment 2
   ---Comment
   ---------------------------

**Fix**

.. code-block:: vhdl

   -- Comment 1
   --|Comment 2
   ---Comment
   ---------------------------
