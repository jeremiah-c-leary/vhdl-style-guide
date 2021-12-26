
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

  CONSTANT con_a : std_logic;
  SIGNAL   sig_a : STD_LOGIC;

BEGIN

END ARCHITECTURE rtl;

PACKAGE some_pkg IS

END PACKAGE some_pkg;

PACKAGE BODY some_pkg_body IS

END PACKAGE BODY some_pkg_body;
