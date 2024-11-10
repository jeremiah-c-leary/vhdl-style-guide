
package test is

  procedure my_proc (
    PARAM1          : IN integer;
    VARIABLE PARAM2 : OUT integer;
    CONSTANT PARAM3 : IN integer;
    SIGNAL PARAM4   : OUT integer;
    FILE PARAM5     : MY_FILE
  );

  procedure my_proc (
    PARAM1          : IN integer;
    VARIABLE PARAM2 : OUT integer;
    CONSTANT PARAM3 : IN integer;
    SIGNAL PARAM4   : OUT integer;
    FILE PARAM5     : MY_FILE
  );

end package test;
