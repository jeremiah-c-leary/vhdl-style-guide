
package pkg is

  FUNCTION my_func is new my_generic_func
    generic map (
      test => 2
    );

end package;

architecture RTL of FIFO is

  function func1 return integer is begin end function func1;

  function func1 return integer is begin end FUNCTION func1;

  function func1 return integer is begin end Function func1;

begin

end architecture RTL;
