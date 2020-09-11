
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    EXIT_LABEL : exit loop_label when a(23 downto 5) = 20;

    exit loop_label when a(23 downto 5) = 20;

    EXIT_LABEL : exit when a(23 downto 5) = 20;

    exit when a(23 downto 5) = 20;

    EXIT_LABEL : exit loop_label;

    exit loop_label;

    exit;

  end process;

end architecture RTL;
