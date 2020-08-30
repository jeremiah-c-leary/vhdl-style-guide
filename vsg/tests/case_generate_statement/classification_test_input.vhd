 
architecture RTL of FIFO is
   
begin

  LABEL0 : case a & b & c generate

    when "000" =>
  
    when "001" =>

  end generate LABEL0;


  -- Test nested case generates
  LABEL0 : case a & b & c generate

    when "000" =>

      LABEL1 : case a & b & c generate

        when "000" =>
      
        when "001" =>

      end generate LABEL1;
 
    when "001" =>

  end generate LABEL0;

  -- Test deeply nested case generates
  LABEL0 : case a & b & c generate

    when "000" =>

      LABEL1A : case a & b & c generate

        when "000" =>
      
          LABEL2A : case a & b & c generate

            when "000" =>
          
            when "001" =>

              LABEL2A : case a & b & c generate
    
                when "000" =>
              
                when "001" =>
    
              end generate LABEL2A;

          end generate LABEL2A;
 
        when "001" =>

      end generate LABEL1A;
 
    when "001" =>

      LABEL1B : case a & b & c generate

        when "000" =>
      
        when "001" =>

      end generate LABEL1B;
 
  end generate LABEL0;


end architecture RTL;
