
-- This is valid
architecture RTL of ENTITY1 is

begin

end architecture RTL;

-- This is not valid
architecture ENTITY1 of entity1 is

begin

end architecture ENTITY1;

-- This is valid
architecture BLUE of ENTITY1 is

begin

end architecture BLUE;

-- This is not valid
architecture CDC of ENTITY1 is

begin

end architecture CDC;
