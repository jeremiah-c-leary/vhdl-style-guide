
architecture RTL of FIFO is

  subtype counter is unsigned(4 downto 0);

  -- Violations below

  subtype counter is
  unsigned(4 downto 0);

  subtype counter is


  unsigned(4 downto 0);

  -- Honor comments

  subtype counter is
  -- some comment
  unsigned(4 downto 0);

  subtype counter
  -- synthesis translate_off
  is unsigned(4 downto 0);

begin

end architecture RTL;
