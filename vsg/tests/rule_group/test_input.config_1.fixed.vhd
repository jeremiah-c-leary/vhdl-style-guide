
LIBRARY ieee;
  USE ieee.std_logic_1164.all;

ENTITY blah IS
  GENERIC (
    g_blah : STD_LOGIC
  );
  PORT (
    i_input  : IN    STD_LOGIC;
    o_output : OUT   STD_LOGIC;
    io_inout : INOUT STD_LOGIC
  );
END ENTITY blah;

ARCHITECTURE rtl OF blah IS

  CONSTANT con_a : STD_LOGIC;
  SIGNAL   sig_a : STD_LOGIC;

  COMPONENT comp_1 IS
    GENERIC (
      g_gen_1 : INTEGER
    );
    PORT (
      i_input  : IN    INTEGER;
      o_output : OUT   STD_LOGIC;
      io_inout : INOUT INTEGER
    );
  END COMPONENT comp_1;

BEGIN

  proc_label : PROCESS (Ab, Cd, Ef) IS

    VARIABLE : Var_a : STD_LOGIC_VECTOR(7 DOWNTO 0);

  BEGIN

    a <= b OR c AND d XOR e;

  END PROCESS proc_label;

  u_inst : COMPONENT my_comp
    GENERIC MAP (
      g_gen_1 => 1
    )
    PORT MAP (
      i_input => W_sig_1
    );

END ARCHITECTURE rtl;

PACKAGE some_pkg IS

  PROCEDURE proc_1;

  FUNCTION func_1 Return Integer;

END PACKAGE some_pkg;

PACKAGE BODY some_pkg_body IS

  PROCEDURE proc_1 IS
  BEGIN

  END PROCEDURE proc_1;

END PACKAGE BODY some_pkg_body;
