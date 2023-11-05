
architecture RTL of FIFO is

begin

  -- Test generate_statement_body
  LABEL_1 : for i in 0 to 7 generate

      signal blah : std_logic;

    begin
        a <= blah;
    end LABEL_1A;

  end generate LABEL3;

  -- Test generate_statement_body
  LABEL_2 : for i in 0 to 7 generate

    begin
        a <= blah;
    end;

  end generate LABEL3;

  -- Test generate_statement_body
  LABEL_3 : for i in 0 to 7 generate

    begin
        a <= blah;

  end generate LABEL3;

end architecture RTL;
