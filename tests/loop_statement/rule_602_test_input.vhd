architecture rtl of test is

begin

  proc_label : process(all)
  begin

    for lv_index in t_range loop
    end loop;

    -- Violation below

    for index in t_range loop
    end loop;

    for range_index in t_range loop
    end loop;

  end process proc_label;
end architecture;
