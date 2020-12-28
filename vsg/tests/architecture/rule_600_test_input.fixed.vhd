
entity FIFO is
  generic (
    G_WIDTH : natural := 16
  );
end entity;

architecture rtl of fifo is

  signal w_data : std_logic_vector(G_WIDTH - 1 dowtno 0);

begin

  output <= large_data(G_WIDTH - 1 downto 0);

end architecture rtl;
