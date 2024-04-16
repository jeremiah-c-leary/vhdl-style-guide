
architecture RTL of FIFO is

begin

  process

  begin

    if a = '1' then
      b <= '0';
    elsif c = '1' then
      b <= '1';
    end if;

    -- Violations below
    if a = '1' then
      b <= '0';
    elsif c = '1' then
      b <= '1';
    end if;

    if a = '1' then -- comment 1
      b <= '0';
    elsif c = '1' then -- comment 2
  -- comment 3
  -- comment 4
      b <= '1';
    end if;

    if a = '1'
    -- synthesis translate_off
    then
    end if;

  end process;

end architecture RTL;
