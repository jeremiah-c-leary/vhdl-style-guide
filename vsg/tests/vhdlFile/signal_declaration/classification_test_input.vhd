
architecture RTL of FIFO is

  signal fifo_wr : std_logic;

  signal fifo_wr : std_logic_vector(3 downto 0);

  signal fifo_wr : std_logic_vector(3 downto 0) := "000";

  signal fifo_wr, fifo_rd, fifo_empty : std_logic := '1';

  signal fifo_rd : fifo_wr'subtype;

begin

end architecture RTL;
