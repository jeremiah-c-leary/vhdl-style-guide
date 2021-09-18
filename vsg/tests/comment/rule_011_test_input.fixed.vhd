-- This should be okay

architecture rtl of fifo is

 -- Comment
  signal a : std_logic;

  -- Okay comment
  signal b : std_logic_vector;

begin

 -- Comment 1
  a <= b;
 -- Comment 2
  c <= d;
 -- Comment 3
  e <= f;

 -- BQ1/M3S1
  rx_tdata_remapped <= rx_tdata(119 downto 112) & rx_tdata(127 downto 120) &
     -- BI1/M2S1
                       rx_tdata(87 downto 80) & rx_tdata(95 downto 88) &
  -- BQ0/M3S0
                       rx_tdata(103 downto 96) & rx_tdata(111 downto 104) &
     -- BQ0/M2S0
                       rx_tdata(71 downto 64) & rx_tdata(79 downto 72) &
     -- AQ1/M1S1
                       rx_tdata(55 downto 48) & rx_tdata(63 downto 56) &
     -- AI1/M0S1
                       rx_tdata(23 downto 16) & rx_tdata(31 downto 24) &
     -- AQ0/M1S0
                       rx_tdata(39 downto 32) & rx_tdata(47 downto 40) &
         -- AI0/M0S0
                       rx_tdata(7 downto 0) & rx_tdata(15 downto 8);

end architecture rtl;
