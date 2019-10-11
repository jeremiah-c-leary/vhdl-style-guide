
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a, b, c) is
  begin
     -- This is a case statement
     case  boolean_1 is

      when STATE_1 =>

        a <= b;
	b <= c;
	c <= d;

      when  STATE_2  =>

        a <= b;
	b <= c;
	c <= d;

      when STATE_3  =>

        a <= b;
	b <= c;
	c <= d;

      when   others =>

          null;

     end  case;
   -- This will be an error
  end process PROC_1;


  PROC_1 : process (a, b, c) is
  begin
    a <= a;
    CASE boolean_1 or
         boolean_2 or
	 boolean_3   IS 
     -- This comment will be an error
     WHEN STATE_1 or
            STATE_1 and STATE_3 =>

        a <= b;
	b <= c;
	c <= d;

       wHEn  STATE_2 =>

        a <= b;
	b <= c;
	c <= d;

      wheN STATE_3 or
         STATE_3 or
           STATE_4 =>

        a <= b;
	b <= c;
	c <= d;

      when others  =>

        null;
   -- This will be an error
   end CASE;

  end process PROC_1;

  PROC_1 : process (a, b, c) is
  begin

    case(boolean)is

    END case;

  end process PROC_1;

  -- Checking for labels in front of case keywords
  PROC_1 : process (a, b, c) is
  begin

    MY_LABEL:case (boolean) is

      when STATE_1 =>
        a <= b;
      when STATE_2 =>
        a <= b;
      when STATE_3 =>
        a <= b;
      when others =>
        null;

    end case LABEL;

  end process PROC_1;

end architecture ARCH;
