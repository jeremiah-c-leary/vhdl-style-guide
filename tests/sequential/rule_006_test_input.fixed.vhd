
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
    sig3 or -- This comment is okay
    sig4;

  end process;

end architecture RTL;
