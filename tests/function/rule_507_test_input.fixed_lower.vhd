
package test is

  function my_func (
    param1          : IN integer;
    VARIABLE param2 : OUT integer;
    CONSTANT param3 : IN integer;
    SIGNAL param4   : OUT integer;
    FILE param5     : MY_FILE
  ) return integer;

  function my_func (
    param1          : IN integer;
    VARIABLE param2 : OUT integer;
    CONSTANT param3 : IN integer;
    SIGNAL param4   : OUT integer;
    FILE param5     : MY_FILE
  ) return integer;

end package test;
