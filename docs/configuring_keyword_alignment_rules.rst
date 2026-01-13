.. _configuring-keyword-alignment-rules:

Configuring Keyword Alignment Rules
-----------------------------------

There are several rules that enforce alignment for a group of lines based on the keywords such as 'after', '<=' etc.
Some of the configurations are available in all keyword alignment rules, while others are rule specific.

There are several options to these rules:

.. NOTE:: Some options are rule dependent.

.. |compact_alignment| replace::
   :code:`compact_alignment`

.. |compact_alignment__yes| replace::
   :code:`yes` = Align to left most column.

.. |compact_alignment__no| replace::
   :code:`no` = Align to right most column.

.. |blank_line_ends_group| replace::
   :code:`blank_line_ends_group`

.. |blank_line_ends_group__yes| replace::
   :code:`yes` = stop if a blank line is encountered.

.. |blank_line_ends_group__no| replace::
   :code:`no` = continue if a blank line is encountered.

.. |comment_line_ends_group| replace::
   :code:`comment_line_ends_group`

.. |comment_line_ends_group__yes| replace::
   :code:`yes` = stop if a blank line is encountered.

.. |comment_line_ends_group__no| replace::
   :code:`no` = continue if a blank line is encountered.

.. |separate_generic_port_alignment| replace::
   :code:`separate_generic_port_alignment`

.. |separate_generic_port_alignment__yes| replace::
   :code:`yes` = stop if **port** keyword detected.

.. |separate_generic_port_alignment__no| replace::
   :code:`no` = continue if **port** keyword detected.

.. |if_control_statements_ends_group| replace::
   :code:`if_control_statements_ends_group`

.. |if_control_statements_ends_group__yes| replace::
   :code:`yes` = stop when an if structure keyword is encountered.

.. |if_control_statements_ends_group__no| replace::
   :code:`no` = continue when an if structure keyword is encountered.

.. |case_control_statements_ends_group| replace::
   :code:`case_control_statements_ends_group`

.. |case_control_statements_ends_group__yes| replace::
   :code:`yes` = stop when a case control keyword is encountered.

.. |case_control_statements_ends_group__no| replace::
   :code:`no` = continue when a case control keyword is encountered.

.. |case_control_statements_ends_group__bocoec| replace::
   :code:`break_on_case_or_end_case` = Stop alignment if :code:`case` or :code:`end case` is encountered.

.. |generate_statements_ends_group| replace::
   :code:`generate_statements_ends_group`

.. |generate_statements_ends_group__yes| replace::
   :code:`yes` = stop when a generate statement keyword is encountered.

.. |generate_statements_ends_group__no| replace::
   :code:`no` = continue when a generate statement keyword is encountered.

.. |loop_control_statements_ends_group| replace::
   :code:`loop_control_generic_port_alignment`

.. |loop_control_statements_ends_group__yes| replace::
   :code:`yes` = stop when a loop control statement keyword is encountered.

.. |loop_control_statements_ends_group__no| replace::
   :code:`no` = continue when a loop control statement keyword is encountered.

.. |aggregate_parens_ends_group| replace::
   :code:`aggregate_parens_ends_group`

.. |aggregate_parens_ends_group__yes| replace::
   :code:`yes` = stop when an aggregate parenthesis is encountered.

.. |aggregate_parens_ends_group__no| replace::
   :code:`no` = continue when an aggregate parenthesis is encountered.

.. |ignore_single_line_aggregates| replace::
   :code:`ignore_single_line_aggregates`

.. |ignore_single_line_aggregates__yes| replace::
   :code:`yes` = ignore aggregates which are on a single line.

.. |ignore_single_line_aggregates__no| replace::
   :code:`no` = include aggregates which are on a single line.

.. |include_type_is_keyword| replace::
   :code:`include_type_is_keyword`

.. |include_type_is_keyword__yes| replace::
   :code:`yes` = align type is keyword with colons.

.. |include_type_is_keyword__no| replace::
   :code:`no` = ignore type is keywords for alignment.

.. |align_to| replace::
   :code:`align_to`

