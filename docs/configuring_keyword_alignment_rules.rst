.. _configuring-keyword-alignment-rules:

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

#. :code:`if_control_statements_ends_group` - if set to :code:`True` any line with if control statement ends the group of lines that should be aligned and starts new group.
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

    **Fix (if_control_statements_ends_group = True)**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid <= '1';
          data       <= '1';
      else
          data_valid        <= '0';
          hold_transmission <= '1';
      end if;

    **Fix (if_control_statements_ends_group = False)**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid        <= '1';
          data              <= '1';
      else
          data_valid        <= '0';
          hold_transmission <= '1';
      end if;

#. :code:`case_control_statements_ends_group` - if set to :code:`True`, any line with case control statements (:code:`case`, :code:`when` or :code:`end case`) ends the group of lines that should be aligned and starts new group. If set to :code:`False`, no line with case control statements ends the group of lines that should be aligned and starts a group. If set to :code:`break_on_case_or_end_case`, any line with :code:`case` or :code:`end case` ends the group of lines that should be aligned and starts new group.
   By default set to :code:`True`.

    **Violation**

    .. code-block:: vhdl

      data_valid_before    <= '1';
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
      end case;
      data_valid_after       <= '1';

    **Fix (case_control_statements_ends_group = True)**

    .. code-block:: vhdl

      data_valid_before <= '1';
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
      end case;
      data_valid_after <= '1';

    **Fix (case_control_statements_ends_group = False)**

    .. code-block:: vhdl

      data_valid_before <= '1';
      case A is
          when A =>
              X         <= F;
              XY        <= G;
              XYZ       <= H;
          when B =>
              a         <= I;
              ab        <= h;
              c         <= a;
          when others =>
              null;
      end case;
      data_valid_after  <= '1';

    **Fix (case_control_statements_ends_group = break_on_case_or_end_case)**

    .. code-block:: vhdl

      data_valid_before <= '1';
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
      end case;
      data_valid_after <= '1';

#. :code:`generate_statements_ends_group` - if set to :code:`True` any line with generate statement keywords ends the group of lines that should be aligned and starts new group.
   By default set to :code:`False`.

    **Violation**

    .. code-block:: vhdl

      data_valid_before    <= '1';
      generate_label : if G_ENABLE = '1' generate
          data_valid <= '0';
          hold_transmission <= '1';
      end generate;
      data_valid_after       <= '1';

    **Fix (generate_statements_ends_group = True)**

    .. code-block:: vhdl

      data_valid_before <= '1';
      generate_label : if G_ENABLE = '1' generate
          data_valid        <= '0';
          hold_transmission <= '1';
      end generate;
      data_valid_after <= '1';

    **Fix (generate_statements_ends_group = False)**

    .. code-block:: vhdl

      data_valid_before     <= '1';
      generate_label : if G_ENABLE = '1' generate
          data_valid        <= '0';
          hold_transmission <= '1';
      end generate;
      data_valid_after      <= '1';

#. :code:`loop_control_statements_ends_group` - if set to :code:`True` any line with loop control statement (including for and while loops) ends the group of lines that should be aligned and starts new group.
   By default set to :code:`False`.

    **Violation**

    .. code-block:: vhdl

      data_valid_before    <= '1';
      for index in 4 to 23 loop
          data_valid <= '0';
          hold_transmission <= '1';
      end loop;
      data_valid_after       <= '1';

    **Fix (loop_control_statements_ends_group = True)**

    .. code-block:: vhdl

      data_valid_before <= '1';
      for index in 4 to 23 loop
          data_valid        <= '0';
          hold_transmission <= '1';
      end loop;
      data_valid_after <= '1';

    **Fix (loop_control_statements_ends_group = False)**

    .. code-block:: vhdl

      data_valid_before     <= '1';
      for index in 4 to 23 loop
          data_valid        <= '0';
          hold_transmission <= '1';
      end loop;
      data_valid_after      <= '1';

#. :code:`no_alignment` - if set to :code:`True` the keyword will be forced to the left.
   By default set to :code:`False`.

    **Violation**

    .. code-block:: vhdl

      signal wr_en : std_logic;
      signal rd_en   : std_logic;

      constant c_short_period : time;
      constant c_long_period : time;

    **Fix**

    .. code-block:: vhdl

      signal wr_en : std_logic;
      signal rd_en   : std_logic;

      constant c_short_period : time;
      constant c_long_period : time;


.. NOTE:: If given keyword alignment rule has any of the above keyword alignment specific configuration, then it is explicitly noted in the documentation of this rule.

The default value for each of these case rules can be overridden using a configuration.

Rules Enforcing Keyword Alignment
#################################

* `after_002 <after_rules.html#after-002>`_
* `architecture_026 <architecture_rules.html#architecture-026>`_
* `architecture_027 <architecture_rules.html#architecture-027>`_
* `architecture_400 <architecture_rules.html#architecture-400>`_
* `block_401 <block_rules.html#block-401>`_
* `block_402 <block_rules.html#block-402>`_
* `case_generate_statement_400 <case_generate_statement_rules.html#case-generate-statement-400>`_
* `component_017 <component_rules.html#component-017>`_
* `component_020 <component_rules.html#component-020>`_
* `concurrent_006 <concurrent_rules.html#concurrent-006>`_
* `concurrent_008 <concurrent_rules.html#concurrent-008>`_
* `concurrent_400 <concurrent_rules.html#concurrent-400>`_
* `declarative_part_400 <declarative_part_rules.html#declarative-part-400>`_
* `entity_017 <entity_rules.html#entity-017>`_
* `entity_018 <entity_rules.html#entity-018>`_
* `entity_020 <entity_rules.html#entity-020>`_
* `function_012 <function_rules.html#function-012>`_
* `generate_401 <generate_rules.html#generate-401>`_
* `generate_403 <generate_rules.html#generate-403>`_
* `generate_405 <generate_rules.html#generate-405>`_
* `instantiation_010 <instantiation_rules.html#instantiation-010>`_
* `instantiation_029 <instantiation_rules.html#instantiation-029>`_
* `package_400 <package_rules.html#package-400>`_
* `package_401 <package_rules.html#package-401>`_
* `package_402 <package_rules.html#package-402>`_
* `package_body_401 <package_body_rules.html#package-body-401>`_
* `package_body_402 <package_body_rules.html#package-body-402>`_
* `procedure_401 <procedure_rules.html#procedure-401>`_
* `procedure_410 <procedure_rules.html#procedure-410>`_
* `procedure_411 <procedure_rules.html#procedure-411>`_
* `procedure_412 <procedure_rules.html#procedure-412>`_
* `procedure_call_401 <procedure_call_rules.html#procedure-call-401>`_
* `process_031 <process_rules.html#process-031>`_
* `process_033 <process_rules.html#process-033>`_
* `process_034 <process_rules.html#process-034>`_
* `process_035 <process_rules.html#process-035>`_
* `process_400 <process_rules.html#process-400>`_
* `process_401 <process_rules.html#process-401>`_
* `sequential_400 <sequential_rules.html#sequential-400>`_
* `subprogram_body_400 <subprogram_body_rules.html#subprogram-body-400>`_
* `subprogram_body_401 <subprogram_body_rules.html#subprogram-body-401>`_
* `type_400 <type_rules.html#type-400>`_
