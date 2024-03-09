
architecture RTL of FIFO is

begin

  FOR_LABEL : for i in 0 to 7 generate

    signal          sig1 : std_logic;
    constant        con1 : std_logic;
    -- Comment
    shared variable var1 : std_logic;
    alias           a    is name;

    alias a    : subtype_indication is name;

  begin

  end generate;

  IF_LABEL : if a = '1' generate

    signal               sig1 : std_logic;
    constant   con1 : std_logic;
    -- Comment
    shared variable                var1 : std_logic;
    alias    a    is name;

    alias     a    : subtype_indication is name;

    begin

  elsif a = '0' generate

    signal  sig1 : std_logic;
    constant        con1 : std_logic;
    -- Comment
    shared variable        var1 : std_logic;
    alias             a    is name;

    alias    a    : subtype_indication is name;

    begin

  else generate

    signal       sig1 : std_logic;
    constant con1 : std_logic;
    -- Comment
    shared variable var1 : std_logic;
    alias    a    is name;

    alias a    : subtype_indication is name;

  begin

  end generate;

  CASE_LABEL : case data generate

    when a = 1 =>

        signal       sig1 : std_logic;
        constant   con1 : std_logic;
        -- Comment
        shared variable       var1 : std_logic;
        alias    a    is name;

        alias      a    : subtype_indication is name;

    begin

    when a = 0 =>

        signal       sig1 : std_logic;
        constant  con1 : std_logic;
        -- Comment
        shared variable var1 : std_logic;
        alias        a    is name;

        alias a    : subtype_indication is name;

  begin

  end generate;

end;
