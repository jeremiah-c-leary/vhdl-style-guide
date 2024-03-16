
entity FIFO is
  generic (
    G_WIDTH : natural := 16;
    g_depth : natural := 4
  );
end entity;

entity FIFO2 is
  generic (
    g_width : natural := 16;
    G_DEPTH : natural := 4
  );
end entity;

architecture rtl of fifo is

  signal w_data : std_logic_vector(g_width - 1 downto 0);
  signal w_data : std_logic_vector(G_WIDTH - 1 downto 0);
  signal w_depth : std_logic_vector(G_DEPTH - 1 downto 0);
  signal w_depth : std_logic_vector(g_depth - 1 downto 0);

begin

  output <= large_data(g_width - 1 downto 0);
  output <= large_data(G_WIDTH - 1 downto 0);
  output <= large_data(G_DEPTH - 1 downto 0);
  output <= large_data(g_depth - 1 downto 0);

end architecture rtl;

architecture rtl2 of fifo is

  signal w_data : std_logic_vector(g_width - 1 downto 0);
  signal w_data : std_logic_vector(G_WIDTH - 1 downto 0);
  signal w_depth : std_logic_vector(G_DEPTH - 1 downto 0);
  signal w_depth : std_logic_vector(g_depth - 1 downto 0);

begin

  output <= large_data(g_width - 1 downto 0);
  output <= large_data(G_WIDTH - 1 downto 0);
  output <= large_data(G_DEPTH - 1 downto 0);
  output <= large_data(g_depth - 1 downto 0);

end architecture rtl;

architecture rtl of fifo2 is

  signal w_data : std_logic_vector(G_WIDTH - 1 downto 0);
  signal w_data : std_logic_vector(g_width - 1 downto 0);
  signal w_depth : std_logic_vector(g_depth - 1 downto 0);
  signal w_depth : std_logic_vector(G_DEPTH - 1 downto 0);

begin

  output <= large_data(G_WIDTH - 1 downto 0);
  output <= large_data(g_width - 1 downto 0);
  output <= large_data(g_depth - 1 downto 0);
  output <= large_data(G_DEPTH - 1 downto 0);

end architecture rtl;
