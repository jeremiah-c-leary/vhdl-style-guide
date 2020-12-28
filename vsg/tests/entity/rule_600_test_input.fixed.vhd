
entity FIFO is
  generic (
    G_WIDTH : natural := 16
  );
  port (
    I_DATA : in std_logic_vector(G_WIDTH - 1 downto 0);
    O_DATA : in std_logic_vector(G_WIDTH - 1 downto 0)
  );
end entity;
