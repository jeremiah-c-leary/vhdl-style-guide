
architecture ARCH of ENTITY is

begin

  -- checking for whens under and if statment
  PROC_NAME : process () is

  begin

    if (a = '1') then

      d <= sig1 when b = '1'--This is a comment
           else sig2 when c = '0'  -- This is a comment
           else sig3 when d = '1'
           else sig4;

    else

      d <= '0';

    end if;

  end process;

end architecture ARCH;
