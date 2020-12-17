
architecture RTL of ENTITY_NAME is

  type T_FLAG_TYPE is protected        -- protected type declaration
   procedure init (foo : real);
   impure function myfunct return boolean;
  end protected T_FLAG_TYPE;

begin

end architecture RTL;
