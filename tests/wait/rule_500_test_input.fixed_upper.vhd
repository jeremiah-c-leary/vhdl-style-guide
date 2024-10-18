
architecture rtl of test is

  procedure overflow  is
  begin

    WAIT on a;
    WAIT until a;
    WAIT for a;

    WAIT ON A;
    WAIT UNTIL A;
    WAIT FOR A;

  end procedure overflow;

begin

end architecture rtl;
