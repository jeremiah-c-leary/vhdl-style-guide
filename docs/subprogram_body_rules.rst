.. include:: icons.rst

Subprogram Body Rules
---------------------

subprogram_body_201
###################

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **is** keyword.

This rule allows the **begin** keyword to occupy the blank line:

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin

Refer to `Configuring Blank Lines <configuring_blank_lines.html>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
     constant width : integer := 32;
   begin

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

     constant width : integer := 32;
   begin

subprogram_body_202
###################

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **begin** keyword.

This rule allows the **is** keyword to occupy the blank line:

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin

Refer to `Configuring Blank Lines <configuring_blank_lines.html>`_ for options.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

     constant width : integer := 32;
   begin

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

     constant width : integer := 32;

   begin

subprogram_body_203
###################

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **begin** keyword.

Refer to `Configuring Blank Lines <configuring_blank_lines.html>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin
     a <= b;

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin

     a <= b;

subprogram_body_204
###################

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **end** keyword.

Refer to `Configuring Blank Lines <configuring_blank_lines.html>`_ for options.

**Violation**

.. code-block:: vhdl

   begin

     a <= b;
   end function overflow;

**Fix**

.. code-block:: vhdl

   begin

     a <= b;

   end function overflow;

subprogram_body_205
###################

|phase_3| |error| |blank_line|

This rule checks for a blank line below the end of the function declaration.

Refer to `Configuring Blank Lines <configuring_blank_lines.html>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   end;
   signal wr_en : std_logic;

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   end;

   signal wr_en : std_logic;

subprogram_body_400
###################

|phase_5| |error| |alignment|

This rule checks the alignment of the **<=** and **:=** operators over consecutive sequential assignments in subprogram bodies.

Following extra configurations are supported:

* :code:`if_control_statements_ends_group`,
* :code:`case_control_statements_ends_group`.
* :code:`case_keyword_statements_ends_group`.
* :code:`loop_control_statements_ends_group`,

Refer to `Configuring Keyword Alignment Rules <configuring_keyword_alignment_rules.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';
   rd_en   <= '0';
   v_variable := 10;

**Fix**

.. code-block:: vhdl

   wr_en      <= '1';
   rd_en      <= '0';
   v_variable := 10;

