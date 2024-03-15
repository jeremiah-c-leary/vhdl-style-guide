
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    FORCE_LABEL : sig1 := a + b - c after 10 ns, d + e after 25 ns;

    FORCE_LABEL : sig1 := a + b - c after 10 ns, d + e after 25 ns;

    FORCE_LABEL : sig1 := a + b - c after 10 ns, d + e after 25 ns;

    FORCE_LABEL : sig1 := a + b - c, d + e;

    FORCE_LABEL : sig1 := a + b - c;

    FORCE_LABEL : sig2 := a;

    sig2 := a;

  end process;

end architecture RTL;
