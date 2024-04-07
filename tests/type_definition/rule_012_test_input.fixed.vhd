
architecture RTL of FIFO is

  type state_machine is record
    data : std_logic_vector(31 downto 0);
    chip_select : std_logic;
    wr_en : std_logic;
  end record;

  -- Violations below

  type state_machine is record
    data : std_logic_vector(31 downto 0);
    chip_select : std_logic;
    wr_en : std_logic;
  end record;

begin

end architecture RTL;
