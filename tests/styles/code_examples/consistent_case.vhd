
architecture RTL of FIFO is

  procedure average_samples;

begin

  Average_samples;

  PROC1 : process () is
  begin

     AVERAGE_SAMPLES;
     AVERAGE_SaMPLES;
     aVeRAGE_SaMPLES;

  end process;

end architecture RTL;

-- Test scoping

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

      TEST_VAR0 := insn_base;
      TEST_VAR1 := addr;

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

      Addr := TEst_Var0;
      INSN_base := TEST_VAR1;

      addr := TEst_Var0;
      insn_base := TEST_VAR1;

    end procedure procedure_2;

  begin -- ps_test1

  end process ps_test1;

end architecture arch;

-- Additional scoping test

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

      TEST_VAR0 := insn_base;
      TEST_VAR1 := addr;

    end procedure procedure_1;

    ----------------------------------------------------------------------------
    -- procedure_2

    procedure procedure_2 is

      variable addr      : integer;
      variable insn_base : integer;

    begin

      Addr := TEst_Var0;
      INSN_base := TEST_VAR1;

      addr := TEst_Var0;
      insn_base := TEST_VAR1;

    end procedure procedure_2;

  begin -- ps_test1

  end process ps_test0;

end architecture arch;
