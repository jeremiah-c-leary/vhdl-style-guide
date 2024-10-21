
package rule_510_test_input is

  PURE function func1 return integer;
  IMPURE function func1 return integer;

  PURE FUNCTION FUNC1 RETURN INTEGER;
  IMPURE FUNCTION FUNC1 RETURN INTEGER;

end package;

package body rule_510_test_input is

  PURE function func1 return integer is begin end function func1;
  IMPURE function func1 return integer is begin end function func1;

  PURE FUNCTION FUNC1 RETURN INTEGER IS BEGIN END FUNCTION FUNC1;
  IMPURE FUNCTION FUNC1 RETURN INTEGER IS BEGIN END FUNCTION FUNC1;

end package body;

architecture RTL of FIFO is

  PURE function func1 return integer is begin end function func1;
  IMPURE function func1 return integer is begin end function func1;

  PURE FUNCTION FUNC1 RETURN INTEGER IS BEGIN END FUNCTION FUNC1;
  IMPURE FUNCTION FUNC1 RETURN INTEGER IS BEGIN END FUNCTION FUNC1;

begin

end architecture RTL;