
architecture ARCH of ENTITY1 is

begin

  my_cmp : component cmp
    port map (
      clk   => clk,
      reset => reset
    );

  x : block is
    port (
      p1 : inout bit;
      p2 : inout bit
    );
    port map (
      p1 => a,
      p2 => b
    );
  begin
  end block x;

  -- Violations below

  my_cmp : component cmp
    port map (
          clk   => clk,
  reset => reset
    );

  x : block is
    port (
      p1 : inout bit;
      p2 : inout bit
    );
    port map (
p1 => a,
        p2 => b
    );
  begin
  end block x;

end architecture ARCH;
