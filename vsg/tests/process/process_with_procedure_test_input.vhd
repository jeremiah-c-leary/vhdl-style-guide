entity TEST_E is
end entity TEST_E;

architecture TEST_A of TEST_E is

begin

  TEST_PROCESS : process
    procedure test_procedure (
      constant test1_c    : in boolean := true
    ) is
    begin
    end procedure test_procedure;

  begin
  end process TEST_PROCESS;

end architecture TEST_A;
