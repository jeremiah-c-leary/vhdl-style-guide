package test is

  function my_func (
    PARAM1 : IN integer;
    PARAM2 : IN integer;
    PARAM3 : OUT integer
  ) return integer;

end package test;

package body test is

  function my_func (
    PARAM1 : IN integer;
    PARAM2 : IN integer;
    PARAM3 : OUT integer
  ) return integer is
  begin

  end function my_func;

end package body test;

architecture rtl of test is

  function my_func (
    PARAM1 : IN integer;
    PARAM2 : IN integer;
    PARAM3 : OUT integer
  ) return integer is
  begin

  end function my_func;

begin

end architecture rtl;