.. |align_to__keyword| replace::
   :code:`keyword` = align to the keyword specified in rule

.. |align_to__current_indent| replace::
   :code:`current_indent` = align to the current indent level

.. |yes| replace::
   :code:`yes`

.. |no| replace::
   :code:`no`

.. |break_on_case_or_end_case| replace::
   :code:`break_on_case_or_end_case`

.. |values_ca| replace::
   :code:`yes`, :code:`no`

.. |values_bleg| replace::
   :code:`yes`, :code:`no`

.. |values_cleg| replace::
   :code:`yes`, :code:`no`

.. |values_sgpa| replace::
   :code:`yes`, :code:`no`

.. |values_icseg| replace::
   :code:`yes`, :code:`no`

.. |values_ccseg| replace::
   :code:`yes`, :code:`no`, :code:`break_on_case_or_end_case`

.. |values_gseg| replace::
   :code:`yes`, :code:`no`

.. |values_lcseg| replace::
   :code:`yes`, :code:`no`

.. |values_apeg| replace::
   :code:`yes`, :code:`no`

.. |values_isla| replace::
   :code:`yes`, :code:`no`

.. |values_itik| replace::
   :code:`yes`, :code:`no`

.. |values_at| replace::
   :code:`keyword`, :code:`current_indent`

.. |def_at| replace::
   :code:`keyword`

+--------------------------------------+----------------+----------+------------------------------------------------+
| Option                               |   Values       | Default  | Description                                    |
+======================================+================+==========+================================================+
| |compact_alignment|                  | |values_ca|    | |yes|    | * |compact_alignment__yes|                     |
|                                      |                |          | * |compact_alignment__no|                      |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |blank_line_ends_group|              | |values_bleg|  | |yes|    | * |blank_line_ends_group__yes|                 |
|                                      |                |          | * |blank_line_ends_group__no|                  |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |comment_line_ends_group|            | |values_cleg|  | |yes|    | * |comment_line_ends_group__yes|               |
|                                      |                |          | * |comment_line_ends_group__no|                |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |separate_generic_port_alignment|    | |values_sgpa|  | |yes|    | * |separate_generic_port_alignment__yes|       |
|                                      |                |          | * |separate_generic_port_alignment__no|        |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |if_control_statements_ends_group|   | |values_icseg| | |yes|    | * |if_control_statements_ends_group__yes|      |
|                                      |                |          | * |if_control_statements_ends_group__no|       |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |case_control_statements_ends_group| | |values_ccseg| | |yes|    | * |case_control_statements_ends_group__yes|    |
|                                      |                |          | * |case_control_statements_ends_group__no|     |
|                                      |                |          | * |case_control_statements_ends_group__bocoec| |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |generate_statements_ends_group|     | |values_gseg|  | |yes|    | * |generate_statements_ends_group__yes|        |
|                                      |                |          | * |generate_statements_ends_group__no|         |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |loop_control_statements_ends_group| | |values_lcseg| | |yes|    | * |loop_control_statements_ends_group__yes|    |
|                                      |                |          | * |loop_control_statements_ends_group__no|     |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |include_type_is_keyword|            | |values_itik|  | |no|     | * |include_type_is_keyword__yes|               |
|                                      |                |          | * |include_type_is_keyword__no|                |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |aggregate_parens_ends_group|        | |values_apeg|  | |no|     | * |aggregate_parens_ends_group__yes|           |
|                                      |                |          | * |aggregate_parens_ends_group__no|            |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |ignore_single_line_aggregates|      | |values_isla|  | |no|     | * |ignore_single_line_aggregates__yes|         |
|                                      |                |          | * |ignore_single_line_aggregates__no|          |
+--------------------------------------+----------------+----------+------------------------------------------------+
| |align_to|                           | |values_at|    | |def_at| | * |align_to__keyword|                          |
|                                      |                |          | * |align_to__current_indent|                   |
+--------------------------------------+----------------+----------+------------------------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     process_031:
        compact_alignment: 'yes'
        blank_line_ends_group: 'yes'
        comment_line_ends_group : 'yes'
        separate_generic_port_alignment: 'yes'
        if_control_statements_ends_group: 'yes'
        case_control_statements_ends_group: 'yes'
        generate_statements_ends_group: 'yes'
        loop_control_statements_ends_group: 'yes'
        aggregate_parens_ends_group: 'yes'
        ignore_single_line_aggregates: 'yes'
        include_type_is_keyword: 'no'


