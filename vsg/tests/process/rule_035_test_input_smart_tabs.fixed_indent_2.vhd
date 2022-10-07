
architecture RTL of FIFO is

begin


	process

	begin

		a <= b;                          -- level 2
		ab <= xy;                        -- level 2

		-- level 2
		if (a = b) then                  -- level 2
			z <= y;                        -- level 3
		-- level 2
		elsif (a + b -c = z) then        -- level 2
			z <= x;                        -- level 3
		end if;                          -- level 2

	end process;  -- level 1

end architecture RTL;
