package test is

  procedure my_proc (
    param1 : IN integer;
    PARAM2 : IN integer;
    PaRaM3 : OUT integer
  );

end package test;

package body test is

  procedure my_proc (
    param1 : IN integer;
    PARAM2 : IN integer;
    PaRaM3 : OUT integer
  ) is
  begin

  end procedure my_proc;

end package body test;

architecture rtl of test is

  procedure my_proc (
    param1 : IN integer;
    PARAM2 : IN integer;
    PaRaM3 : OUT integer
  ) is
  begin

  end procedure my_proc;

begin

end architecture rtl;
