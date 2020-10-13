
entity FIFO is
  port (
    I_WR_EN : in  std_logic;
    I_DATA  : out std_logic_vector(31 downto 0);
    I_RD_EN : in  std_logic;
    O_DATA  : out std_logic_vector(31 downto 0)
  );
end entity FIFO;


entity FIFO is
  port (
    I_WR_EN : IN  std_logic;
    I_DATA  : OUT std_logic_vector(31 downto 0);
    I_RD_EN : IN  std_logic;
    O_DATA  : OUT std_logic_vector(31 downto 0)
  );
end entity FIFO;
