
architecture RTL of FIFO is

begin

	process

	begin

		if (a = '1' or b = '0' and
		    c = '1' xor d = '1' and
		    g = x) then
			b <= '0';
		end if;
	end process;

end architecture RTL;
