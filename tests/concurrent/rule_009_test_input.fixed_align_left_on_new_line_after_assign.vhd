
architecture rtl of fifo is

begin

  my_signal <= '1' when input = "00" else
               my_signal2 or my_sig3 when input = "01" else
               my_sig4 and my_sig5 when input = "10" else
               '0';

  my_signal <= '1' when input = "0000" else
               my_signal2 or my_sig3 when input = "0100" and input = "1100" else
               my_sig4 when input = "0010" else
               '0';

  my_signal <= '1' when input(1 downto 0) = "00" and func1(func2(G_VALUE1),
                   to_integer(cons1(37 downto 0))) = 256 else
               '0' when input(3 downto 0) = "0010" else
               'Z';

  my_signal <= '1' when input(1 downto
                   0) = "00" and func1(func2(G_VALUE1),
                     to_integer(cons1(37 downto 0))) = 256 else
               '0' when input(3 downto 0) = "0010" else
               'Z';

  my_signal <= '1' when a = "0000" and func1(345) or
                 b = "1000" and func2(567) and
                 c = "00" else
               sig1 when a = "1000" and func2(560) and
                 b = "0010" else
               '0';

  my_signal <= '1' when input(1 downto
                   0) = "00" and func1(func2(G_VALUE1),
                     to_integer(cons1(37 downto 0))) = 256 else
               my_signal when input(3 downto 0) = "0010" else
               'Z';

  -- Testing no code after assignment

  my_signal <=
    '1' when input(1 downto
        0) = "00" and func1(func2(G_VALUE1),
          to_integer(cons1(37 downto 0))) = 256 else
    my_signal when input(3 downto 0) = "0010" else
    'Z';

  my_signal <=
    (others => '0') when input(1 downto
        0) = "00" and func1(func2(G_VALUE1),
          to_integer(cons1(37 downto 0))) = 256 else
    my_signal when input(3 downto 0) = "0010" else
    'Z';

end architecture rtl;
