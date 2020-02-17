Configuring Keyword Alignment Rules
-----------------------------------

There are several rules that enforce alignment for a group of lines based on the keywords such as 'after', '<=' etc.
Some of the configurations are available in all keyword alignment rules, while others are rule specific.

Common Keyword Alignment Configuration
######################################

Following configuration options can be independently changed for each of the keyword alignment rules.

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

#. :code:`case_control_statements_end_group` - if set to :code:`True`
   By default set to :code:`True`.

.. NOTE:: If given keyword alignment rule has any of the above keyword alignment specific configuration, then it is explicitly noted in the documentation of this rule.

The default value for each of these case rules can be overridden using a configuration.
