
architecture RTL of FIFO is

  procedure proc1 is
  begin
  end procedure proc1;

  procedure proc1 (
    constant a : in integer;
    signal d : out std_logic
  ) is
  begin
  end procedure proc1;

  procedure proc1 is

  begin
  end procedure proc1;

  procedure proc1 (
    constant a : in integer;
    signal d : out std_logic
  ) is

  begin
  end procedure proc1;

  procedure proc1 is
    constant width : integer := 32;

  begin
  end procedure proc1;

  procedure proc1 (
    constant a : in integer;
    signal d : out std_logic
  ) is
    constant width : integer := 32;

  begin
  end procedure proc1;

  -- Fixes follow

  procedure proc1 is
    constant width : integer := 32;

  begin
  end procedure proc1;

  procedure proc1 (
    constant a : in integer;
    signal d : out std_logic
  ) is
    constant width : integer := 32;

  begin
  end procedure proc1;

begin

end architecture RTL;
