
entity FIFO is
  port (
    I_WR_EN  : in  std_logic;
    O_DATA   : out std_logic_vector(31 downto 0);
    IO_RD_EN : inout  std_logic;
    O_DATA   : out std_logic_vector(31 downto 0)
  );
end entity FIFO;


entity FIFO is
  port (
    WR_EN : in  std_logic;
    DATA  : out std_logic_vector(31 downto 0);
    RD_EN : inout  std_logic;
    DATA  : out std_logic_vector(31 downto 0)
  );
end entity FIFO;
