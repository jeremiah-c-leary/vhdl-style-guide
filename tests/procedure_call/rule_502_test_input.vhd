architecture rtl of test is

  procedure my_proc (
    param1 : IN integer;
    PARAM2 : IN integer;
    PaRaM3 : OUT integer
  ) is
  begin

  end procedure my_proc;

  procedure outer_proc is
  begin

    my_proc (
      param1 => sig1,
      PARAM2 => SIG2,
      PaRaM3 => SiG3
    );

  end procedure;

begin

  my_proc (
    param1 => sig1,
    PARAM2 => SIG2,
    PaRaM3 => SiG3
  );

  process (all)
  begin

    my_proc (
      param1 => sig1,
      PARAM2 => SIG2,
      PaRaM3 => SiG3
    );

  end process;
end architecture rtl;
