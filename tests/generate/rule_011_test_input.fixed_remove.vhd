
architecture RTL of FIFO is

begin

  FOR_LABEL : for i in 0 to 7 generate

  end generate;

  IF_LABEL : if a = '1' generate

  end generate;

  CASE_LABEL : case data generate

  end generate;

  -- Violations below

  FOR_LABEL : for i in 0 to 7 generate

  end generate;

  IF_LABEL : if a = '1' generate

  end generate;

  CASE_LABEL : case data generate

  end generate;

  -- Nested generates

  LABEL_1 : for i in 0 to 7 generate

    LABEL_2 : if a = '1' generate

      LABEL_3 : case data generate

      end generate;

      LABEL_4 : for i in 1 to 8 generate

      end generate;

    end generate;

    LABEL_5 : if b = '1' generate

      LABEL_6 : case data generate

      end generate;

      LABEL_7 : for i in 1 to 8 generate

      end generate;

    end generate;

  end generate;

end;
