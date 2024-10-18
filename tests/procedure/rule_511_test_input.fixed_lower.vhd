package rule_511_test_input is

  procedure overflow (
    a          : integer;
    variable a : integer;
    constant a : integer;
    signal   a : integer;
    file     a : file_type
  );

  procedure overflow (
    a          : integer;
    variable a : integer;
    constant a : integer;
    signal   a : integer;
    file     a : file_type
  );

end package;

architecture rtl of test is

  procedure overflow (
    a          : integer;
    variable a : integer;
    constant a : integer;
    signal   a : integer;
    file     a : file_type
  ) is
  begin

  end procedure overflow;

  procedure overflow (
    a          : integer;
    variable a : integer;
    constant a : integer;
    signal   a : integer;
    file     a : file_type
  ) is
  begin

  end procedure overflow;

begin

end architecture rtl;
