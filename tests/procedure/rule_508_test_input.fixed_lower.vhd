
package test is

  procedure my_proc (
    param1          : IN integer;
    VARIABLE param2 : OUT integer;
    CONSTANT param3 : IN integer;
    SIGNAL param4   : OUT integer;
    FILE param5     : MY_FILE
  );

  procedure my_proc (
    param1          : IN integer;
    VARIABLE param2 : OUT integer;
    CONSTANT param3 : IN integer;
    SIGNAL param4   : OUT integer;
    FILE param5     : MY_FILE
  );

end package test;
