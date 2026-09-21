
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

  -- Check bit string literal as choice

  process begin
    case x is
      when x"1" => Out_1 <= 0;
    end case;
  end process;

  -- Check others

  process begin
    case x is
      when others => Out_1 <= 0;
    end case;
  end process;

  process begin
    case foo(i) is
    end case;
  end process;

  -- Testing combined case and ?

  process begin
    case? is
    end case;
  end process;

end architecture RTL;
