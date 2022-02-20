
entity FIFO is
  port (
    I_WR_EN  : in  std_logic;
    I_DATA   : out std_logic_vector(31 downto 0);
    B_RD_EN  : buffer  std_logic;
    O_DATA   : out std_logic_vector(31 downto 0)
  );
end entity FIFO;


entity FIFO is
  port (
    WR_EN : in  std_logic;
    DATA  : out std_logic_vector(31 downto 0);
    RD_EN : buffer  std_logic;
    DATA  : out std_logic_vector(31 downto 0)
  );
end entity FIFO;
