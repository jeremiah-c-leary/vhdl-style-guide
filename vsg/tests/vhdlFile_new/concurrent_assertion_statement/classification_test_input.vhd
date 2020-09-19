
architecture RTL of FIFO is

begin

  LABEL : assert TRUE
    report "This is a string"
    severity WARNING;
  
  assert TRUE
    report "This is a string"
    severity WARNING;
  
  LABEL : assert TRUE
    report "This is a string";
  
  LABEL : assert TRUE
    severity WARNING;

  postponed assert TRUE
    report "This is a string";
    
  LABEL : postponed assert TRUE
    report "This is a string";

end architecture RTL;
