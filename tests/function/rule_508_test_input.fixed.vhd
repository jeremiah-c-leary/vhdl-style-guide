
architecture rtl of test is

  function my_func (
    param1          : in integer;
    variable param2 : out integer;
    constant param3 : in integer;
    signal param4   : out integer;
    file param5     : my_file
  ) return integer is

    constant con : integer := param1;
    variable var : integer := param4;

    procedure my_proc (
      param1          : in integer;
      variable param2 : out integer;
      constant param3 : in integer;
      signal param4   : out integer;
      file param5     : my_file
    ) is
      constant con : integer := param1;
    begin
      loop
        next when param3 = param4;
      end loop;
    end procedure;

    function my_func (
      param1          : in integer;
      variable param2 : out integer;
      constant param3 : in integer;
      signal param4   : out integer;
      file param5     : my_file
    ) return integer is

      constant con : integer := param1;
      variable var : integer := param4;

    begin

      -- PARAM1
      sig <= param1 + param2;
      var := param1 + param2;
      sig <= param1 when true else param2;
      var := param1 when true else param2;
      with param5 select param4 :=
        param1 when 1,
        param2 when 0,
        param3 when others;
      with param4 select param5 <=
        param1 when 1,
        param2 when 0,
        param3 when others;

      return param1;

    end function my_func;

  begin

    -- PARAM1
    sig <= param1 + param2;
    var := param1 + param2;
    sig <= param1 when true else param2;
    var := param1 when true else param2;
    with param5 select param4 :=
      param1 when 1,
      param2 when 0,
      param3 when others;
    with param4 select param5 <=
      param1 when 1,
      param2 when 0,
      param3 when others;

    return my_func(
      param1 => param1,
      param2 => param2,
      param3 => param3,
      param4 => param4,
      param5 => param5
    );

  end function my_func;

  function my_func (
    Param1          : in integer;
    variable Param2 : out integer;
    constant Param3 : in integer;
    signal Param4   : out integer;
    file Param5     : my_file
  ) return integer is

    constant con : integer := Param1;
    variable var : integer := Param4;

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

    return Param1;

  end function my_func;

begin

end architecture rtl;