
architecture RTL of FIFO is

  procedure proc1 is
  begin
  end procedure proc1;

  signal wr_en : std_logic;

  -- Violations follow
  procedure proc1 is
  begin
  end procedure proc1;

  signal wr_en : std_logic;

begin

end architecture RTL;
