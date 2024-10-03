library ieee;
  use ieee.std_logic_1164.all;

entity test is
  generic (
    G1 : integer := 0;
    G2 : integer := 0
  );
  port (
    p1 : in    std_logic;
    p2 : out   std_logic
  );
end entity test;

architecture test of test is

  component test2 is
    generic (
      G1 : integer := 0;
      G2 : integer := 0
    );
    port (
      p1 : in    std_logic;
      p2 : out   std_logic
    );
  end component test2;

  signal s1 : std_logic;
  signal s2 : std_logic;

begin

  test2_i : component test2
    generic map (
      G1 => G1,
      G2 => G2
    )
    port map (
      p1 => p1,
      p2 => s1
    );

  test3_i : entity work.test3
    generic map (
      G1 => G1,
      G2 => G2
    )
    port map (
      p1 => p1,
      p2 => s2
    );

  p2 <= p1 when G1 = 0 and G2 = 0 else
        '0';

end architecture test;
