
architecture rtl of test is

begin

  cmp_g_test : component test
    port map (
      clk   => clk,
      reset => reset
    );

  cmp_g_test : entity work.test
    port map (
      clk   => clk,
      reset => reset
    );

  -- Violations below

  cmp_g_test : component test
    port map (
      clk   => clk,
      reset => reset
    );

  cmp_g_test : entity work.test
    port map (
      clk   => clk,
      reset => reset
    );

end architecture rtl;
