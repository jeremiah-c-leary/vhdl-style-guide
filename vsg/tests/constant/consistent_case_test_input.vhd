
architecture RTL of ENTITY1 is

  constant c_size  : integer := 5;
  constant c_ones  : std_logic_vector(C_SIZE - 1 downto 0) := (others => '1');
  constant c_zeros : std_logic_vector(c_size - 1 downto 0) := (others => '0');

  signal data : std_logic_vector(c_size - 1 downto 0);

begin

  data <= C_ONES;

  PROC_NAME : process () is
  begin

    data <= C_ones;

    if (sig2 = '0') then
      data <= c_Zeros;
    end if;

    if (sig2 = '1') then
      data <= c_ones;
    end if;

    if (sig3 = '1') then
      data <= c_zeros;
    end if;

  end process PROC_NAME;

end architecture RTL;
