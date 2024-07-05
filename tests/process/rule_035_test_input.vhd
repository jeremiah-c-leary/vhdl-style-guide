
architecture RTL of FIFO is

begin


  process

  begin

    a <= b;                   -- Comment
    ab <= xy;                 -- Comment

    -- Check for something
    if (a = b) then
      z <= y;                 -- Assign this statement
    -- Check for this other thing
    elsif (a + b -c = z) then
      z <= x;                 -- Assign this other statement
    end if;

  end process;

  -- Violations below

  process

  begin

    a <= b; -- Comment
    ab <= xy; -- Comment

    -- Check for something
    if (a = b) then
      z <= y;   -- Assign this statement
    -- Check for this other thing
    elsif (a + b -c = z) then
      z <= x; -- Assign this other statement
    end if;

  end process;


end architecture RTL;
