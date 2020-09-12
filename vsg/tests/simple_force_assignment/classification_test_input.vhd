
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    FORCE_LABEL : sig1 <= force in a + b - c after 10 ns, d + e after 25 ns;

    FORCE_LABEL : sig1 <= force out a + b - c after 10 ns, d + e after 25 ns;

    FORCE_LABEL : sig1 <= force a + b - c after 10 ns, d + e after 25 ns;

    FORCE_LABEL : sig1 <= force a + b - c, d + e;

    FORCE_LABEL : sig1 <= force a + b - c;

    FORCE_LABEL : sig2 <= force a;

    sig2 <= force a;

  end process;

end architecture RTL;
