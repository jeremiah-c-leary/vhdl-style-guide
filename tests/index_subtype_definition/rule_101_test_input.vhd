
architecture RTL of FIFO is

  -- Passing

  type my_array is array (natural range <>) of std_logic_vector(7 downto 0);

  -- Violation below

  type my_array is array (natural range        <>) of std_logic_vector(7 downto 0);

begin

end architecture RTL;
