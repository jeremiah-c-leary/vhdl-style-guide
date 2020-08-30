
entity BLOCK_EXAMPLE is
end entity BLOCK_EXAMPLE;

architecture RTL of BLOCK_EXAMPLE is

begin

  BLK : block is
  begin

    GEN : for ii in 0 to 7 generate

      BLK2 : block is
      begin

        GEN2 : for jj in 0 to 7 generate

        end generate GEN2; 

      end block BLK2;

    end generate GEN;

  end block BLK;


  BLK : block is
  begin

    IF_GEN_LABEL: if a = x generate

        BLK2 : block is
        begin
  
            GEN2 : for jj in 0 to 7 generate
    
                BLK3: block is
                begin
          
                end block BLK3;
  
            end generate GEN2; 

            BLK4 : block is
            begin

              CASE_GEN_LABEL : case a & B & c generate

                when "000" =>
                    BLK4A : block is
                    begin
                    end block BLK4A;
                when "001" =>

                  IF_GEN_LABELA: if a = y generate

                    BLK4B : block is
                    begin
                    end block BLK4B;

                  end generate IF_GEN_LABELA;     

               end generate CASE_GEN_LABEL;
      
            end block BLK4;
      
            BLK5 : block is
            begin

            end block BLK5;

        end block BLK2;

    end generate IF_GEN_LABEL;

    GEN : for ii in 0 to 7 generate

        GEN2 : for jj in 0 to 7 generate

          IF_GEN_LABEL2 : if b = y generate

            BLK2 : block is
            begin
      
            end block BLK2;
   
          elsif x = z generate
 
            BLK2 : block is
            begin
      
          end block BLK2;

        end generate IF_GEN_LABEL2;

        end generate GEN2;
    end generate GEN;

  end block BLK;

end architecture RTL;
