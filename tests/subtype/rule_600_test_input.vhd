
architecture RTL of ENTITY1 is

  subtype range_st is integer range 0 to 9;
  subtype width_st is integer range 16 to 128;

  subtype range_subt is integer range 0 to 9;
  subtype width_subt is integer range 16 to 128;

  subtype rangest is integer range 0 to 9;
  subtype widthst is integer range 16 to 128;

  subtype MAJOR_FIELD is std_logic_vector(7 downto 0);
  subtype major_field is std_logic_vector(7 downto 0);

  subtype MINOR_FIELD is std_logic_vector(7 downto 0);
  subtype minor_field is std_logic_vector(7 downto 0);

begin

end architecture RTL;
