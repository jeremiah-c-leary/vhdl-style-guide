
architecture RTL of FIFO is

begin

  process
  begin

    sig1 <= sig2; -- This comment is okay

  end process;

  -- Violations below

  process
  begin

    sig1 <= sig2 and
    -- Some comment
    sig3 or -- This comment is okay
    -- other comment
    sig4;

  end process;

end architecture RTL;
