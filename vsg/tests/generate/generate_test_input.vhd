
architecture ARCH of ENTITY_1 is

begin

  GENERATE_1 : if CONDITION = '1' generate
  begin
    a <= b;
  end generate GENERATE_1;

   generate_1 : IF CONDITION = '1' generate
 begin
    a <= b;
   end generate generate_1;

 generate_1 : if CONDITION = '1' GENERATE
   BEGIN
    a <= b;
END GENERATE generate_1;

  GENERATE_1:if CONDITION = '1' generate
  begin
    a <= b;
  end generate;

  GENERATE_1  :  if  CONDITION = '1'  generate
  begin
    a <= b;
  end  generate GENERATE_1;

  GENERATE_1 : if CONDITION = '1' generate
  begin
    a <= b;
  end generate  GENERATE_1;

  GENERATE_1 : if CONDITION = '1' generate
  begin
    a <= b;
  end generate GENERATE_1;

  GENERATE_1 : if CONDITION = '1' generate
  begin
    a <= b;
  end generate GENERATE_1;

  GENERATE_1 : if CONDITION = '1' generate
  begin
    a <= b;
  end generate GENERATE_1;

  GENERATE_1 : if CONDITION = '1' generate
  begin
    a <= b;
  end generate GENERATE_1;
  b <= c;
  GENERATE_1 : if CONDITION = '1' generate
    a <= b;
  end generate GENERATE_1;

  GENERATE_1 : for i in 0 to 7 generate
    a <= b;
  end Generate GENERATE_1;


  GENERATE_1 : for i in 0 to 7 generate
    a <= b;

    GENERATE_2 : for i in 0 to 7 generate
      a <= b;

      GENERATE_3 : for i in 0 to 7 generate
        a <= b;
      end generate generate_3;

    end generate GENERATE_2;

    GENERATE_4 : for i in 0 to 7 generate
      a <= b;
    end generate GENERATE_4;

  end generate GENERATE_1;

  GENERATE_1 : if(CONDITION = '1')generate
  begin
    a <= b;
  end generate GENERATE_1;

  GENERATE_1 : if (i = 0) generate

    GENERATE_2 : if (j = 10) generate

      -- generate <- this should not be counted as a generate keyword

      GENERATE_3 : if (k = 5) generate
        a <= b;
      end generate generate_3;

    end generate generate_2;

  end generate generate_1;

  --- This tests multiline generate

  GENERATE_1 :
    if (i = 0) generate
    end generate GENERATE_1;

end architecture ARCH;
