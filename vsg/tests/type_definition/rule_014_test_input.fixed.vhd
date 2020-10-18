
architecture RTL of ENTITY1 is

  type state_machine is (IDLE, WRITE, READ, DONE);

  signal sm : state_machine;
  signal sm1 : state_machine;

  constant some_const : state_machine;

  component COMP1 is
    port (
      SIG1 : in    state_machine;
      SIG2 : out   std_logic;
      SIG3 : in    std_logic
    );
  end component COMP1;

begin

end architecture RTL;
