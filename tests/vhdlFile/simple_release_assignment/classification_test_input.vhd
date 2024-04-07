
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    RELEASE_LABEL : sig1 <= release in;

    RELEASE_LABEL : sig2 <= release;

    sig3 <= release out;

    sign4 <= release;

  end process;

end architecture RTL;
