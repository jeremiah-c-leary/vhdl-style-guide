
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
    i_wr_en : in  std_logic;
    i_data  : out std_logic_vector(31 downto 0);
    i_rd_en : in  std_logic;
    o_data  : out std_logic_vector(31 downto 0)
  );
end entity FIFO;
