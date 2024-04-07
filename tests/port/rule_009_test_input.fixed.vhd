
entity FIFO is
  port (
    I_WR_EN : inout std_logic;
    I_DATA  : out   std_logic_vector(31 downto 0);
    I_RD_EN : in    std_logic;
    O_DATA  : out   std_logic_vector(31 downto 0)
  );
end entity FIFO;


entity FIFO is
  port (
    I_WR_EN : inout std_logic;
    I_DATA  : in    std_logic_vector(31 downto 0);
    I_RD_EN : inout std_logic;
    O_DATA  : out   std_logic_vector(31 downto 0)
  );
end entity FIFO;
