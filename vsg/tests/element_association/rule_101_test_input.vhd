
architecture rtl of fifo is

begin

  a <= (others => (others => '0'));

  process begin

    a <= (others => (others => '0'));

  end process;

end architecture;


architecture rtl of fifo is

begin

  a <= (others =>(others =>    '0'));

  process begin

    a <= (others =>    (others =>'0'));

  end process;

end architecture;
