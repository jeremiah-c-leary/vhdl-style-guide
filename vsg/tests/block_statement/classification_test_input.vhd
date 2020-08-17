
entity BLOCK_EXAMPLE is
end entity BLOCK_EXAMPLE;

architecture RTL of BLOCK_EXAMPLE is

begin

  -- correct block format
  BLK : block is







  begin


    BLK2 : block is
    begin


        BLK3 : block is
        begin
    
    
        a <= b; 
    
        end block BLK3;
    
    
    end block BLK2;


    BLK4 : block is
    begin


        BLK5 : block is
        begin

        a <= b when c = 1 else
             d when e = 2 else
             f; 
    
            BLK6 : block is

            begin
        
                PROC_LABEL : process (a, b, c) is
                begin
                   ASSERT_LABEL : assert FALSE report "blah" severity WARNING;
                end process PROC_LABEL;
                    
        
                assert TRUE report "blah" severity FATAL;
        
            end block BLK6;
    
    
    
        end block BLK5;
    
    
    end block BLK4;

    assert TRUE report "blah" severity FATAL;

  end block BLK;

end architecture RTL;

