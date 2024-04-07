
architecture RTL of FIFO is

begin

  process
  begin

    sig1 <= sig2;
    sig2 <= sig3;

  end process;

  -- Violations below

  process
  begin

    sig1 <= sig2;
 sig2 <= sig3; -- Comment 1

    siga <= sigb;
 sigb <= sigc;
 sigc <= sigd;

  end process;

end architecture RTL;
