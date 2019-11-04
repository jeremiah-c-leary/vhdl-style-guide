

architecture ARCH of ENTITY is

  signal sig1, sig2, sig3,
     sig4, sig5, sig6, : std_logic;

  signal sig1, sig2,
     sig3,
     sig4,
     sig5,
     sig6
     : std_logic;


  -- Test variations of a single signal declaration

  signal sig1 : std_logic;

  signal sig1 : std_logic
    ;

  signal sig1 :
    std_logic
    ;

  signal sig1
    :
    std_logic
    ;

  signal
    sig1
    :
    std_logic
    ;

  -- Test variations of a two signal declarations

  signal sig1, sig2 : std_logic;

  signal sig1, sig2 : std_logic
    ;

  signal sig1, sig2 :
    std_logic
    ;

  signal sig1, sig2
    :
    std_logic
    ;

  signal sig1,
    sig2
    :
    std_logic
    ;

  signal sig1
    ,
    sig2
    :
    std_logic
    ;

  signal
    sig1
    ,
    sig2
    :
    std_logic
    ;


begin

end architecture ARCH;

