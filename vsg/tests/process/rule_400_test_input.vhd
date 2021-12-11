
architecture RTL of FIFO is

  procedure rst_procedure is
  begin
      a    <= (others => '0');
      b <= (others => '0');
      c       := d;
  end procedure;

begin

  PROC_1 : process

    procedure rst_procedure is
    begin
        a    <= (others => '0');
        b <= (others => '0');
        c       := d;
    end procedure;

  begin

    a <= 2;
    b := 1;

    a  <= 2;
    b    := 3;

    a      <= 3;
    b  := 10;

  end process;

end architecture RTL;
