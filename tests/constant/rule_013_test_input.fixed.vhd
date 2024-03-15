
architecture RTL of ENTITY1 is

  constant c_size  : integer := 5;
  constant c_ones  : std_logic_vector(c_size - 1 downto 0) := (others => '1');
  constant c_zeros : std_logic_vector(c_size - 1 downto 0) := (others => '0');

  signal data : std_logic_vector(c_size - 1 downto 0);

begin

  data <= c_ones;

  PROC_NAME : process () is
  begin

    data <= c_ones & c_zeros;

    if (sig2 = '0') then
      data <= c_zeros;
    end if;

    if (sig2 = '1') then
      data <= c_ones;
    end if;

    if (sig3 = '1') then
      data <= c_zeros;
    end if;

  end process PROC_NAME;

end architecture RTL;
