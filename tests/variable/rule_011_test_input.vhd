
architecture RTL of ENTITY1 is

  shared variable my_shared_variable : integer;

  component comp1 is
    generic (MY_SHARED_VARIABLE : my_shared_variable := 0);
    port (My_Shared_variable : in std_logic_vector(MY_shared_variable downto 0));
  end component comp1;

  procedure procedure_1 is

    variable VAriable1 : std_logic;
    variable VAriable2 : std_logic;
    variable VAriable3 : std_logic;
    variable VAriable4 : std_logic;
    variable My_shared_variable : integer;

  begin

    VAriable1 := VAriable2 & VAriable3 & VAriable4;
    variable1 := variable2 & variable3 & variable4;

    variable1 := '0' when a = '1' else
                 '1';

    with a select
       variable1 := 0 when 0,
       variable2 := 1 when 1;

    My_shared_variable := 0;
    my_shared_variable := 0;

  end procedure procedure_1;

  procedure procedure_2 is

    variable Variable1 : std_logic;
    variable Variable2 : std_logic;
    variable Variable3 : std_logic;
    variable Variable4 : std_logic;
    variable MY_shared_variable : integer;

  begin

    Variable1 := Variable2 & Variable3 & Variable4;
    variable1 := variable2 & variable3 & variable4;

    MY_shared_variable := 0;
    my_shared_variable := 0;

  end procedure procedure_2;

  procedure some_proc is
    constant something : natural;
  begin
    do_stuff(something);
  end procedure some_proc;

  procedure some_proc is
    variable something : natural;
  begin
    do_stuff(something);
  end procedure some_proc;

begin

  PROC_NAME : process () is

    variable variable1 : std_logic;
    variable variable2 : std_logic;
    variable variable3 : std_logic;
    variable variable4 : std_logic;

    procedure procedure_3 is

      variable VARiable1 : std_logic;
      variable VARiable2 : std_logic;
      variable VARiable3 : std_logic;
      variable VARiable4 : std_logic;
      variable MY_Shared_variable : integer;

    begin

      VARiable1 := VARiable2 & VARiable3 & VARiable4;
      variable1 := variable2 & variable3 & variable4;

      my_shared_variable := 0;
      MY_Shared_variable := 0;

    end procedure procedure_3;

    procedure procedure_4 is

      variable VARIable1 : std_logic;
      variable VARIable2 : std_logic;
      variable VARIable3 : std_logic;
      variable VARIable4 : std_logic;
      variable MY_SHared_variable : integer;

    begin

      VARIable1 := VARIable2 & VARIable3 & VARIable4;
      variable1 := variable2 & variable3 & variable4;

      my_shared_variable := 0;
      MY_SHared_variable := 0;

    end procedure procedure_4;

  begin

    VARIABLE1 := VARIABLE2 & VARIABLE3 & VARIABLE4;
    variable1 := variable2 & variable3 & variable4;

    My_shared_variable := 0;
    my_shared_variable := 0;

  end process PROC_NAME;

  PROC_NAME : process () is

    variable VARIABLE1 : std_logic;
    variable VARIABLE2 : std_logic;
    variable VARIABLE3 : std_logic;
    variable VARIABLE4 : std_logic;

    procedure procedure_5 is

      variable VARIAble1 : std_logic;
      variable VARIAble2 : std_logic;
      variable VARIAble3 : std_logic;
      variable VARIAble4 : std_logic;
      variable MY_SHAred_variable : integer;

    begin

      VARIAble1 := VARIAble2 & VARIAble3 & VARIAble4;
      variable1 := variable2 & variable3 & variable4;

      MY_SHAred_variable := 0;
      my_shared_variable := 0;

    end procedure procedure_5;

    procedure procedure_6 is

      variable VARIABle1 : std_logic;
      variable VARIABle2 : std_logic;
      variable VARIABle3 : std_logic;
      variable VARIABle4 : std_logic;
      variable MY_SHARed_variable : integer;

    begin

      VARIABle1 := VARIABle2 & VARIABle3 & VARIABle4;
      variable1 := variable2 & variable3 & variable4;

      MY_SHARed_variable := 0;
      my_shared_variable := 0;

    end procedure procedure_6;

  begin

    VARIABLE1 := VARIABLE2 & VARIABLE3 & VARIABLE4;
    variable1 := variable2 & variable3 & variable4;

    My_shared_variable := 0;
    my_shared_variable := 0;

  end process PROC_NAME;

  BLOCK_1 : block is

    shared variable my_Shared_variable : integer;

  begin

    BLOCK_1_1 : block is

      shared variable my_SHARED_variable : integer;

    begin

      PROC_NAME : process () is

        variable variable1 : std_logic;
        variable variable2 : std_logic;
        variable variable3 : std_logic;
        variable variable4 : std_logic;

        procedure procedure_3 is

          variable VARiable1 : std_logic;
          variable VARiable2 : std_logic;
          variable VARiable3 : std_logic;
          variable VARiable4 : std_logic;
          variable MY_Shared_variable : integer;

        begin

          VARiable1 := VARiable2 & VARiable3 & VARiable4;
          variable1 := variable2 & variable3 & variable4;

          my_shared_variable := 0;
          MY_Shared_variable := 0;

        end procedure procedure_3;

        procedure procedure_4 is

          variable VARIable1 : std_logic;
          variable VARIable2 : std_logic;
          variable VARIable3 : std_logic;
          variable VARIable4 : std_logic;
          variable MY_SHared_variable : integer;

        begin

          VARIable1 := VARIable2 & VARIable3 & VARIable4;
          variable1 := variable2 & variable3 & variable4;

          my_SHARED_variable := 0;
          my_shared_variable := 0;

        end procedure procedure_4;

      begin

        VARIABLE1 := VARIABLE2 & VARIABLE3 & VARIABLE4;
        variable1 := variable2 & variable3 & variable4;

        My_shared_variable := 0;
        my_shared_variable := 0;

      end process PROC_NAME;

    end block BLOCK_1_1;

    PROC_NAME : process () is

      variable VARIABLE1 : std_logic;
      variable VARIABLE2 : std_logic;
      variable VARIABLE3 : std_logic;
      variable VARIABLE4 : std_logic;

      procedure procedure_5 is

        variable VARIAble1 : std_logic;
        variable VARIAble2 : std_logic;
        variable VARIAble3 : std_logic;
        variable VARIAble4 : std_logic;
        variable MY_SHAred_variable : integer;

      begin

        VARIAble1 := VARIAble2 & VARIAble3 & VARIAble4;
        variable1 := variable2 & variable3 & variable4;

        MY_SHAred_variable := 0;
        my_shared_variable := 0;

      end procedure procedure_5;

      procedure procedure_6 is

        variable VARIABle1 : std_logic;
        variable VARIABle2 : std_logic;
        variable VARIABle3 : std_logic;
        variable VARIABle4 : std_logic;
        variable MY_SHARed_variable : integer;

      begin

        VARIABle1 := VARIABle2 & VARIABle3 & VARIABle4;
        variable1 := variable2 & variable3 & variable4;

        MY_SHARed_variable := 0;
        my_shared_variable := 0;

      end procedure procedure_6;

    begin

      VARIABLE1 := VARIABLE2 & VARIABLE3 & VARIABLE4;
      variable1 := variable2 & variable3 & variable4;

      my_Shared_variable := 0;
      my_shared_variable := 0;

    end process PROC_NAME;

  end block BLOCK_1;

