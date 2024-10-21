
package rule_510_test_input is

  pure function func1 return integer;
  impure function func1 return integer;

  pure FUNCTION FUNC1 RETURN INTEGER;
  impure FUNCTION FUNC1 RETURN INTEGER;

end package;

package body rule_510_test_input is

  pure function func1 return integer is begin end function func1;
  impure function func1 return integer is begin end function func1;

  pure FUNCTION FUNC1 RETURN INTEGER IS BEGIN END FUNCTION FUNC1;
  impure FUNCTION FUNC1 RETURN INTEGER IS BEGIN END FUNCTION FUNC1;

end package body;

architecture RTL of FIFO is

  pure function func1 return integer is begin end function func1;
  impure function func1 return integer is begin end function func1;

  pure FUNCTION FUNC1 RETURN INTEGER IS BEGIN END FUNCTION FUNC1;
  impure FUNCTION FUNC1 RETURN INTEGER IS BEGIN END FUNCTION FUNC1;

begin

end architecture RTL;