

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

  constant c_length_constant : integer := I_FOO'length     + I_BAR'length +
                                          I_MOREFOO'length + I_MOREBAR'length + 1;

  constant c_length_constant : integer := I_FOO'length     + I_BAR'length +
    I_MOREFOO'length + I_MOREBAR'length + 1;

end package PACK;

architecture RTL of ENTITY1 is

begin

  constant1 <= A;
  constant_2 <= B;

end architecture RTL;
