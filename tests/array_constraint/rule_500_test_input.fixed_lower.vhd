
architecture rtl of fifo is

  subtype t_my_array is t_array(open)(t_range);

begin

  cmp : entity work.my_component
    port map (
      clk   => open,
      reset => reset
    );

end architecture rtl;

--====== UPPERCASE before


architecture rtl of fifo is

  subtype t_my_array is t_array(open)(t_range);

begin

  cmp : entity work.my_component
    port map (
      clk   => OPEN,
      reset => reset
    );

end architecture rtl;
