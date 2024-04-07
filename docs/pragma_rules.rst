.. include:: includes.rst

Pragma Rules
------------

pragma_300
##########

|phase_4| |error| |indent|

This rule checks the indent of pragmas.

|configuring_pragmas_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

   -- synthesis translate_off
     signal wr_en : std_logic;
     signal rd_en : std_Logic;
   -- synthesis translate_on

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     -- synthesis translate_off
     signal wr_en : std_logic;
     signal rd_en : std_Logic;
     -- synthesis translate_on

   begin

pragma_400
##########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above opening pragmas.

|configuring_previous_line_rules_link|

|configuring_pragmas_link|

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

   end component;
   -- synthesis translate_on

**Fix**

.. code-block:: vhdl

   end component;

   -- synthesis translate_on

pragma_401
##########

|phase_3| |error| |blank_line|

This rule checks for a blank line below opening pragmas.

|configuring_blank_lines_link|

|configuring_pragmas_link|

The default style is :code:`no_blank_line`.

**Violation**

.. code-block:: vhdl

   -- synthesis translate_on

   signal rd_en : std_logic;


**Fix**

.. code-block:: vhdl

   -- synthesis translate_on
   signal rd_en : std_logic;

pragma_402
##########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above closing pragmas.

|configuring_previous_line_rules_link|

|configuring_pragmas_link|

The default style is :code:`no_blank_line`.

**Violation**

.. code-block:: vhdl

   end component;

   -- synthesis translate_off

**Fix**

.. code-block:: vhdl

   end component;
   -- synthesis translate_off

pragma_403
##########

|phase_3| |error| |blank_line|

This rule checks for a blank line below closing pragmas.

|configuring_blank_lines_link|

|configuring_pragmas_link|

The default style is :code:`require_blank_line`.

**Violation**

.. code-block:: vhdl

   -- synthesis translate_off
   signal rd_en : std_logic;


**Fix**

.. code-block:: vhdl

   -- synthesis translate_off

   signal rd_en : std_logic;
