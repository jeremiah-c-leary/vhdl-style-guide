
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

  PROC_NAME : process (siG2) is
  begin

    siG1 <= '0';

    if (SIG2 = '0') then
      sIg1 <= '1';
    elsif (SiG2 = '1') then
      SIg1 <= '0';
    end if;

  end process PROC_NAME;

  -- This is a component that is brought in by a component declaration in the same file
  U_COMP1 : COMP1
  port map (
    SIG1 => Sig1,
    SIG2 => SIg2,
    SIG3 => sig3
  );

  -- This is a component that is brought in by a package
  U_COMP2 : COMP2
  port map (
    SIG3 => Sig3,
    SIG4 => sig4,
    SIG5 => siG5
  );

  -- This is a component that is directly instantiated
  U_COMP3 : entity library.COMP3
  port map (
    SIG6 => siG6,
    SIG7 => sig7
  );

  Sig1 <= '0';
  sig1 <= sig2 and sig3;
  sig1 <= Sig2 and sig3;
  sig1 <= sig2 and 
          Sig3;
  SIG1 <= SIG2 and SIG3;
  SIG1 <= SIG1 or SIG1;


end architecture RTL;
