Configuring Keyword Alignment Rules
-----------------------------------

There are several rules that enforce alignment for a group of lines based on the keywords such as 'after', '<=' etc.
Some of the configurations are available in all keyword alignment rules, while others are rule specific.

Common Keyword Alignment Configuration
######################################

Following configuration options can be independently changed for each of the keyword alignment rules.

#. :code:`compact_alignment` - if set to :code:`True` it enforces single space before alignment keyword in the line with the longest part before the keyword.
   Otherwise the alignment occurs to the keyword maximum column.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      signal sig_short   : std_logic;
      signal sig_very_long      : std_logic;

    **Fix (compact_alignment = True)**

    .. code-block:: vhdl

      signal sig_short     : std_logic;
      signal sig_very_long : std_logic;

    **Fix (compact_alignment = False)**

    .. code-block:: vhdl

      signal sig_short          : std_logic;
      signal sig_very_long      : std_logic;

#. :code:`blank_line_ends_group` - if set to :code:`True` any blank line encountered in the VHDL file ends the group of lines that should be aligned and starts new group.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      signal wr_en : std_logic;
      signal rd_en   : std_logic;

      constant c_short_period : time;
      constant c_long_period : time;

    **Fix (blank_line_ends_group = True)**

    .. code-block:: vhdl

      signal wr_en   : std_logic;
      signal rd_en   : std_logic;

      constant c_short_period : time;
      constant c_long_period  : time;

    **Fix (blank_line_ends_group = False)**

    .. code-block:: vhdl

      signal wr_en            : std_logic;
      signal rd_en            : std_logic;

      constant c_short_period : time;
      constant c_long_period  : time;

#. :code:`comment_line_ends_group` - if set to :code:`True` any purely comment line in the VHDL file ends the group of lines that should be aligned and starts new group.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      port (
          sclk_i : in std_logic;
          pclk_i : in std_logic;
          rst_i : in std_logic;
          ---- serial interface ----
          spi_ssel_o : out std_logic;
          spi_sck_o : out std_logic;
          spi_mosi_o : out std_logic;
          spi_miso_i : in std_logic
      );

    **Fix (comment_line_ends_group = True)**

    .. code-block:: vhdl

      port (
          sclk_i : in std_logic;
          pclk_i : in std_logic;
          rst_i  : in std_logic;
          ---- serial interface ----
          spi_ssel_o : out std_logic;
          spi_sck_o  : out std_logic;
          spi_mosi_o : out std_logic;
          spi_miso_i : in std_logic
      );


    **Fix (comment_line_ends_group = False)**

    .. code-block:: vhdl

      port (
          sclk_i     : in std_logic;
          pclk_i     : in std_logic;
          rst_i      : in std_logic;
          ---- serial interface ----
          spi_ssel_o : out std_logic;
          spi_sck_o  : out std_logic;
          spi_mosi_o : out std_logic;
          spi_miso_i : in std_logic
      );

.. NOTE:: As all keyword alignment rules have above configurations they are not mentioned in the documentation for each rule.

Rule Specific Keyword Alignment Configuration
#############################################

#. :code:`separate_generic_port_alignment` - if set to :code:`True` alignment within the generic declarative/mapping part is separated from alignment within the  port declarative/mapping part.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      generic (
          g_width : positive;
          g_output_delay : positive
      );
      port (
          clk_i : in std_logic;
          data_i : in std_logic;
          data_o : in std_logic
      );

    **Fix (separate_generic_port_alignment = True)**

    .. code-block:: vhdl

      generic (
          g_width        : positive;
          g_output_delay : positive
      );
      port (
          clk_i  : in std_logic;
          data_i : in std_logic;
          data_o : in std_logic
      );

    **Fix (separate_generic_port_alignment = False)**

    .. code-block:: vhdl

      generic (
          g_width        : positive;
          g_output_delay : positive
      );
      port (
          clk_i          : in std_logic;
          data_i         : in std_logic;
          data_o         : in std_logic
      );

#. :code:`if_control_statements_end_group` - if set to :code:`True` any line with if control statement ends the group of lines that should be aligned and starts new group.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid <= '1';
          data <= '1';
      else
          data_valid <= '0';
          hold_transmission <= '1';
      end if;

    **Fix (if_control_statements_end_group = True)**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid <= '1';
          data       <= '1';
      else
          data_valid        <= '0';
          hold_transmission <= '1';
      end if;

    **Fix (if_control_statements_end_group = False)**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid        <= '1';
          data              <= '1';
      else
          data_valid        <= '0';
          hold_transmission <= '1';
      end if;

#. :code:`case_control_statements_end_group` - if set to :code:`True` any line with case control statement ends the group of lines that should be aligned and starts new group.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      case A is
          when A =>
              X <= F;
              XY <= G;
              XYZ <= H;
          when B =>
              a <= I;
              ab <= h;
              c <= a;
          when others =>
            null;
      end case

    **Fix (case_control_statements_end_group = True)**

    .. code-block:: vhdl

      case A is
          when A =>
              X   <= F;
              XY  <= G;
              XYZ <= H;
          when B =>
              a  <= I;
              ab <= h;
              c  <= a;
          when others =>
              null;
      end case

    **Fix (case_control_statements_end_group = False)**

    .. code-block:: vhdl

      case A is
          when A =>
              X   <= F;
              XY  <= G;
              XYZ <= H;
          when B =>
              a   <= I;
              ab  <= h;
              c   <= a;
          when others =>
              null;
      end case

.. NOTE:: If given keyword alignment rule has any of the above keyword alignment specific configuration, then it is explicitly noted in the documentation of this rule.

The default value for each of these case rules can be overridden using a configuration.

Rules Enforcing Keyword Alignment
#################################

* `after_002 <after_rules.html#after-002>`_
* `architecture_026 <architecture_rules.html#architecture-026>`_
* `architecture_027 <architecture_rules.html#architecture-027>`_
* `block_401 <block_rules.html#block-401>`_
* `component_017 <component_rules.html#component-017>`_
* `component_020 <component_rules.html#component-020>`_
* `concurrent_006 <concurrent_rules.html#concurrent-006>`_
* `concurrent_008 <concurrent_rules.html#concurrent-008>`_
* `context_028 <context_rules.html#context-028>`_
* `entity_017 <entity_rules.html#entity-017>`_
* `entity_018 <entity_rules.html#entity-018>`_
* `entity_020 <entity_rules.html#entity-020>`_
* `function_012 <function_rules.html#function-012>`_
* `generate_401 <generate_rules.html#generate-401>`_
* `generate_403 <generate_rules.html#generate-403>`_
* `generate_405 <generate_rules.html#generate-405>`_
* `instantiation_010 <instantiation_rules.html#instantiation-010>`_
* `instantiation_029 <instantiation_rules.html#instantiation-029>`_
* `procedure_401 <procedure_rules.html#procedure-401>`_
* `process_033 <process_rules.html#process-033>`_
* `process_034 <process_rules.html#process-034>`_
* `process_035 <process_rules.html#process-035>`_
* `sequential_005 <sequential_rules.html#sequential-005>`_
* `type_400 <type_rules.html#type-400>`_
* `variable_assignment_005 <variable_assignment_rules.html#variable_assignment-005>`_
