
entity FIFO is
  port (
    I_WR_EN : in  std_logic;
I_RD_EN : in  std_logic; -- Some comment
    I_DATA : in std_logic_vector(15 downto 0);
    O_DATA : out std_logic_vector(15 downto 0);
    O_RD_FULL : out std_logic;
O_WR_FULL : out std_logic;
O_RD_ALMOST_FULL : out std_logic;
O_WR_ALMOST_FULL : out std_logic  -- Some comment
  );
end entity FIFO;

