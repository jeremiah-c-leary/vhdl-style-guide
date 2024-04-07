
-- Nothing should fail in this entity
entity ENT1 is
  generic (
    G_GENERIC1 : std_logic_vector(3 downto 0);
    G_GENERIC2 : std_logic_vector(0 TO 256)
  );
  port (
    P_PORT1 : std_logic_vector(15 downto 6); -- DOWNTO
    P_PORT2 : std_logic_vector(56 TO 132)
  );
end entity ENT1;

-- Everything should fail in this entity
entity ENT1 is
  generic (
    G_GENERIC1 : std_logic_vector(3 downTo 0);
    G_GENERIC2 : std_logic_vector(0 TO 256)
  );
  port (
    P_PORT1 : std_logic_vector(15 Downto 6);
    P_PORT2 : std_logic_vector(56 TO 132)
  );
end entity ENT1;

architecture ARCH of ENT1 is

  constant c_const1 : std_logic_vector(3 DOWNTO 0);  -- downto
  constant c_const2 : std_logic_vector(3 downto 0);
  constant c_const3 : std_logic_vector(345 TO 670);
  constant c_const4 : std_logic_vector(345 TO 670);

  signal w_sig1 : std_logic_vector(50 dOWnto 45);
  signal w_sig2 : std_logic_vector(50 downto 45);
  signal w_sig3 : std_logic_vector(46 TO 345);
  signal w_sig4 : std_logic_vector(46 TO 345);

begin

end architecture ARCH;
