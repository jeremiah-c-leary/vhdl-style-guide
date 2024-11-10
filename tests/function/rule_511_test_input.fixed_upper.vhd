package rule_511_test_input is

  function overflow (
    a          : integer;
    VARIABLE a : integer;
    CONSTANT a : integer;
    SIGNAL   a : integer;
    FILE     a : file_type
  ) return integer;

  function overflow (
    a          : integer;
    VARIABLE a : integer;
    CONSTANT a : integer;
    SIGNAL   a : integer;
    FILE     a : file_type
  ) return integer;

end package;

architecture rtl of test is

  function overflow (
    a          : integer;
    VARIABLE a : integer;
    CONSTANT a : integer;
    SIGNAL   a : integer;
    FILE     a : file_type
  ) return integer is
  begin

  end function overflow;

  function overflow (
    a          : integer;
    VARIABLE a : integer;
    CONSTANT a : integer;
    SIGNAL   a : integer;
    FILE     a : file_type
  ) return integer is
  begin

  end function overflow;

begin

end architecture rtl;
