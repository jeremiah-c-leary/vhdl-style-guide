
architecture RTL of FIFO is

  subtype my_subtype is my_type(1 downto 0);
  subtype my_slv is std_logic_vector(1 downto 0);
  subtype my_uslv is std_ulogic_vector(1 downto 0);
  subtype my_s is signed(1 downto 0);
  subtype my_u is unsigned(1 downto 0);
  subtype my_sl is std_ulogic('0', '1');
  subtype my_usl is std_logic('0', '1');
  subtype my_int is integer range 1 to 100;
  subtype my_nat is natural range 1 to 100;

  -- Violations below

  subtype my_subtype is my_type(1 downto 0);
  subtype my_slv is std_logic_vector(1 downto 0);
  subtype my_uslv is std_ulogic_vector(1 downto 0);
  subtype my_s is signed(1 downto 0);
  subtype my_u is unsigned(1 downto 0);
  subtype my_sl is std_ulogic('0', '1');
  subtype my_usl is std_logic('0', '1');
  subtype my_int is integer range 1 to 100;
  subtype my_nat is natural range 1 to 100;

begin

end architecture RTL;