Example: |compact_alignment| set to |yes|
#########################################

Enforces single space before alignment keyword in the line with the longest part before the keyword.

    **Violation**

    .. code-block:: vhdl

      signal sig_short   : std_logic;
      signal sig_very_long      : std_logic;

    **Fix**

    .. code-block:: vhdl

      signal sig_short     : std_logic;
      signal sig_very_long : std_logic;

Example: |compact_alignment| set to |no|
########################################

Aligns to right most instance of keyword.

    **Violation**

    .. code-block:: vhdl

      signal sig_short   : std_logic;
      signal sig_very_long      : std_logic;

    **Fix**

    .. code-block:: vhdl

      signal sig_short          : std_logic;
      signal sig_very_long      : std_logic;

Example: |blank_line_ends_group| set to |yes|
#############################################

Any blank line encountered in the VHDL file ends the group of lines that should be aligned and starts new group.

    **Violation**

    .. code-block:: vhdl

      signal wr_en : std_logic;
      signal rd_en   : std_logic;

      constant c_short_period : time;
      constant c_long_period : time;

    **Fix**

    .. code-block:: vhdl

      signal wr_en   : std_logic;
      signal rd_en   : std_logic;

      constant c_short_period : time;
      constant c_long_period  : time;

Example: |blank_line_ends_group| set to |no|
############################################

Any blank line encountered in the VHDL file will not end the group of lines that should be aligned.

    **Violation**

    .. code-block:: vhdl

      signal wr_en : std_logic;
      signal rd_en   : std_logic;

      constant c_short_period : time;
      constant c_long_period : time;

    **Fix**

    .. code-block:: vhdl

      signal wr_en            : std_logic;
      signal rd_en            : std_logic;

      constant c_short_period : time;
      constant c_long_period  : time;

Example: |comment_line_ends_group| set to |yes|
###############################################

Any comment line in the VHDL file ends the group of lines that should be aligned and starts new group.

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

    **Fix**

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

Example: |comment_line_ends_group| set to |no|
##############################################

Any comment line in the VHDL file will not end the group of lines that should be aligned and starts new group.

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

    **Fix**

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

Example: |separate_generic_port_alignment| set to |yes|
#######################################################

Alignment within the generic declarative/mapping part is separated from alignment within the port declarative/mapping part.

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

    **Fix**

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

Example: |separate_generic_port_alignment| set to |no|
######################################################

Alignment within the generic declarative/mapping part is the same as the alignment within the port declarative/mapping part.

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

    **Fix**

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

Example: |if_control_statements_ends_group| set to |yes|
########################################################

Any line with if control statement ends the group of lines that should be aligned and starts new group.

    **Violation**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid <= '1';
          data <= '1';
      else
          data_valid <= '0';
          hold_transmission <= '1';
      end if;

    **Fix**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid <= '1';
          data       <= '1';
      else
          data_valid        <= '0';
          hold_transmission <= '1';
      end if;

Example: |if_control_statements_ends_group| set to |no|
#######################################################

Any line with if control statement does not end the group of lines that should be aligned and starts new group.

    **Violation**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid <= '1';
          data <= '1';
      else
          data_valid <= '0';
          hold_transmission <= '1';
      end if;

    **Fix**

    .. code-block:: vhdl

      if condition = '1' then
          data_valid        <= '1';
          data              <= '1';
      else
          data_valid        <= '0';
          hold_transmission <= '1';
      end if;

Example: |case_control_statements_ends_group| set to |yes|
##########################################################

Any line with case control statements (:code:`case`, :code:`when` or :code:`end case`) ends the group of lines that should be aligned and starts new group.

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

    **Fix**

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

Example: |case_control_statements_ends_group| set to |no|
#########################################################

