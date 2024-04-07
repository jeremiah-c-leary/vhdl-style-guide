
architecture RTL of FIFO is

begin

  CASE_LABEL : case data generate

    when 0 =>

      a <= z;

    when 1 =>

      a <= c;

    when 2 =>

      a <= b;

    when others =>

      null;

  end generate;

  -- Violations below


  CASE_LABEL : case data generate

         when 0 =>

      a <= z;

when 1 =>

      a <= c;

      when 2 =>

      a <= b;

   when others =>

      null;

  end generate;

end;
