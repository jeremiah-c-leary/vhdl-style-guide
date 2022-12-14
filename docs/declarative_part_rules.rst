.. include:: includes.rst

Declarative Part Rules
----------------------

declarative_part_400
####################

|phase_5| |error| |alignment|

This rule checks the alignment of **:=** operator for signal, constant and variable declarations.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   signal clk : std_logic := '0';
   variable reset : std_logic := '1';
   shared variable enable : std_logic := '0';
   constant reset_value : integer := 32;

**Fix**

.. code-block:: vhdl

   signal clk : std_logic             := '0';
   variable reset : std_logic         := '1';
   shared variable enable : std_logic := '0';
   constant reset_value : integer     := 32;
