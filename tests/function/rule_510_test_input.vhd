package rule_510_test_input is

  function overflow (
    a : in    integer;
    b : out   integer;
    c : inout integer
  ) return integer;

  function overflow (
    a : IN    integer;
    b : OUT   integer;
    c : INOUT integer
  ) return integer;

end package;

package body rule_510_test_input is

  function overflow (
    a : in    integer;
    b : out   integer;
    c : inout integer
  ) return integer is
  begin
  end function;

  function overflow (
    a : IN    integer;
    b : OUT   integer;
    c : INOUT integer
  ) return integer is
  begin
  end function;

end package body;
