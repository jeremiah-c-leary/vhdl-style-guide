
entity FIFO is
  generic (
    G_WIDTH : natural := 16
  );
  port (
    I_INPUT : in std_logic;
    O_OUTPUT : out std_logic;
    IO_INOUT : inout std_logic
  );
end entity;

architecture rtl of fifo is

  function func1 (
    i_input : std_logic;
    o_output : std_logic;
    io_inout : std_logic
  ) return integer is

    variable v_data : std_logic_vector(g_width - 1 downto 0);
    variable v_read : std_logic_vector(i_input'range);
    variable v_read : std_logic_vector(o_output'left downto 0);
    variable v_read : std_logic_vector(31 downto io_inout'right);

  begin

    a <= i_input;
    b <= o_output;
    c <= io_inout;

  end function;

  procedure proc1 (
    i_input : std_logic;
    o_output : std_logic;
    io_inout : std_logic
  ) is

    variable w_data : std_logic_vector(g_width - 1 downto 0);
    variable w_read : std_logic_vector(i_input'range);
    variable w_read : std_logic_vector(o_output'left downto 0);
    variable w_read : std_logic_vector(31 downto io_inout'right);

  begin

    a <= i_input;
    b <= o_output;
    c <= io_inout;

  end function;

  signal w_data : std_logic_vector(G_WIDTH - 1 downto 0);
  constant w_read : std_logic_vector(I_INPUT'range);
  shared variable w_read : std_logic_vector(O_OUTPUT'left downto 0);
  signal w_read : std_logic_vector(31 downto IO_INOUT'right);

begin

  output <= large_data(g_width - 1 downto 0);

  process (I_INPUT, O_OUTPUT, IO_INOUT) is

    variable v_data : std_logic_vector(G_WIDTH - 1 downto 0);
    variable v_read : std_logic_vector(I_INPUT'range);
    variable v_read : std_logic_vector(O_OUTPUT'left downto 0);
    variable v_read : std_logic_vector(31 downto IO_INOUT'right);

  begin

    a <= I_INPUT;
    b <= O_OUTPUT;
    c <= IO_INOUT;

  end process;

  a <= I_INPUT;
  b <= O_OUTPUT;
  c <= IO_INOUT;

  U_RAM : RAM
    generic map (
      g_width => g_width
    )
    port map (
      i_input => I_INPUT,
      o_output => O_OUTPUT,
      io_inout => IO_INOUT
    );

  U_RAM : RAM
    generic map (
      g_width => g_width
    )
    port map (
      I_INPUT,
      O_OUTPUT,
      IO_INOUT
    );

end architecture rtl;

-- Violations Below

architecture rtl of fifo is

  function func1 (
    i_input : std_logic;
    o_output : std_logic;
    io_inout : std_logic
  ) return integer is

    variable v_data : std_logic_vector(g_width - 1 downto 0);
    variable v_read : std_logic_vector(i_input'range);
    variable v_read : std_logic_vector(o_output'left downto 0);
    variable v_read : std_logic_vector(31 downto io_inout'right);

  begin

    a <= i_input;
    b <= o_output;
    c <= io_inout;

  end function;

  procedure proc1 (
    i_input : std_logic;
    o_output : std_logic;
    io_inout : std_logic
  ) is

    variable w_data : std_logic_vector(g_width - 1 downto 0);
    variable w_read : std_logic_vector(i_input'range);
    variable w_read : std_logic_vector(o_output'left downto 0);
    variable w_read : std_logic_vector(31 downto io_inout'right);

  begin

    a <= i_input;
    b <= o_output;
    c <= io_inout;

  end function;

  signal w_data : std_logic_vector(g_width - 1 downto 0);
  signal w_read : std_logic_vector(I_INPUT'range);
  signal w_read : std_logic_vector(O_OUTPUT'left downto 0);
  signal w_read : std_logic_vector(31 downto IO_INOUT'right);

begin

  output <= large_data(g_width - 1 downto 0);

  process (I_INPUT, O_OUTPUT, IO_INOUT) is

    variable v_data : std_logic_vector(g_width - 1 downto 0);
    variable v_read : std_logic_vector(I_INPUT'range);
    variable v_read : std_logic_vector(O_OUTPUT'left downto 0);
    variable v_read : std_logic_vector(31 downto IO_INOUT'right);

  begin

    a <= I_INPUT;
    b <= O_OUTPUT;
    c <= IO_INOUT;

  end process;

  a <= I_INPUT;
  b <= O_OUTPUT;
  c <= IO_INOUT;

  U_RAM : RAM
    generic map (
      g_width => g_width
    )
    port map (
      i_input => I_INPUT,
      o_output => O_OUTPUT,
      io_inout => IO_INOUT
    );

  U_RAM : RAM
    generic map (
      g_width => g_width
    )
    port map (
      I_INPUT,
      O_OUTPUT,
      IO_INOUT
    );

end architecture rtl;

-- Change entities

entity NEW_FIFO is
  generic (
    g_width : natural := 16
  );
  port (
    i_input : in std_logic;
    o_output : out std_logic;
    io_inout : inout std_logic
  );
end entity;

architecture rtl of new_fifo is

  function func1 (
    I_INPUT : std_logic;
    O_OUTPUT : std_logic;
    IO_INOUT : std_logic
  ) return integer is

    variable v_data : std_logic_vector(G_WIDTH - 1 downto 0);
    variable v_read : std_logic_vector(I_INPUT'range);
    variable v_read : std_logic_vector(O_OUTPUT'left downto 0);
    variable v_read : std_logic_vector(31 downto IO_INOUT'right);

  begin

    a <= I_INPUT;
    b <= O_OUTPUT;
    c <= IO_INOUT;

  end function;

  procedure proc1 (
    I_INPUT : std_logic;
    O_OUTPUT : std_logic;
    IO_INOUT : std_logic
  ) is

    variable w_data : std_logic_vector(G_WIDTH - 1 downto 0);
    variable w_read : std_logic_vector(I_INPUT'range);
    variable w_read : std_logic_vector(O_OUTPUT'left downto 0);
    variable w_read : std_logic_vector(31 downto IO_INOUT'right);

  begin

    a <= I_INPUT;
    b <= O_OUTPUT;
    c <= IO_INOUT;

  end function;

  signal w_data : std_logic_vector(g_width - 1 downto 0);
  signal w_read : std_logic_vector(i_input'range);
  signal w_read : std_logic_vector(o_output'left downto 0);
  signal w_read : std_logic_vector(31 downto io_inout'right);

begin

  output <= large_data(g_width - 1 downto 0);

  process (i_input, o_output, io_inout) is

    variable v_data : std_logic_vector(g_width - 1 downto 0);
    variable v_read : std_logic_vector(i_input'range);
    variable v_read : std_logic_vector(o_output'left downto 0);
    variable v_read : std_logic_vector(31 downto io_inout'right);

  begin

    a <= i_input;
    b <= o_output;
    c <= io_inout;

  end process;

  a <= i_input;
  b <= o_output;
  c <= io_inout;

  U_RAM : RAM
    generic map (
      G_WIDTH => G_WIDTH
    )
    port map (
      I_INPUT => i_input,
      O_OUTPUT => o_output,
      IO_INOUT => io_inout
    );

  U_RAM : RAM
    generic map (
      G_WIDTH => G_WIDTH
    )
    port map (
      i_input,
      o_output,
      io_inout
    );

end architecture rtl;

-- Violations

architecture rtl of new_fifo is

  function func1 (
    I_INPUT : std_logic;
    O_OUTPUT : std_logic;
    IO_INOUT : std_logic
  ) return integer is

    variable v_data : std_logic_vector(G_WIDTH - 1 downto 0);
    variable v_read : std_logic_vector(I_INPUT'range);
    variable v_read : std_logic_vector(O_OUTPUT'left downto 0);
    variable v_read : std_logic_vector(31 downto IO_INOUT'right);

  begin

    a <= I_INPUT;
    b <= O_OUTPUT;
    c <= IO_INOUT;

  end function;

  procedure proc1 (
    I_INPUT : std_logic;
    O_OUTPUT : std_logic;
    IO_INOUT : std_logic
  ) is

    variable w_data : std_logic_vector(G_WIDTH - 1 downto 0);
    variable w_read : std_logic_vector(I_INPUT'range);
    variable w_read : std_logic_vector(O_OUTPUT'left downto 0);
    variable w_read : std_logic_vector(31 downto IO_INOUT'right);

  begin

    a <= I_INPUT;
    b <= O_OUTPUT;
    c <= IO_INOUT;

  end function;

  signal w_data : std_logic_vector(g_width - 1 downto 0);
  signal w_read : std_logic_vector(i_input'range);
  signal w_read : std_logic_vector(o_output'left downto 0);
  signal w_read : std_logic_vector(31 downto io_inout'right);

begin

  output <= large_data(G_WIDTH - 1 downto 0);

  process (i_input, o_output, io_inout) is

    variable v_data : std_logic_vector(G_WIDTH - 1 downto 0);
    variable v_read : std_logic_vector(i_input'range);
    variable v_read : std_logic_vector(o_output'left downto 0);
    variable v_read : std_logic_vector(31 downto io_inout'right);

  begin

    a <= i_input;
    b <= o_output;
    c <= io_inout;

  end process;

  a <= i_input;
  b <= o_output;
  c <= io_inout;

  U_RAM : RAM
    generic map (
      G_WIDTH => G_WIDTH
    )
    port map (
      I_INPUT => i_input,
      O_OUTPUT => o_output,
      IO_INOUT => io_inout
    );

  U_RAM : RAM
    generic map (
      G_WIDTH => G_WIDTH
    )
    port map (
      i_input,
      o_output,
      io_inout
    );

  with i_input select o_output <=
    '0' when '1',
    '1' when '0',
    'x' when others;

end architecture rtl;
