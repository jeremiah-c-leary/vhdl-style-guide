
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

entity test is
  generic (
    G1 : integer := 0;
    g2 : integer := 0
  );
  port (
    P1 : in  std_logic;
    P2 : out std_logic
  );
end entity test;

architecture rtl of test is

  component test2 is
    generic (
      G1 : integer := 0;
      g2 : integer := 0
    );
    port (
      P1 : in    std_logic;
      p2 : out   std_logic
    );
  end component test2;

begin

  test2_i : component test2
    generic map (
      G1 => G1,
      g2 => G2
    )
    port map (
      P1 => P1,
      P2 => P2
    );

  test3_lower : entity work.test3
    generic map (
      g1 => G1,
      g2 => G2
    )
    port map (
      p1 => p1,
      p2 => p2
    );

  test3_upper : entity work.test3
    generic map (
      G1 => g1,
      G2 => g2
    )
    port map (
      p1 => p1,
      p2 => p2
    );

end architecture;

-- Testing case where entity name is not detected
architecture beh of test3 is

begin

end architecture beh;
