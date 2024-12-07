
architecture ARCH of ENTITY1 is

  function my_func is new my_func
    generic map (
      g_test => c_test
    );

  function my_func is new my_func
    generic map (
      g_test => c_test
    );

  function my_func is new my_func
    generic map (
      g_test => c_test
    );

  function my_func is new my_func
    generic map (
      g_test => c_test
    );

begin

  U_INST1 : INST1
    generic map (
      G_GEN_1 => 3,
      G_GEN_2 => 4,
      G_GEN_3 => 5
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
    generic map (
      G_GEN_1 => 1,
      G_GEN_2 => 2,
      G_GEN_3 => 3
    );

  U_INST1 : INST1
    generic map (
      G_GEN_1 => 1,
      G_GEN_2 => 2,
      G_GEN_3 => 3
    );

  U_INST1 : INST1
    generic map (
      G_GEN_1 => 1,
      G_GEN_2 => 2,
      G_GEN_3 => 3
    );

  my_block : block is
    GENERIC (
      g_test : BOOLEAN
    );
    generic map (
      g_test => C_TEST
    );
  begin
  end block;

  my_block : block is
    GENERIC (
      g_test : BOOLEAN
    );
    generic map (
      g_test => C_TEST
    );
  begin
  end block;

  my_block : block is
    GENERIC (
      g_test : BOOLEAN
    );
    generic map (
      g_test => C_TEST
    );
  begin
  end block;

  my_block : block is
    GENERIC (
      g_test : BOOLEAN
    );
    generic map (
      g_test => C_TEST
    );
  begin
  end block;

end architecture ARCH;

package my_pkg_g is new my_pkg
  generic map (
    g_test => c_test
  );

package my_pkg_g is new my_pkg
  generic map (
    g_test => c_test
  );

package my_pkg_g is new my_pkg
  generic map (
    g_test => c_test
  );

package my_pkg_g is new my_pkg
  generic map (
    g_test => c_test
  );
