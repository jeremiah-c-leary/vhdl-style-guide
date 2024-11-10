
package test is

  function my_func (
    PARAM1          : IN integer;
    VARIABLE PARAM2 : OUT integer;
    CONSTANT PARAM3 : IN integer;
    SIGNAL PARAM4   : OUT integer;
    FILE PARAM5     : MY_FILE
  ) return integer;

  function my_func (
    PARAM1          : IN integer;
    VARIABLE PARAM2 : OUT integer;
    CONSTANT PARAM3 : IN integer;
    SIGNAL PARAM4   : OUT integer;
    FILE PARAM5     : MY_FILE
  ) return integer;

end package test;
