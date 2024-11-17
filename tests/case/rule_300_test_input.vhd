
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a, b, c) is
  begin

    my_case_statement_label : case boolean_1 is

      when STATE_1 =>

        a <= b;
        b <= c;
        c <= d;

    end case;

    -- Violations below

        my_case_statement_label : case boolean_1 is

      when STATE_1 =>

        a <= b;
        b <= c;
        c <= d;

    end case;

my_case_statement_label : case boolean_1 is

      when STATE_1 =>

        a <= b;
        b <= c;
        c <= d;

    end case;

  end process PROC_1;

end architecture ARCH;
