
architecture RTL of FIFO is

begin

  process
  begin

    -- These are passing

    a := b or
      d;

    a := '0' when c = '0' else
      '1' when d = '1' else
      'Z';

    -- Failing variations

    a := b or
         d;

    a := '0' when c = '0' else
         '1' when d = '1' else
         'Z';

  end process;

end architecture RTL;
