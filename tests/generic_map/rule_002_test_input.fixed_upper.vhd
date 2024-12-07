
package my_pkg_g is new my_pkg
  generic map (
    G_GEN_1(3 downto 0) => 3,
    G_GEN_2(2 downto 1) => 4,
    G_GEN_3 => 5
  );

architecture rtl of test is

function my_func is new my_func
  generic map (
    G_GEN_1(3 downto 0) => 3,
    G_GEN_2(2 downto 1) => 4,
    G_GEN_3 => 5
  );

begin

  u_inst1 : inst1
    generic map (
      G_GEN_1(3 downto 0) => 3,
      G_GEN_2(2 downto 1) => 4,
      G_GEN_3 => 5
    )
    port map (
      port_1(3 downto 0) => w_port_1,
      port_2 => w_port_2,
      port_3(2 downto 1) => w_port_3
    );

  my_block : block is

    generic (
      g_test : boolean
    );
    generic map (
      G_GEN_1(3 downto 0) => 3,
      G_GEN_2(2 downto 1) => 4,
      G_GEN_3 => 5
    );

  begin

  end block my_block;

end architecture rtl;

  -- Violations below

PACKAGE MY_PKG_G IS NEW MY_PKG
  GENERIC MAP (
    G_GEN_1(3 DOWNTO 0) => 3,
    G_GEN_2(2 DOWNTO 1) => 4,
    G_GEN_3 => 5
  );

ARCHITECTURE RTL OF TEST IS

FUNCTION MY_FUNC IS NEW MY_FUNC
  GENERIC MAP (
    G_GEN_1(3 DOWNTO 0) => 3,
    G_GEN_2(2 DOWNTO 1) => 4,
    G_GEN_3 => 5
  );

BEGIN

  U_INST1 : INST1
    GENERIC MAP (
      G_GEN_1(3 DOWNTO 0) => 3,
      G_GEN_2(2 DOWNTO 1) => 4,
      G_GEN_3 => 5
    )
    PORT MAP (
      PORT_1(3 DOWNTO 0) => W_PORT_1,
      PORT_2 => W_PORT_2,
      PORT_3(2 DOWNTO 1) => W_PORT_3
    );

  MY_BLOCK : BLOCK IS

    GENERIC (
      G_TEST : BOOLEAN
    );
    GENERIC MAP (
      G_GEN_1(3 DOWNTO 0) => 3,
      G_GEN_2(2 DOWNTO 1) => 4,
      G_GEN_3 => 5
    );

  BEGIN

  END BLOCK MY_BLOCK;

END ARCHITECTURE RTL;
