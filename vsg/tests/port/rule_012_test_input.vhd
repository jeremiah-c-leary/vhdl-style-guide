
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
    I_WR_EN : in  std_logic := '0';
    I_DATA  : out std_logic_vector(31 downto 0):=(others=>'0');
    I_RD_EN : in  std_logic   := '1';
    O_DATA  : out std_logic_vector(31 downto 0):=(others => '1')
  );
end entity FIFO;

entity FIFO is
  port (
    I_WR_EN : in  std_logic := '0';-- COmment
    I_DATA  : out std_logic_vector(31 downto 0):=(others=>'0');  -- Comment
    I_RD_EN : in  std_logic   := '1'; -- Comment
    O_DATA  : out std_logic_vector(31 downto 0):=(others => '1') -- Comment
  );
end entity FIFO;
