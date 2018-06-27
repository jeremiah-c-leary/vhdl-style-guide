----------------------------------------------------------------------
----                                                              ----
----  iteration_synth.vhd                                         ----
----                                                              ----
----  This file is part of the turbo decoder IP core project      ----
----  http://www.opencores.org/projects/turbocodes/               ----
----                                                              ----
----  Author(s):                                                  ----
----      - David Brochart(dbrochart@opencores.org)               ----
----                                                              ----
----  All additional information is available in the README.txt   ----
----  file.                                                       ----
----                                                              ----
----------------------------------------------------------------------
----                                                              ----
---- Copyright (C) 2005 Authors                                   ----
----                                                              ----
---- This source file may be used and distributed without         ----
---- restriction provided that this copyright statement is not    ----
---- removed from the file and that any derivative work contains  ----
---- the original copyright notice and the associated disclaimer. ----
----                                                              ----
---- This source file is free software; you can redistribute it   ----
---- and/or modify it under the terms of the GNU Lesser General   ----
---- Public License as published by the Free Software Foundation; ----
---- either version 2.1 of the License, or (at your option) any   ----
---- later version.                                               ----
----                                                              ----
---- This source is distributed in the hope that it will be       ----
---- useful, but WITHOUT ANY WARRANTY; without even the implied   ----
---- warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR      ----
---- PURPOSE. See the GNU Lesser General Public License for more  ----
---- details.                                                     ----
----                                                              ----
---- You should have received a copy of the GNU Lesser General    ----
---- Public License along with this source; if not, download it   ----
---- from http://www.opencores.org/lgpl.shtml                     ----
----                                                              ----
----------------------------------------------------------------------



architecture SYNTH of ITERATION is

  signal zout1         : ARRAY4c;
  signal zout2         : ARRAY4c;
  signal zout1perm     : ARRAY4c;
  signal zoutint1      : ARRAY4c;
  signal zout2int      : ARRAY4c;
  signal tmp0          : std_logic_vector(Z_WIDTH * 4 + SIG_WIDTH * 2 - 1 downto 0);
  signal tmp1          : std_logic_vector(Z_WIDTH * 4 + SIG_WIDTH * 2 - 1 downto 0);
  signal tmp2          : std_logic_vector(SIG_WIDTH * 6 - 1 downto 0);
  signal tmp3          : std_logic_vector(SIG_WIDTH * 6 - 1 downto 0);
  signal tmp4          : std_logic_vector(SIG_WIDTH * 4 - 1 downto 0);
  signal tmp5          : std_logic_vector(SIG_WIDTH * 4 - 1 downto 0);
  signal tmp6          : std_logic_vector(Z_WIDTH * 4 - 1 downto 0);
  signal tmp7          : std_logic_vector(Z_WIDTH * 4 - 1 downto 0);
  signal tmp8          : std_logic_vector(SIG_WIDTH * 6 - 1 downto 0);
  signal tmp9          : std_logic_vector(SIG_WIDTH * 6 - 1 downto 0);
  signal tmp10         : std_logic_vector(SIG_WIDTH * 8 - 1 downto 0);
  signal tmp11         : std_logic_vector(SIG_WIDTH * 8 - 1 downto 0);
  signal abdel1perm    : ARRAY2a;
  signal abdel1permint : ARRAY2a;
  signal adel1         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal bdel1         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal ydel1         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal wdel1         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal yintdel1      : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal wintdel1      : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal adel2         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal bdel2         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal ydel2         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal wdel2         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal adecint       : std_logic;
  signal bdecint       : std_logic;
  signal adel3         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal bdel3         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal ydel3         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal wdel3         : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal yintdel3      : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal wintdel3      : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal yintdel4      : std_logic_vector(SIG_WIDTH - 1 downto 0);
  signal wintdel4      : std_logic_vector(SIG_WIDTH - 1 downto 0);

