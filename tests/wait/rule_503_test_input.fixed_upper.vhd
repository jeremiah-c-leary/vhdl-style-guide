
architecture rtl of test is

  procedure overflow  is
  begin

    wait on a;
    wait until a;
    wait FOR a;

    WAIT ON A;
    WAIT UNTIL A;
    WAIT FOR A;

  end procedure overflow;

begin

end architecture rtl;
