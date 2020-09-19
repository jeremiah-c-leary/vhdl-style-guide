
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    C1: case ? x is
      when 1 => Out_1 <= 0;
      when 2 => Out_1 <= 1;
      when 3 => Out_1 <= 2;
    end case ? C1;

    C1: case x is
      when 1 => Out_1 <= 0;
      when 2 => Out_1 <= 1;
      when 3 => Out_1 <= 2;
    end case C1;

    case x is
      when 1 => Out_1 <= 0;
      when 2 => Out_1 <= 1;
      when 3 => Out_1 <= 2;
    end case;

  end process;

  process
  begin

    C3: case Code_Variable is
      when ADD | SUB => Operation := 0;
      when MULT | DIV => Operation := 1;
    end case C3;

  end process;


end architecture RTL;
