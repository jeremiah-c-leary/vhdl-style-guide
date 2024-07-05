
entity FIFO is
  port (
    WR_EN_I  : in  std_logic;
    DATA_O   : out std_logic_vector(31 downto 0);
    RD_EN_L  : linkage  std_logic;
    DATA_O   : out std_logic_vector(31 downto 0)
  );
end entity FIFO;


entity FIFO is
  port (
    WR_EN : in  std_logic;
    DATA  : out std_logic_vector(31 downto 0);
    RD_EN : linkage  std_logic;
    DATA  : out std_logic_vector(31 downto 0)
  );
end entity FIFO;
