
architecture rtl of test is

  procedure overflow  is
  begin

    wait on a;
    wait until a;
    wait for a;

    wait ON A;
    wait UNTIL A;
    wait FOR A;

  end procedure overflow;

begin

end architecture rtl;
