
entity ADDER_TREE is
  generic (
    IN_WIDTH  : integer := 14;
    OUT_WIDTH : integer := 15
  );
  port (
    Q : out   std_logic_vector((OUT_WIDTH - 1) downto 0)
  );
end entity ADDER_TREE;
