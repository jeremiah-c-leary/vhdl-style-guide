
architecture rtl of test is

  procedure overflow  is
  begin

    wait on a;
    wait until a;
    wait for a;

    WAIT ON A;
    WAIT until A;
    WAIT FOR A;

  end procedure overflow;

begin

end architecture rtl;
