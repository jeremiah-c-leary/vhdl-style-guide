
architecture RTL of ENTITY1 is

  type state_machine is (IDLE, WRITE, READ, DONE);

  signal sm : state_machine;
  signal sm1 : state_machine;

  constant some_const : state_machine;

  component COMP1 is
    port (
      SIG1 : in    STATE_MACHINE;
      SIG2 : out   std_logic;
      SIG3 : in    std_logic
    );
  end component COMP1;

  procedure proc_name (
    constant a : in state_machine
    ) is
  begin
  end procedure proc_name;

  impure function func1 return state_machine is

    variable temp : state_machine;

  begin end function func1;

begin

end architecture RTL;
