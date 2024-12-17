
package my_pkg_g is new my_pkg
  generic map (
    g_test1 => c_test1,
    g_test2 => c_test2
  );

architecture rtl of test is

  function my_func is new my_func
    generic map (
      g_test1 => c_test1,
      g_test2 => c_test2
    );

begin

  cmp_g_test : component test
    generic map (
      g_test1 => c_test1,
      g_test2 => c_test2
    );

  my_block : block is

    generic (
      g_test1 : boolean;
      g_test2 : boolean
    );
    generic map (
      g_test1 => c_test1,
      g_test2 => c_test2
    );

  begin

  end block my_block;

end architecture rtl;

-- Violations below

package my_pkg_g is new my_pkg
  generic map (
    g_test1 => c_test1,
    g_test2 => c_test2
);

architecture rtl of test is

  function my_func is new my_func
    generic map (
      g_test1 => c_test1,
      g_test2 => c_test2
        );

begin

  cmp_g_test : component test
    generic map (
      g_test1 => c_test1,
      g_test2 => c_test2
  );

  my_block : block is

    generic (
      g_test1 : boolean;
      g_test2 : boolean
    );
    generic map (
      g_test1 => c_test1,
      g_test2 => c_test2
              );

  begin

  end block my_block;

end architecture rtl;