begin

  SOVA_I0 : SOVA
    port map (
      CLK     => clk,
      RST     => rst,
      ANOISY  => a,
      BNOISY  => b,
      YNOISY  => y,
      WNOISY  => w,
      ZIN     => zin,
      ZOUT    => zout1,
      ACLEAN  => aDec,
      BCLEAN  => bDec
    );

  ZPERMUT_I0 : ZPERMUT
    generic map (
      FLIP        => (TREL1_LEN + TREL2_LEN + 2 + delay + 1) mod 2
    )
    port map (
      FLIPFLOP    => flipflop,
      Z           => zout1,
      ZPERM       => zout1Perm
    );

  tmp0 <= zout1Perm(0) & zout1Perm(1) & zout1Perm(2) & zout1Perm(3) & abDel1Perm(0) & abDel1Perm(1);

  INTERLEAVER_I0 : INTERLEAVER
    generic map (
      DELAY       => TREL1_LEN + TREL2_LEN + 2 + delay,
      WAY         => 0
    )
    port map (
      CLK         => clk,
      RST         => rst,
      D           => tmp0,
      Q           => tmp1
    );

  zoutInt1(0)         <= tmp1(Z_WIDTH * 4 + SIG_WIDTH * 2 - 1 downto Z_WIDTH * 3 + SIG_WIDTH * 2);
  zoutInt1(1)         <= tmp1(Z_WIDTH * 3 + SIG_WIDTH * 2 - 1 downto Z_WIDTH * 2 + SIG_WIDTH * 2);
  zoutInt1(2)         <= tmp1(Z_WIDTH * 2 + SIG_WIDTH * 2 - 1 downto Z_WIDTH * 1 + SIG_WIDTH * 2);
  zoutInt1(3)         <= tmp1(Z_WIDTH * 1 + SIG_WIDTH * 2 - 1 downto Z_WIDTH * 0 + SIG_WIDTH * 2);
  abDel1PermInt(0)    <= tmp1(SIG_WIDTH * 2 - 1 downto SIG_WIDTH * 1);
  abDel1PermInt(1)    <= tmp1(SIG_WIDTH * 1 - 1 downto SIG_WIDTH * 0);

  tmp2 <= a & b & y & w & yInt & wInt;

  DELAYER_I0 : DELAYER
    generic map (
      DELAY   => TREL1_LEN + TREL2_LEN
    )
    port map (
      CLK     => clk,
      RST     => rst,
      D       => tmp2,
      Q       => tmp3
    );

  aDel1       <= tmp3(SIG_WIDTH * 6 - 1 downto SIG_WIDTH * 5);
  bDel1       <= tmp3(SIG_WIDTH * 5 - 1 downto SIG_WIDTH * 4);
  yDel1       <= tmp3(SIG_WIDTH * 4 - 1 downto SIG_WIDTH * 3);
  wDel1       <= tmp3(SIG_WIDTH * 3 - 1 downto SIG_WIDTH * 2);
  yIntDel1    <= tmp3(SIG_WIDTH * 2 - 1 downto SIG_WIDTH * 1);
  wIntDel1    <= tmp3(SIG_WIDTH * 1 - 1 downto SIG_WIDTH * 0);

  ABPERMUT_I0 : ABPERMUT
    generic map (
      FLIP        => (TREL1_LEN + TREL2_LEN + 2 + delay + 1) mod 2
    )
    port map (
      FLIPFLOP    => flipflop,
      A           => aDel1,
      B           => bDel1,
      ABPERM      => abDel1Perm
    );

  tmp4 <= aDel1 & bDel1 & yDel1 & wDel1;

  DELAYER_I1 : DELAYER
    generic map (
      DELAY   => FRSIZE
    )
    port map (
      CLK     => clk,
      RST     => rst,
      D       => tmp4,
      Q       => tmp5
    );

  aDel2   <= tmp5(SIG_WIDTH * 4 - 1 downto SIG_WIDTH * 3);
  bDel2   <= tmp5(SIG_WIDTH * 3 - 1 downto SIG_WIDTH * 2);
  yDel2   <= tmp5(SIG_WIDTH * 2 - 1 downto SIG_WIDTH * 1);
  wDel2   <= tmp5(SIG_WIDTH * 1 - 1 downto SIG_WIDTH * 0);

  SOVA_I1 : SOVA
    port map (
      CLK     => clk,
      RST     => rst,
      ANOISY  => abDel1PermInt(1),
      BNOISY  => abDel1PermInt(0),
      YNOISY  => yIntDel1,
      WNOISY  => wIntDel1,
      ZIN     => zoutInt1,
      ZOUT    => zout2,
      ACLEAN  => aDecInt,
      BCLEAN  => bDecInt
    );

  tmp6 <= zout2(0) & zout2(1) & zout2(2) & zout2(3);

  DEINTERLEAVER_I0 : INTERLEAVER
    generic map (
      DELAY       => 2 * (TREL1_LEN + TREL2_LEN + 2) + FRSIZE + delay,
      WAY         => 1
    )
    port map (
      CLK         => clk,
      RST         => rst,
      D           => tmp6,
      Q           => tmp7
    );

  zout2Int(0) <= tmp7(Z_WIDTH * 4 - 1 downto Z_WIDTH * 3);
  zout2Int(1) <= tmp7(Z_WIDTH * 3 - 1 downto Z_WIDTH * 2);
  zout2Int(2) <= tmp7(Z_WIDTH * 2 - 1 downto Z_WIDTH * 1);
  zout2Int(3) <= tmp7(Z_WIDTH * 1 - 1 downto Z_WIDTH * 0);

  ZPERMUT_I1 : ZPERMUT
    generic map (
      FLIP        => (2 * (TREL1_LEN + TREL2_LEN + 2) + FRSIZE + delay) mod 2
    )
    port map (
      FLIPFLOP    => flipflop,
      Z           => zout2Int,
      ZPERM       => zout
    );

  tmp8 <= aDel2 & bDel2 & yDel2 & wDel2 & yIntDel1 & wIntDel1;

  DELAYER_I2 : DELAYER
    generic map (
      DELAY   => TREL1_LEN + TREL2_LEN
    )
    port map (
      CLK     => clk,
      RST     => rst,
      D       => tmp8,
      Q       => tmp9
    );

  aDel3       <= tmp9(SIG_WIDTH * 6 - 1 downto SIG_WIDTH * 5);
  bDel3       <= tmp9(SIG_WIDTH * 5 - 1 downto SIG_WIDTH * 4);
  yDel3       <= tmp9(SIG_WIDTH * 4 - 1 downto SIG_WIDTH * 3);
  wDel3       <= tmp9(SIG_WIDTH * 3 - 1 downto SIG_WIDTH * 2);
  yIntDel3    <= tmp9(SIG_WIDTH * 2 - 1 downto SIG_WIDTH * 1);
  wIntDel3    <= tmp9(SIG_WIDTH * 1 - 1 downto SIG_WIDTH * 0);

  tmp10 <= aDel3 & bDel3 & yDel3 & wDel3 & yIntDel3 & wIntDel3 & yIntDel4 & wIntDel4;

  DELAYER_I3 : DELAYER
    generic map (
      DELAY   => FRSIZE
    )
    port map (
      CLK     => clk,
      RST     => rst,
      D       => tmp10,
      Q       => tmp11
    );

  aDel        <= tmp11(SIG_WIDTH * 8 - 1 downto SIG_WIDTH * 7);
  bDel        <= tmp11(SIG_WIDTH * 7 - 1 downto SIG_WIDTH * 6);
  yDel        <= tmp11(SIG_WIDTH * 6 - 1 downto SIG_WIDTH * 5);
  wDel        <= tmp11(SIG_WIDTH * 5 - 1 downto SIG_WIDTH * 4);
  yIntDel4    <= tmp11(SIG_WIDTH * 4 - 1 downto SIG_WIDTH * 3);
  wIntDel4    <= tmp11(SIG_WIDTH * 3 - 1 downto SIG_WIDTH * 2);
  yIntDel     <= tmp11(SIG_WIDTH * 2 - 1 downto SIG_WIDTH * 1);
  wIntDel     <= tmp11(SIG_WIDTH * 1 - 1 downto SIG_WIDTH * 0);

end architecture;
