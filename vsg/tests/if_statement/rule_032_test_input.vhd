
architecture RTL of FIFO is

begin

  process

  begin

    if a = '1' then
      b <= '0';
    -- Some comment
    elsif c = '1' then
      b <= '1';
    else
      if x = '1' then
        z <= '0';
      -- Some comment
      -- Some comment
      -- Some comment
      elsif x = '0' then
        z <= '1';
      else
        z <= 'Z';
      end if;
    end if;

    -- Violations below
    if a = '1' then
      b <= '0';
      -- Some comment
    elsif c = '1' then
      b <= '1';
    else
      if x = '1' then
        z <= '0';
-- Some comment
      -- Some comment
           -- Some comment
      elsif x = '0' then
        z <= '1';
      else
        z <= 'Z';
      end if;
    end if;


  end process;

end architecture RTL;
