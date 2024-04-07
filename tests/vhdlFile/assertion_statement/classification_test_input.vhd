
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    LABEL : assert TRUE
      report "This is a string"
      severity WARNING;

    assert TRUE
      report "This is a string"
      severity WARNING;

    LABEL : assert TRUE
      report "This is a string";

    LABEL : assert TRUE
      severity WARNING;

    LABEL : assert TRUE;

  end process;

end architecture;
