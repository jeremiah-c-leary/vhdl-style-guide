
architecture rtl of test is

  -- Simple function
  function my_func (
    Param1          : in integer;
    variable Param2 : out integer;
    constant Param3 : in integer;
    signal Param4   : out integer;
    file Param5     : my_file
  ) return integer is

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

  end function my_func;

  -- No parameters in this function - the contents shouldn't change.
  function my_func return integer is

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

  end function my_func;

  -- Function with nested subprograms.
  function my_func (
    param1          : in integer;
    variable param2 : out integer;
    constant param3 : in integer;
    signal param4   : out integer;
    file param5     : my_file
  ) return integer is

    constant con : integer := paRAM1;
    variable var : integer := paRAM4;

    procedure PARAM1 (
      PARAM1          : in integer;
      variable PARAM2 : out integer;
      constant PARAM3 : in integer
    ) is
      constant con : integer := param1;
    begin
      loop
        next when parAM3 = PARAm4;
      end loop;
    end procedure;

    function my_func (
      variable Param2 : out integer;
      constant Param3 : in integer;
      signal Param4   : out integer;
      file Param5     : my_file
    ) return integer is

      constant con : integer := param1;
      variable var : integer := PARAM4;

    begin

      -- PARAM1
      sig <= PARAM1 + ParaM2;
      var := PARAM1 + ParaM2;
      sig <= PARAM1 when true else ParaM2;
      var := PARAM1 when true else ParaM2;
      with param5 select param4 :=
        PARAM1 when 1,
        ParaM2 when 0,
        Param3 when others;
      with param4 select param5 <=
        PARAM1 when 1,
        ParaM2 when 0,
        Param3 when others;

      return PARAM1;

    end function my_func;

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

    return my_func(
      param1 => pAram1,
      param2 => pAram2,
      param3 => pAram3,
      param4 => pAram4,
      param5 => pAram5
    );

  end function my_func;

  -- Procedure with nested subprograms.
  procedure my_proc (
    param1          : in integer;
    variable param2 : out integer;
    constant param3 : in integer;
    signal param4   : out integer;
    file param5     : my_file
  ) is

    constant con : integer := PARAM1;
    variable var : integer := PARam4;

    procedure PARAM1 (
      PARAM1          : in integer;
      variable PARAM2 : out integer;
      constant PARAM3 : in integer
    ) is
      constant con : integer := PARaM1;
    begin
      loop
        next when PARaM3 = PARam4;
      end loop;
    end procedure;

    function my_func (
      variable Param2 : out integer;
      constant Param3 : in integer;
      signal Param4   : out integer;
      file Param5     : my_file
    ) return integer is

      constant con : integer := PARAM1;
      variable var : integer := param4;

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

    end function my_func;

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

    return my_func(
      param1 => parAm1,
      param2 => parAm2,
      param3 => parAm3,
      param4 => parAm4,
      param5 => parAm5
    );

  end procedure my_proc;

begin

end architecture rtl;
