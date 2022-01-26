
library ieee;
  use ieee.std_logic_1164.all;

entity BLAH is
  generic (
    G_BLAH : std_logic
  );
  port (
    I_INPUT  : in    std_logic;
    O_OUTPUT : out   std_logic;
    IO_INOUT : inout std_logic
  );
end entity BLAH;

ARCHITECTURE RTL of BLAH is

  constant CON_A : STD_LOGIC;
  signal   SIG_A : STD_LOGIC;

  component COMP_1 is
    generic (
      G_GEN_1 : integer
    );
    port (
      I_INPUT  : in    integer;
      O_OUTPUT : out   std_logic;
      IO_INOUT : inout integer
    );
  end component COMP_1;

begin

  proc_label : process (Ab, Cd, Ef) is

    variable : VAR_A : Std_logic_vector(7 downto 0);

  begin

    a <= b Or c And d Xor e;

  end process proc_label;

  u_inst : component MY_COMP
    generic map (
      G_GEN_1 => 1
    )
    port map (
      I_INPUT => W_sig_1
    );

end architecture RTL;

package SOME_PKG is

  procedure PROC_1;

  function FUNC_1 Return Integer;

end package SOME_PKG;

package body SOME_PKG_BODY is

  procedure PROC_1 is
  begin

  end procedure PROC_1;

end package body SOME_PKG_BODY;