No line with case control statements ends the group of lines that should be aligned and starts a group.

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

    **Fix**

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

Example: |case_control_statements_ends_group| set to |break_on_case_or_end_case|
################################################################################

Any line with :code:`case` or :code:`end case` ends the group of lines that should be aligned and starts new group.

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

    **Fix**

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

Example: |generate_statements_ends_group| set to |yes|
######################################################

Any line with generate statement keywords ends the group of lines that should be aligned and starts new group.

    **Violation**

    .. code-block:: vhdl

      data_valid_before    <= '1';
      generate_label : if G_ENABLE = '1' generate
          data_valid <= '0';
          hold_transmission <= '1';
      end generate;
      data_valid_after       <= '1';

    **Fix**

    .. code-block:: vhdl

      data_valid_before <= '1';
      generate_label : if G_ENABLE = '1' generate
          data_valid        <= '0';
          hold_transmission <= '1';
      end generate;
      data_valid_after <= '1';

Example: |generate_statements_ends_group| set to |no|
#####################################################

No line with generate statement keywords ends the group of lines that should be aligned and starts new group.

    **Violation**

    .. code-block:: vhdl

      data_valid_before    <= '1';
      generate_label : if G_ENABLE = '1' generate
          data_valid <= '0';
          hold_transmission <= '1';
      end generate;
      data_valid_after       <= '1';

    **Fix**

    .. code-block:: vhdl

      data_valid_before     <= '1';
      generate_label : if G_ENABLE = '1' generate
          data_valid        <= '0';
          hold_transmission <= '1';
      end generate;
      data_valid_after      <= '1';

Example: |loop_control_statements_ends_group| set to |yes|
##########################################################

Any line with loop control statement (including for and while loops) ends the group of lines that should be aligned and starts new group.

    **Violation**

    .. code-block:: vhdl

      data_valid_before    <= '1';
      for index in 4 to 23 loop
          data_valid <= '0';
          hold_transmission <= '1';
      end loop;
      data_valid_after       <= '1';

    **Fix**

    .. code-block:: vhdl

      data_valid_before <= '1';
      for index in 4 to 23 loop
          data_valid        <= '0';
          hold_transmission <= '1';
      end loop;
      data_valid_after <= '1';

Example: |loop_control_statements_ends_group| set to |no|
#########################################################

No line with loop control statement (including for and while loops) ends the group of lines that should be aligned and starts new group.

    **Violation**

    .. code-block:: vhdl

      data_valid_before    <= '1';
      for index in 4 to 23 loop
          data_valid <= '0';
          hold_transmission <= '1';
      end loop;
      data_valid_after       <= '1';

    **Fix**

    .. code-block:: vhdl

      data_valid_before     <= '1';
      for index in 4 to 23 loop
          data_valid        <= '0';
          hold_transmission <= '1';
      end loop;
      data_valid_after      <= '1';

Example: |include_type_is_keyword| set to |yes|
###############################################

Any blank line encountered in the VHDL file ends the group of lines that should be aligned and starts new group.

    **Violation**

    .. code-block:: vhdl

      signal wr_en : std_logic;
      signal rd_en   : std_logic;
      type sm is (idle, read, write);
      constant c_short_period : time;
      constant c_long_period : time;

    **Fix**

    .. code-block:: vhdl

      signal wr_en            : std_logic;
      signal rd_en            : std_logic;
      type sm                 is (idle, read, write);
      constant c_short_period : time;
      constant c_long_period  : time;


Example: |include_type_is_keyword| set to |no|
##############################################

Any blank line encountered in the VHDL file will not end the group of lines that should be aligned.

    **Violation**

    .. code-block:: vhdl

      signal wr_en : std_logic;
      signal rd_en   : std_logic;
      type sm is (idle, read, write);
      constant c_short_period : time;
      constant c_long_period : time;

    **Fix**

    .. code-block:: vhdl

      signal wr_en            : std_logic;
      signal rd_en            : std_logic;
      type sm is (idle, read, write);
      constant c_short_period : time;
      constant c_long_period  : time;

