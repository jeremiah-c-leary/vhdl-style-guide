
architecture rtl of fifo is

  procedure my_proc is
  begin

    for x in t_range loop end loop;

    for x IN t_range loop end loop;

  end procedure;

begin

  process begin

    for x in (31 downto 0) loop end loop;

    for x IN (31 downto 0) loop end loop;

  end process;

  gen_label : for x in range (3 downto 0) generate

  end generate;

  gen_label : for x IN range (3 downto 0) generate

  end generate;

end;
