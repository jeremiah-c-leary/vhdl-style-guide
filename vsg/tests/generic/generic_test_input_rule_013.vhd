
entity ENTITY1 is
  generic (G_GEN_1 : std_logic_vector(6 downto 0);
    G_GEN_2 : std_logic_vector(8 downto 1)
  );
  port (PORT_1 : in std_logic_vector(12 downto 0);
    PORT_2 : out std_logic_vector(0 to 25)
  );
end entity ENTITY1;

