
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
  end generate GENERATE_1;

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
  end generate GENERATE_1;


  GENERATE_1 : for i in 0 to 7 generate
    a <= b;

    GENERATE_2 : for i in 0 to 7 generate
      a <= b;

      GENERATE_3 : for i in 0 to 7 generate
        a <= b;
      end generate GENERATE_3;

    end generate GENERATE_2;

    GENERATE_4 : for i in 0 to 7 generate
      a <= b;
    end generate GENERATE_4;

  end generate GENERATE_1;


end architecture ARCH;
