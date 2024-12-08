
architecture RTL of FIFO is

begin

  BLOCK_LABEL : block is

    signal sig1   : std_logic;
    constant con1 : std_logic := '0';
    file file1    : std_logic;
    alias alias1  : subtype_indicator is name;
    alias alias1  is name;

    -- Checking exclusions
    constant c_abc : integer;
    function my_func return integer is
      constant c_abc : integer;
    begin
    end function;
    constant c_abc : integer;
    type flag_pt is protected body
      variable flag : boolean;
    end protected body;

  begin
  end block BLOCK_LABEL;

end architecture RTL;
