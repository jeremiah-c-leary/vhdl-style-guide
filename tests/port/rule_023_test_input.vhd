
entity FIFO is
  port (
    I_WR_EN : in   std_logic;
    I_DATA  : out  std_logic_vector(31 downto 0);
    I_RD_EN : in   std_logic;
    O_DATA  : out  std_logic_vector(31 downto 0);
    V_DATA  : view some_view
  );
end entity FIFO;


entity FIFO is
  port (
    I_WR_EN : std_logic;
    I_DATA  : std_logic_vector(31 downto 0);
    I_RD_EN : std_logic;
    O_DATA  : std_logic_vector(31 downto 0);
    V_DATA  : some_view
  );
end entity FIFO;
