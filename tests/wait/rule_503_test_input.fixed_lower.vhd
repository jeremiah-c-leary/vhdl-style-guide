
architecture rtl of test is

  procedure overflow  is
  begin

    wait on a;
    wait until a;
    wait for a;

    WAIT ON A;
    WAIT UNTIL A;
    WAIT for A;

  end procedure overflow;

begin

end architecture rtl;
