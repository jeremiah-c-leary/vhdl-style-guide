
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    I1: if Status_Signal = hold
          then A1: Outputs <= 'X';
        end if I1;
    
    I2: if x = '1' and y = '1'
            then return '1';
          else return '0';
          end if I2;
    
    
    I3: if Code_of_Operation(1) = '1'
          then F := Operand_1 + Operand_2;
        elsif Code_of_Operation(0) = '1'
          then F := Operand_1 - Operand_2;
          else F := "00000000";
        end if I3;
    
    if Status = RUN
      then
        if Code_of_Operation = CONC
          then
            F := Operand_1 & Operand_2 ;
          else
            F := "00000000";
        end if;
      Output_1 <= F;
    end if;

  end process;

end architecture RTL;