end architecture RTL;

package body my_package is

  shared variable my_shared_VARIABLE : integer;

  procedure procedure_p1 is

    variable VARiaBle1 : std_logic;
    variable VARiaBle2 : std_logic;
    variable VARiaBle3 : std_logic;
    variable VARiaBle4 : std_logic;
    variable my_sharED_VARIABLE : integer;

    procedure procedure_p1a is

      variable VARiABle1 : std_logic;
      variable VARiABle2 : std_logic;
      variable VARiABle3 : std_logic;
      variable VARiABle4 : std_logic;
      variable my_shaRED_VARIABLE : integer;

    begin

      VARiABle1 := VARiABle2 & VARiABle3 & VARiABle4;
      variable1 := variable2 & variable3 & variable4;

      my_shaRED_VARIABLE := 0;
      my_shared_variable := 0;

    end procedure procedure_p1a;

  begin

    VARiaBle1 := VARiaBle2 & VARiaBle3 & VARiaBle4;
    variable1 := variable2 & variable3 & variable4;

    my_sharED_VARIABLE := 0;
    my_shared_variable := 0;

  end procedure procedure_p1;

end package body;

--=============================================================================
-- Issue #1023 test
--=============================================================================

PACKAGE BODY var_pkg IS


  FUNCTION to_slv (input : char) RETURN boolean IS
  BEGIN
    CASE input IS
      WHEN 'C'|'c' =>
        RETURN true;

      WHEN OTHERS =>
        RETURN false;
    END CASE;

  END FUNCTION;


  FUNCTION to_char (int : integer) RETURN character IS

    VARIABLE c : character;

  BEGIN

    CASE int IS
      WHEN 'C'|'c' =>
        c := 'Z';
      WHEN 0 =>
        c := '0';
      WHEN 1 =>
        c := '1';
      WHEN OTHERS =>
        c := '?';
    END CASE;

    RETURN c;

  END FUNCTION to_char;

END PACKAGE BODY var_pkg;

--=============================================================================
-- Issue #998 test
--=============================================================================

architecture arch of test is

begin

  ps_test0 : process is

    ----------------------------------------------------------------------------
    -- procedure_1

    procedure procedure_1 (
      constant INSN_BASE : in integer;
      constant ADDR      : in integer
    ) is

      variable test_var0 : integer;
      variable test_var1 : integer;

    begin

      test_var0 := INSN_BASE;
      test_var1 := ADDR;

    end procedure procedure_1;

  begin -- ps_test0

  end process ps_test0;

  ps_test1 : process is

    ----------------------------------------------------------------------------
    -- procedure_2

    procedure procedure_2 is

      variable addr      : integer;
      variable insn_base : integer;

    begin

    end procedure procedure_2;

  begin -- ps_test1

  end process ps_test1;

end architecture arch;

package pkg_test is

  -- Helper function
  function function1 (
    constant ADDR : std_logic_vector
  ) return std_logic_vector;

  function function2 (
    constant MY_ADDR : natural
  ) return std_logic_vector;

end package pkg_test;


package body pkg_test is

  function function1 (
    constant ADDR : std_logic_vector
  ) return std_logic_vector is
  begin
    return ADDR;
  end function function1;

  function function2 (
    constant MY_ADDR : natural
  ) return std_logic_vector is
    variable addr : std_logic_vector(31 downto 0);
  begin
    addr := std_logic_vector(to_unsigned(MY_ADDR, addr'length));
    return addr;
  end function function2;

end package body pkg_test;

--=============================================================================
-- Issue #1335 test
--=============================================================================

architecture rtl of test is

  procedure my_proc (
    signal param1   : integer;
    variable param2 : integer
  ) is
  begin

  end procedure my_proc;

  signal sig1 : integer;

begin

  process1 : process is

    variable var1 : integer;

  begin

    my_proc(
            param1 => SIG1,
            param2 => VAR1
          );

  end process process1;

end architecture rtl;
