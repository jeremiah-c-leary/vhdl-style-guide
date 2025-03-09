
architecture RTL of FIFO is

  alias ident : std_logic_vector(3 downto 0) is write_enable [name1, name2 return integer];

  alias ident : std_logic_vector(3 downto 0) is write_enable [name1, name2];

  alias ident : std_logic_vector(3 downto 0) is write_enable [return integer];

  alias ident : std_logic_vector(3 downto 0) is write_enable(15 downto 0);


  alias ident is write_enable [name1, name2 return integer];

  alias ident is write_enable [name1, name2];

  alias ident is write_enable [return integer];

  alias ident is write_enable;

  alias alias_sop : std_logic is << signal .tb_top.submodule.i_rx_data : t_mac_interface >> .sop;

begin

end architecture RTL;
