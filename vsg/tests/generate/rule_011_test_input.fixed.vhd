
architecture RTL of FIFO is

begin

  FOR_LABEL : for i in 0 to 7 generate

  end generate FOR_LABEL;

  IF_LABEL : if a = '1' generate

  end generate IF_LABEL;

  CASE_LABEL : case data generate

  end generate CASE_LABEL;

  -- Violations below

  FOR_LABEL : for i in 0 to 7 generate

  end generate FOR_LABEL;

  IF_LABEL : if a = '1' generate

  end generate IF_LABEL;

  CASE_LABEL : case data generate

  end generate CASE_LABEL;

  -- Nested generates

  LABEL_1 : for i in 0 to 7 generate

    LABEL_2 : if a = '1' generate

      LABEL_3 : case data generate

      end generate LABEL_3;

      LABEL_4 : for i in 1 to 8 generate

      end generate LABEL_4;

    end generate LABEL_2;

    LABEL_5 : if b = '1' generate

      LABEL_6 : case data generate

      end generate LABEL_6;

      LABEL_7 : for i in 1 to 8 generate

      end generate LABEL_7;

    end generate LABEL_5;

  end generate LABEL_1;

end;
