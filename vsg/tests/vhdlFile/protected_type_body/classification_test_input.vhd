
architecture RTL of ENTITY_NAME is

  type T_FLAG_TYPE is protected body       -- protected type declaration
   procedure init (foo : real);
   impure function myfunct return boolean;

   constant c_con1 : std_logic;
   variable v_var1 : integer;

  end protected body T_FLAG_TYPE;

begin

end architecture RTL;
