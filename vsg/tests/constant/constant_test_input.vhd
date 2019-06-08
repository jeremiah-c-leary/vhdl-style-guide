

architecture ARCH of ENTITY is

  constant c_const : std_logic := '1';
  constant const : std_logic := '0';
  COnstant  c_const : std_logic := '1';
Constant c_coNST :  std_logic := '0';
constant const  :  STD_LOGIC:='0';
   constant c_const: std_logic
              :='0';

begin

  PROC_1 : process (A) is

    constant c_const   : std_logic := '1';
    constant const        : std_logic := '0';

  begin

  end process PROC_1;

end architecture ARCH;

package PACK is

  constant const : std_logic := '0';

  constant rom : rom_type :=
   (
      0,
    1,
   2,
    3
    );

  constant const : std_logic   := '0';

end package PACK;
