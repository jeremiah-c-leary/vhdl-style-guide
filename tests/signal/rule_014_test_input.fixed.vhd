
architecture RTL of ENTITY1 is

  signal sig1, sig2 : std_logic;
  signal sig9 : std_logic;
  signal sig3 : std_logic;
  signal sig4 : std_logic;
  signal sig5 : std_logic;
  signal sig6 : std_logic;
  signal sig7 : std_logic;

  component COMP1 is
    port (
      SIG1 : in    std_logic;
      SIG2 : out   std_logic;
      SIG3 : in    std_logic
    );
  end component COMP1;

begin

  PROC_NAME : process (sig2) is
  begin

    sig1 <= '0';

    if (sig2 = '0') then
      sig1 <= '1';
    elsif (sig2 = '1') then
      sig1 <= '0';
    end if;

    sig1 <= sig2(4 downto 0) when sig3 = 0 else
            sig1(2 downto 1);

    with expression select
        sig1 <= sig2 when 2,
                sig3 when 4;

    with expression select
        sig1 <= force sig2 when 2,
                sig3 when 4;

    sig1 <= force '0';

    sig1 <= release;

  end process PROC_NAME;

  -- This is a component that is brought in by a component declaration in the same file
  U_COMP1 : COMP1
  port map (
    SIG1 => sig1,
    SIG2 => sig2,
    SIG3 => sig3
  );

  -- This is a component that is brought in by a package
  U_COMP2 : COMP2
  port map (
    SIG3 => sig3,
    SIG4 => sig4,
    SIG5 => sig5
  );

  -- This is a component that is directly instantiated
  U_COMP3 : entity library.COMP3
  port map (
    SIG6 => sig6,
    SIG7 => sig7
  );

  sig1 <= '0';
  sig1 <= sig2 and sig3;
  sig1 <= sig2 and sig3;
  sig1 <= sig2 and
          sig3;
  sig1 <= sig2 and sig3;
  sig1 <= sig1 or sig1;

  sig1 <= sig2(4 downto 0);

  sig1 <= sig2(4 downto 0) when sig3 = 0 else
          sig1(2 downto 1);

  with expression select
      sig1 <= sig2 when 2,
              sig3 when 4;

end architecture RTL;
