
entity ENTITY1 is
  generic (
    wait_generic : std_logic := '0'
  );
  port (
    wait_port : std_logic := '1'
  );
end entity ENTITY1;

architecture ARCH of ENTITY1 is

  signal wait_for_something : std_logic;

  component ENTITY2 is
    generic (
      wait_generic : std_logic := '0'
    );
    port (
      wait_port : std_logic := '1'
    );
  end component ENTITY2;


begin

  PROC1 : process (wait_for_something) is

    -- wait <-- this should not be classified as a wait
    variable wait_for_other_thing : std_logic;

  begin

    wait_label : wait for 10ns;
    wait_label : wait on a,b;
    wait_label : wait until a = '0';

  end process PROC1;

  U_ENTITY2 : ENTITY2
    generic map (
      wait_generic => '0'
    )
    port map (
      wait_port => '1'
    );

end architecture ARCH;
