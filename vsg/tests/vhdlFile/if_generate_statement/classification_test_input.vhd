
architecture RTL of FIFO is

begin

  LABEL0 : if a = 1 generate

  end generate LABEL0;

  -- Simple test case
  LABEL1 : if a = 1 generate

  elsif a = 0 generate

  elsif a = 1 generate

  else generate

  end generate LABEL1;

  -- Test nesting
  LABEL2A: if a = 1 generate

    LABEL3A : if x = 0 generate

    elsif y = 1 generate

    else generate

    end generate LABEL3A;

  elsif b = 0 generate

  elsif c = 1 generate

  else generate

  end generate LABEL2A;

  -- Test multiple layers of nesting
  LABEL2A: if a = 1 generate

      LABEL3A : if x = 0 generate

          LABEL4A : if x = 0 generate

          elsif y = 1 generate

          else generate

          end generate LABEL4A;

      elsif y = 1 generate

      else generate

      end generate LABEL3A;

  elsif b = 0 generate

      LABEL3A : if x = 0 generate

          LABEL4A : if x = 0 generate

          elsif y = 1 generate

          else generate

          end generate LABEL4A;

      elsif y = 1 generate

      else generate

      end generate LABEL3A;

  elsif c = 1 generate

      LABEL3A : if x = 0 generate

          LABEL4A : if x = 0 generate

          elsif y = 1 generate

          else generate

          end generate LABEL4A;

      elsif y = 1 generate

      else generate

      end generate LABEL3A;

  else generate

      LABEL3A : if x = 0 generate

          LABEL4A : if x = 0 generate

          elsif y = 1 generate

          else generate

          end generate LABEL4A;

      elsif y = 1 generate

      else generate

      end generate LABEL3A;

  end generate LABEL2A;

end architecture RTL;
