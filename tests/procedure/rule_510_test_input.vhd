package rule_510_test_input is

  procedure overflow (
    a : in    integer;
    b : out   integer;
    c : inout integer
  );

  procedure overflow (
    a : IN    integer;
    b : OUT   integer;
    c : INOUT integer
  );

end package;

package body rule_510_test_input is

  procedure overflow (
    a : in    integer;
    b : out   integer;
    c : inout integer
  ) is
  begin
  end procedure;

  procedure overflow (
    a : IN    integer;
    b : OUT   integer;
    c : INOUT integer
  ) is
  begin
  end procedure;

end package body;
