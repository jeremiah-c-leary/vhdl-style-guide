
entity FIFO is

  generic (
    G_GEN1 : integer;
    G_GEN2 : std_logic;
    G_GENA : t_user2;
    G_GEN3 : std_logic_vector(3 downto 0);
    G_GEN4 : signed(15 downto 0);
    G_GEN5 : unsigned(7 downto 0);
    G_GEN6 : std_ulogic;
    G_GEN7 : t_user1
  );

end entity FIFO;


-- Violation below

entity FIFO is

  generic (
    G_GEN1 : INTEGER;
    G_GEN2 : STD_LOGIC;
    G_GENA : T_USER2;
    G_GEN3 : STD_LOGIC_VECTOR(3 downto 0);
    G_GEN4 : SIGNED(15 downto 0);
    G_GEN5 : UNSIGNED(7 downto 0);
    G_GEN6 : STD_ULOGIC;
    G_GEN7 : T_USER1
  );

end entity FIFO;

