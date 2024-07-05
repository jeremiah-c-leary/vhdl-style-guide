
entity FIFO is
  port (
    I_WR_EN, I_RD_EN : in  std_logic; -- Some comment
    I_DATA : in std_logic_vector(15 downto 0);
    O_DATA : out std_logic_vector(15 downto 0);
    O_RD_FULL, O_WR_FULL, O_RD_ALMOST_FULL, O_WR_ALMOST_FULL : out std_logic  -- Some comment
  );
end entity FIFO;

entity FIFO is
  port (
    O_RD_FULL, O_WR_FULL : out std_logic_vector(15 downto 0);
    O_RD_FULL, O_WR_FULL : out std_logic_vector(15 downto 0));
end entity FIFO;
