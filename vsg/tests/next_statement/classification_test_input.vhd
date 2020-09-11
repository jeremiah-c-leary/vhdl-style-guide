
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    NEXT_LABEL : next loop_label when a(23 downto 5) = 20;

    next loop_label when a(23 downto 5) = 20;

    NEXT_LABEL : next when a(23 downto 5) = 20;

    next when a(23 downto 5) = 20;

    NEXT_LABEL : next loop_label;

    next loop_label;

    next;

  end process;

end architecture RTL;
