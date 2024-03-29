
architecture RTL of ENTITY1 is

  subtype st_range is integer range 0 to 9;
  subtype st_width is integer range 16 to 128;

  subtype subt_range is integer range 0 to 9;
  subtype subt_width is integer range 16 to 128;

  subtype stRange is integer range 0 to 9;
  subtype stWidth is integer range 16 to 128;

  subtype MAJOR_FIELD is std_logic_vector(7 downto 0);
  subtype major_field is std_logic_vector(7 downto 0);

  subtype MINOR_FIELD is std_logic_vector(7 downto 0);
  subtype minor_field is std_logic_vector(7 downto 0);

begin

end architecture RTL;
