
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

		if a = 1 then
			a <= 2;
			b := 1;
			if b = 1 then
				a  <= 2;
				b    := 3;
				if c = 1 then
					a      <= 3;
					b  := 10;
				end if;
			end if;
		end if;

	end process;

end architecture RTL;
