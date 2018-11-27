
architecture ARCH of ENTITY is

  -- Basic component
  component COMP1 is
    generic (
      generic_1 : std_logic := '0'; -- This should be removed
      generic_2 : std_logic := '1'
    );
    port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;-- This should be removed
      port_3 : inout std_logic;
      port_4 : out   std_logic; -- This should be removed
    );
  end component COMP1;

begin


  -- Basic component
  U_COMP1 : COMP1
    generic map (
      generic_1 => '0', -- This should be removed
      generic_2 => '1'
    )
    port map (
      port_1 => '0',
      port_2 => '1', -- This should be removed
      port_3 => '0',
      port_4 => '1'-- This should be removed
    );

end architecture ARCH;

