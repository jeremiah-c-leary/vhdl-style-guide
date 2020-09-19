
entity some_entity is
  port (
    I_INPUT : in T_CUSTOM_ARRAY(G_A'high downto 0)(function_call(G_B, G_C)-1 downto 0) := (others => (others => '0')); -- This should be untouched
    I_INPUT, I_INPUT2 : in T_CUSTOM_ARRAY(G_A'high downto 0)(function_call(G_B, G_C)-1 downto 0) := (others => (others => '0')); -- This should result in two lines
    I_INPUT, I_INPUT2, I_INPUT3 : in T_CUSTOM_ARRAY(G_A'high downto 0)(function_call(G_B, G_C)-1 downto 0) := (others => (others => '0')) -- This should result in three lines
  );
end entity some_entity;
