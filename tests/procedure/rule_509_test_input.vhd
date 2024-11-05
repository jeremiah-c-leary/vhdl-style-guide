
architecture rtl of test is

  procedure my_proc (
    param1          : in integer;
    variable param2 : out integer;
    constant param3 : in integer;
    signal param4   : out integer;
    file param5     : my_file
  ) is

    constant con : integer := PARAM1;
    variable var : integer := PARAM4;

    function my_func (
      PARAM1          : in integer;
      variable PARAM2 : out integer;
      constant PARAM3 : in integer;
      signal PARAM4   : out integer;
      file PARAM5     : my_file
    ) return integer is
      constant con : integer := param1;
    begin
      loop
        next when param3 = param4;
      end loop;
    end function;

    procedure my_proc (
      Param1          : in integer;
      variable Param2 : out integer;
      constant Param3 : in integer;
      signal Param4   : out integer;
      file Param5     : my_file
    ) is

      constant con : integer := PARAM1;
      variable var : integer := PARAM4;

    begin

      -- PARAM1
      sig <= PARAM1 + PARAM2;
      var := PARAM1 + PARAM2;
      sig <= PARAM1 when true else PARAM2;
      var := PARAM1 when true else PARAM2;
      with PARAM5 select PARAM4 :=
        PARAM1 when 1,
        PARAM2 when 0,
        PARAM3 when others;
      with PARAM4 select PARAM5 <=
        PARAM1 when 1,
        PARAM2 when 0,
        PARAM3 when others;

      return PARAM1;

    end procedure my_proc;

  begin

    -- PARAM1
    sig <= Param1 + Param2;
    var := Param1 + Param2;
    sig <= Param1 when true else Param2;
    var := Param1 when true else Param2;
    with Param5 select Param4 :=
      Param1 when 1,
      Param2 when 0,
      Param3 when others;
    with Param4 select Param5 <=
      Param1 when 1,
      Param2 when 0,
      Param3 when others;

    return my_proc(
      Param1 => Param1,
      Param2 => Param2,
      Param3 => Param3,
      Param4 => Param4,
      Param5 => Param5
    );

  end procedure my_proc;

  procedure my_proc (
    Param1          : in integer;
    variable Param2 : out integer;
    constant Param3 : in integer;
    signal Param4   : out integer;
    file Param5     : my_file
  ) is

    constant con : integer := PARAM1;
    variable var : integer := PARAM4;

  begin

    -- PARAM1
    sig <= PARAM1 + PARAM2;
    var := PARAM1 + PARAM2;
    sig <= PARAM1 when true else PARAM2;
    var := PARAM1 when true else PARAM2;
    with PARAM5 select PARAM4 :=
      PARAM1 when 1,
      PARAM2 when 0,
      PARAM3 when others;
    with PARAM4 select PARAM5 <=
      PARAM1 when 1,
      PARAM2 when 0,
      PARAM3 when others;

    return PARAM1;

  end procedure my_proc;

  procedure my_proc is

    constant con : integer := PARAM1;
    variable var : integer := PARAM4;

  begin

    -- PARAM1
    sig <= PARAM1 + PARAM2;
    var := PARAM1 + PARAM2;
    sig <= PARAM1 when true else PARAM2;
    var := PARAM1 when true else PARAM2;
    with PARAM5 select PARAM4 :=
      PARAM1 when 1,
      PARAM2 when 0,
      PARAM3 when others;
    with PARAM4 select PARAM5 <=
      PARAM1 when 1,
      PARAM2 when 0,
      PARAM3 when others;

    return PARAM1;

  end procedure my_proc;

begin

end architecture rtl;
