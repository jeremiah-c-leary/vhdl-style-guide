
Library ieee;
  Use ieee.std_logic_1164.all;

Entity Blah Is
  Generic (
    G_blah : Std_logic
  );
  Port (
    i_INPUT  : In    Std_logic;
    o_OUTPUT : Out   Std_logic;
    io_INOUT : Inout Std_logic
  );
End Entity Blah;

Architecture Rtl Of Blah Is

  Constant Con_a : Std_logic;
  Signal Sig_a : Std_logic;

Begin

End Architecture Rtl;

Package Some_Pkg Is

End Package Some_Pkg;

Package Body Some_Pkg_Body Is

End Package Body Some_Pkg_Body;
