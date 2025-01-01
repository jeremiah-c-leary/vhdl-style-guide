
architecture rtl of test is

  procedure overflow  is
  begin

    wait ON a;
    wait until a;
    wait for a;

    WAIT ON A;
    WAIT UNTIL A;
    WAIT FOR A;

  end procedure overflow;

begin

end architecture rtl;
