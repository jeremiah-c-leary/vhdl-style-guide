 
architecture RTL of FIFO is
   
begin
   
  -- Demonstrates Use Case #1: Replicating Logic
  -- Stores just the most significant byte in a new signal
  LABEL1: for i in 0 to 7 generate

  end generate LABEL1;

  -- Test nesting
  LABEL2A: for i in 0 to 7 generate
      LABEL2B: for i in 0 to 7 generate
          LABEL2C: for i in 0 to 7 generate
          end generate LABEL2C;
      end generate LABEL2B;
  end generate LABEL2A;
   
  -- Test multiple layers of nesting
  LABEL2A: for i in 0 to 7 generate
      LABEL2B: for i in 0 to 7 generate
          LABEL2C: for i in 0 to 7 generate
          end generate LABEL2C;
          LABEL2D: for i in 0 to 7 generate
          end generate LABEL2D;
      end generate LABEL2B;
      LABEL2E: for i in 0 to 7 generate
          LABEL2F: for i in 0 to 7 generate
          end generate LABEL2C;
          LABEL2G: for i in 0 to 7 generate
          end generate LABEL2E;
      end generate LABEL2F;
  end generate LABEL2G;

end architecture RTL;