Example: |aggregate_parens_ends_group| set to |yes|
###################################################

Any aggregate parenthesis encountered in the VHDL file will end the group of lines that should be aligned.

    **Violation**

    .. code-block:: vhdl

      constant my_constant : my_type := (
        ENUM_1   => (
          A      => 1,
          B      => 2,
          C      => 3
        ),
        ENUM_234 => (
          AA     => 1,
          BB     => 2,
          CC     => 3
        )
      );

    **Fix**

    .. code-block:: vhdl

      constant my_constant : my_type := (
        ENUM_1 => (
          A => 1,
          B => 2,
          C => 3
        ),
        ENUM_234 => (
          AA => 1,
          BB => 2,
          CC => 3
        )
      );

Example: |aggregate_parens_ends_group| set to |no|
##################################################

Any aggregate parenthesis encountered in the VHDL file will not end the group of lines that should be aligned.

    **Violation**

    .. code-block:: vhdl

      constant my_constant : my_type := (
        ENUM_1 => (
          A => 1,
          B => 2,
          C => 3
        ),
        ENUM_234 => (
          AA => 1,
          BB => 2,
          CC => 3
        )
      );

    **Fix**

    .. code-block:: vhdl

      constant my_constant : my_type := (
        ENUM_1   => (
          A      => 1,
          B      => 2,
          C      => 3
        ),
        ENUM_234 => (
          AA     => 1,
          BB     => 2,
          CC     => 3
        )
      );

Example: |aggregate_parens_ends_group| set to |yes| and |ignore_single_line_aggregates| set to |yes|
####################################################################################################

Any aggregate which is fully contained on a single line, including parenthesis, will not be considered defining a group.
In the example below, the others aggregates are ignored which will allow the ENUM_1 assignment and ENUM_234 assignment to be aligned.

    **Violation**

    .. code-block:: vhdl

      constant my_constant : my_type := (
        ENUM_1 => (others => '0'),
        ENUM_234 => (others => '1')
      );

    **Fix**

    .. code-block:: vhdl

      constant my_constant : my_type := (
        ENUM_1   => (others => '0'),
        ENUM_234 => (others => '1')
      );

Example: |align_to| set to :code:`current_indent`
#################################################

For example in rule :code:`process_028` the close parenthesis will be aligned with the **process** keyword.

    **Violation**

    .. code-block:: vhdl

      process (rd_en, wr_en,
               wr_valid, rd_valid
              )

    **Fix**

    .. code-block:: vhdl

      process (rd_en, wr_en,
               wr_valid, rd_valid
      )

Example: |align_to| set to :code:`keyword`
##########################################

For example in rule :code:`process_028` the close parenthesis will be aligned with the open parenthesis.

    **Violation**

    .. code-block:: vhdl

      process (rd_en, wr_en,
               wr_valid, rd_valid
      )

    **Fix**

    .. code-block:: vhdl

      process (rd_en, wr_en,
               wr_valid, rd_valid
              )


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
* `constant_400 <constant_rules.html#constant-400>`_
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
* `procedure_call_401 <procedure_call_rules.html#procedure-call-401>`_
* `process_028 <process_rules.html#process-028>`_
* `process_031 <process_rules.html#process-031>`_
* `process_033 <process_rules.html#process-033>`_
* `process_034 <process_rules.html#process-034>`_
* `process_035 <process_rules.html#process-035>`_
* `process_400 <process_rules.html#process-400>`_
* `process_401 <process_rules.html#process-401>`_
* `protected_type_body_401 <protected_type_body_rules.html#protected-type-body-401>`_
* `protected_type_body_402 <protected_type_body_rules.html#protected-type-body-402>`_
* `sequential_400 <sequential_rules.html#sequential-400>`_
* `signal_401 <signal_rules.html#signal-401>`_
* `subprogram_body_400 <subprogram_body_rules.html#subprogram-body-400>`_
* `subprogram_body_401 <subprogram_body_rules.html#subprogram-body-401>`_
* `type_400 <type_rules.html#type-400>`_
* `variable_401 <variable_rules.html#variable-401>`_
