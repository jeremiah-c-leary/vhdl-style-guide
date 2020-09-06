
entity FIFO is

  begin
    
    LABEL : assert TRUE
      report "This is a string"
      severity WARNING;
  
    LABEL1: postponed Proc1 (Clock);
    LABEL2 : postponed READ (L     => BufLine,
                   VALUE => Q);

    process_and_or : postponed process(a,b,d,e) is

    begin

    end postponed process process_and_or;


end entity FIFO;
