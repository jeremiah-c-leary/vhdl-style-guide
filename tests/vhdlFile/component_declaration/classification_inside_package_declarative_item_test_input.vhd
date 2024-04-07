
architecture RTL of FIFO is

  component COMP is

  end component COMP;

  component COMP

  end component COMP;

  component COMP

  end component;

  -- test with generics
  component COMP is
    generic (
      G_GEN1 : integer := 1;
      G_GEN2 : integer := 0
    );
  end component COMP;

  -- test with ports
  component COMP is
    port (
      I_PORT : in integer := 1;
      O_PORT : out integer := 0
    );
  end component COMP;

  -- test with both
  component COMP is
    generic (
      G_GEN1 : integer := 1;
      G_GEN2 : integer := 0
    );
    port (
      I_PORT : in integer := 1;
      O_PORT : out integer := 0
    );
  end component COMP;

end architecture RTL;
