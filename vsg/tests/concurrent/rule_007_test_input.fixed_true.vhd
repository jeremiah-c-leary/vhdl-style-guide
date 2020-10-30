
architecture RTL of FIFO is

begin

  -- These are passing

  a <= '0' when c = '0' else '1';


  a <= '0' when c = '0' else-- Comment
       '1' when c = '1' else -- comment
       '0' when d = '1' else
       '1';

  -- Violations below

  a <= '0' when c = '0' else
 '1' when c = '1' else
 '0' when d = '1' else
 '1';

  a <= '0' when c = '0' else
 '1' when c = '1' else
 '0' when d =
       '1' else
 '1';

  a <= '0' when c = '0' else
 '1' when c =
       '1' else
 '0' when d = '1' else
 '1';

end architecture RTL;
