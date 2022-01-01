
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

  Component Comp_1 is
    Generic (
      G_gen_1 : Integer
    );
    Port (
      i_INPUT : In   Integer;
      o_OUTPUT : Out   Std_logic;
      io_INOUT : Inout Integer
    );
   End Component Comp_1;

Begin

  Proc_label : Process (Ab, Cd, Ef) Is

    Variable : Var_a : Std_logic_vector(7 Downto 0);

  Begin

    a <= b Or c And d Xor e;

  End Process Proc_label;

  U_Inst : Component My_Comp
    Generic Map (
      G_gen_1 => 1
    )
    Port Map (
      i_Input => W_sig_1
    );

End Architecture Rtl;

Package Some_Pkg Is

  Procedure Proc_1;

  Function Func_1 Return Integer;

End Package Some_Pkg;

Package Body Some_Pkg_Body Is

  Procedure Proc_1 Is
  Begin

  End Procedure Proc_1;

End Package Body Some_Pkg_Body;
