
library ieee;
  use IEEE.STD_LOGIC_1164.all;

entity BLAH is
  generic (
    G_BLAH : STD_LOGIC
  );
  port (
    I_INPUT  : in    STD_LOGIC;
    O_OUTPUT : out   STD_LOGIC;
    IO_INOUT : inout STD_LOGIC
  );
end entity BLAH;

architecture RTL of BLAH is

  constant CON_A : STD_LOGIC;
  signal   SIG_A : STD_LOGIC;

  component COMP_1 is
    generic (
      G_GEN_1 : INTEGER
    );
    port (
      I_INPUT  : in    INTEGER;
      O_OUTPUT : out   STD_LOGIC;
      IO_INOUT : inout INTEGER
    );
  end component COMP_1;

begin

  PROC_LABEL : process (Ab, Cd, Ef) is

    variable VAR_A : STD_LOGIC_VECTOR(7 downto 0);

  begin

    a <= b or c and d xor e;

  end process PROC_LABEL;

  U_INST : component MY_COMP
    generic map (
      G_GEN_1 => 1
    )
    port map (
      I_INPUT => W_sig_1
    );

end architecture RTL;

package SOME_PKG is

  procedure PROC_1;

  function FUNC_1 return integer;

end package SOME_PKG;

package body SOME_PKG_BODY is

  procedure PROC_1 is
  begin

  end procedure PROC_1;

end package body SOME_PKG_BODY;
