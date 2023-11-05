
architecture RTL of ENTITY_NAME is

  type T_FLAG_TYPE is protected        -- protected type declaration
   procedure init (foo : real);
   impure function myfunct return boolean;

   use ieee.std_logic_1164.all;

   attribute Max_delay of Const_1: constant is 10 ns;

   function PARITY is new uninstantiated_subprogram_name;

   procedure PARITY is new uninstantiated_subprogram_name;

  end protected T_FLAG_TYPE;

begin

end architecture RTL;
