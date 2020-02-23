
architecture ARCH of ENTITY_1 is

begin

  -- Passing test case
  LABEL1 : if blah generate
    LABEL2 : for i in 0 to some_number generate
    end generate LABEL2;
  end generate LABEL1;

  -- Failing test cases
  LABEL1 : if blah generate
    LABEL2 : for i in 0 to some_number generate
    end generate;
  end generate;

  -- Multiple level test case
  LABEL1 : if blah generate
    LABEL2A : for i in 0 to some_number generate
      LABEL2A1 : for i in 0 to some_number generate
      end generate;
      LABEL2A2 : for i in 0 to some_number generate
        LABEL2A2A : for i in 0 to some_number generate
        end generate;
      end generate;
      LABEL2A3 : for i in 0 to some_number generate
      end generate;
    end generate;
    LABEL2B : for i in 0 to some_number generate
      LABEL2B1 : for i in 0 to some_number generate
      end generate;
      LABEL2B2 : for i in 0 to some_number generate
      end generate;
      LABEL2B3 : for i in 0 to some_number generate
        LABEL2B3A : for i in 0 to some_number generate
        end generate;
      end generate;
    end generate;
    LABEL2C : for i in 0 to some_number generate
      LABEL2C1 : for i in 0 to some_number generate
        LABEL2C1A : for i in 0 to some_number generate
        end generate;
      end generate;
      LABEL2C2 : for i in 0 to some_number generate
      end generate;
      LABEL2C3 : for i in 0 to some_number generate
      end generate;
    end generate;
    LABEL2D : for i in 0 to some_number generate
      LABEL2D1 : for i in 0 to some_number generate
      end generate;
      LABEL2D2 : for i in 0 to some_number generate
      end generate;
      LABEL2D3 : for i in 0 to some_number generate
      end generate;
    end generate;
  end generate;

  -- Failing test cases
  LABEL1 : if blah generate
    LABEL2 : for i in 0 to some_number generate
      LABEL3 : for i in 0 to some_number generate
      end generate LABEL3;
    end generate;
  end generate;

end architecture ARCH;
