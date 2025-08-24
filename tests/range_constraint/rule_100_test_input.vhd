
architecture RTL of FIFO is

  -- Passing

  type my_array is array (natural range 0 to 7) of std_logic_vector(7 downto 0);
  type my_array is array (natural range 0 to 7) of integer;
  subtype my_array is natural range 7 downto 0;

  -- Violation below

  type my_array is array (natural       range 0 to 7) of std_logic_vector(7 downto 0);
  type my_array is array (natural       range 0 to 7) of integer;
  subtype my_array is natural       range 7 downto 0;


begin

end architecture RTL;
