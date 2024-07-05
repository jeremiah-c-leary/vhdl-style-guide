
architecture RTL of FIFO is

begin

	a     <= b;
	a     <= when c = '0' else '1';
	block_label: block is
	begin
		a <= b;
		a <= c;
	end block;
	a     <= b;
	a     <= when c = '0' else '1';

end architecture RTL;
