
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
    if
a = '1' then
      b <= '0';
    elsif
c = '1' then
      b <= '1';
    end if;

    if
 a = '1' then
      b <= '0';
    elsif
                      c = '1' then
      b <= '1';
    end if;

    if
                   a = '1' then
      b <= '0';
    elsif
                      c = '1' and
   d = '0' then
      b <= '1';
    end if;

    -- Comments between the keyword and the expression
    if
      -- explain the first condition
      a = '1' then
      b <= '0';
    elsif
      -- explain the second condition
      -- over two lines
      c = '1' then
      b <= '1';
    end if;

  end process;

end architecture RTL;
