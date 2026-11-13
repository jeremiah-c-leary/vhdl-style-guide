.. include:: includes.rst

Interface List Rules
--------------------

interface_list_001
##################

|phase_1| |error| |structure| |structure_optional|

This rule checks for the optional trailing semicolon at the end of interface lists.
VHDL-2019 allows a semicolon after the last element of generic, port and subprogram parameter lists.

The default action is "remove", which keeps code compatible with earlier VHDL standards.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   port (
     a : in    std_logic;
     b : out   std_logic;
   );

**Fix**

.. code-block:: vhdl

   port (
     a : in    std_logic;
     b : out   std_logic
   );
