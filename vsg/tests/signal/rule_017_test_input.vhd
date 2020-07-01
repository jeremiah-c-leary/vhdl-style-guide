

architecture ARCH of ENTITY is

  -- This should fail
  signal sig1, sig2, sig3 : std_logic;

  -- This should pass
  signal sig4 : std_logic_vector(3 downto 0);

  -- This should pass
  signal sig5,
         sig6,
         sig7 : std_logic;

  -- This should fail
  signal sig1, sig2 : std_logic;

  -- this should fail
  signal sig1,
         sig2, sig3,
         sig4 : std_logic;

begin


end architecture ARCH;
