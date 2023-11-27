
architecture RTL of ENTITY_NAME is

  type T_FLAG_TYPE is protected body       -- protected type declaration
   procedure init (foo : real);
   impure function myfunct return boolean;

   constant c_con1 : std_logic;
   variable v_var1 : integer;


   function PARITY is new uninstantiated_subprogram_name;

   procedure PARITY is new uninstantiated_subprogram_name;

   package identifier is
   end package;

   package body identifier is
   end package body;

   package pack2 is new pack2_name;

   type indentifier;

   subtype identifier is integer;

   file F1 : IntegerFile;

   alias ident is write_enable;

   attribute LOCATION: COORDINATE;

   attribute Pin_code of Sig_1: signal is 17;

   use ieee.std_logic_1164.all;

  end protected body T_FLAG_TYPE;

begin

end architecture RTL;
