
architecture RTL of FIFO is

begin

  -- These are passing

  a <=
    b or
    d;

  a <=
    '0' when c = '0' else
    '1' when d = '1' else
    'Z';

  -- Failing variations

  a <= b or
       d;

  a <= '0' when c = '0' else
       '1' when d = '1' else
       'Z';

  -- Arrays should be ignored

  a <= (
        b => 0,
        c => 6
       );

end architecture RTL;
