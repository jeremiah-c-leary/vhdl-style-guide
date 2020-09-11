
architecture RTL of ENTITY_NAME is

begin

  process
  begin
  
    LABEL : report "This is a string"
      severity WARNING;
    
    report "This is a string"
      severity WARNING;
    
    LABEL : report "This is a string";

  end process;

end architecture;
