
architecture RTL of FIFO is

  alias ident : std_logic_vector(3 downto 0) is write_enable [name1, name2 return integer];

  alias ident : std_logic_vector(3 downto 0) is write_enable [name1, name2];

  alias ident : std_logic_vector(3 downto 0) is write_enable [return integer];

  alias ident : std_logic_vector(3 downto 0) is write_enable(15 downto 0);


  alias ident is write_enable [name1, name2 return integer];

  alias ident is write_enable [name1, name2];

  alias ident is write_enable [return integer];

  alias ident is write_enable;

  alias s_event_count : natural range 0 to 2**16 - 1 is << signal some.reference.some_signal : natural range 0 to 2**16 - 1 >>;

  alias opposite_view is some_view'converse;

begin

end architecture RTL;
