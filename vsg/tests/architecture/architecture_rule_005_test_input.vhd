
-- This should not fail
architecture rtl of entity1 is

begin
end architecture rtl;

-- These should fail
architecture rtl 
of entity1 is

begin
end architecture rtl;

----------------------------
architecture rtl

     of entity1 is

begin

end architecture rtl;

----------------------------
architecture rtl
of
entity1
is
begin
end architecture rtl;


----------------------------
architecture rtl



of

entity1

is

begin

end architecture rtl;
