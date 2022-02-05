
architecture RTL of FIFO is

begin

  CASE_LABEL : case data generate

    when a = 1 =>

        signal          signal1 : std_logic;
        constant        con1    : std_logic;
        shared variable var1    : std_logic;
        alias           a       is name;
        alias           a       : subtype_indication is name;

      begin

    when b = 2 =>

        signal          sig1      : std_logic;
        constant        constant1 : std_logic;
        shared variable var1      : std_logic;
        alias           a         is name;
        alias           a         : subtype_indication is name;

      begin

    when c = 2 =>

        signal          sig1  : std_logic;
        constant        con1  : std_logic;
        shared variable vars1 : std_logic;
        alias           a     is name;
        alias           a     : subtype_indication is name;

      begin

  end generate;

  -- Violations below

  CASE_LABEL : case data generate

    when a = 1 =>

        signal          signal1: std_logic;
        constant        con1            : std_logic;
        shared variable var1       : std_logic;
        alias           a                 is name;
        alias           a : subtype_indication is name;

      begin

    when b = 2 =>

        signal          sig1                : std_logic;
        constant        constant1: std_logic;
        shared variable var1  : std_logic;
        alias           a                 is name;
        alias           a : subtype_indication is name;

      begin

    when c = 2 =>

        signal          sig1 : std_logic;
        constant        con1   : std_logic;
        shared variable vars1: std_logic;
        alias           a                 is name;
        alias           a : subtype_indication is name;

      begin

  end generate;

end;
