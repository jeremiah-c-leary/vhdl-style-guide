
architecture RTL of FIFO is

begin

	process

	begin

		if (a = '1' or b = '0' and
		    c = '1' xor d = '1' and
		    g = x) then
			b <= '0';
		elsif (a = '1' or b = '0' and
		       c = '1' xor d = '1' and
		       g = x) then
			b <= '1';
		else
			b <= '1';
		end if;

		-- Violations below

		if (a = '1' or b = '0' and
		  c = '1' xor d = '1' and
		  g = x) then
			b <= '0';
		elsif (a = '1' or b = '0' and
		  c = '1' xor d = '1' and
		  g = x) then
			b <= '1';
		else
			b <= '1';
		end if;

		if a = 1 then
			b <= 1;
		elsif
		     b = 1 then
			c <= 2;
		end if;

	end process;

	-- Check comments in if statements
	process begin

		if (a = 1 and
-- Comment
		b = 0) then
			b <= '1';
		end if;
	end process;

end architecture RTL;
