
architecture ARCH of ENTITY is

begin

  PROC_NAME : process (a, b, c) is
  begin
    if a = 1 then
	b <= d;
	c <= x;
     end if;

     IF a = 1 or d = 20 or    -- this if should not be replaced
       g = 34 or x = 3000 THEN
	b <= e;
	c <= y;
    END if;

    if (a = 1 or d = 20 or
       g = 34 or x = 3000 or
       c = 34) then -- else <-- this should not be classified as an else keyword
	b <= e;
	c <= y;
   ELSIF z = 45 and f = 45 then
	b <= g;
	c <= o;
   end IF;


    if (a = 1 or d = 20 or
        g = 34 or x = 3000 or
        c = 34)then
       if b = 1 then
	b <= e;
	c <= y;
     end if;
      b <= e;
      c <= y;
   end if;

    if a = 1 or d = 20 or
       g = 34 or x = 3000 or
       c = 34 then
      b <= e;
      c <= y;
      if b = 1 then
	b <= e;
	c <= y;
      end if;
    end if;

    if a = 1 or d = 20 or
       g = 34 or x = 3000 or
       c = 34 then
      b <= e;
      c <= y;
      if(b = 1)then
	b <= e;
	c <= y;
        end if;
      b <= e;
    end if;

-- Test blank line requirements

    if (a = 1 or d = 20 or
       g = 34 or x = 3000 or
         c = 34) then

	b <= e;
	c <= y;

    elsif  (z = 45 and f = 45)  then

	b <= g;
	c <= o;

    end if;

    if (a = 1) then

	b <= d;
	c <= x;

   else

	g <= z;

    end if;

    if (a = 1) then
	b <= d;
	c <= x;
    ELSE
	g <= z;
    end if;

    if (a = 2) then b <= d;
    elsif (b = 3) then c <= e;
    elsif (c = 4) then -- Not an error
      c <= f;
    else g <= x;
    end if;

    if (a = 2) then b <= '1'; else b <= '0'; end if;

    if (a = 2) then
      a <= '0'; elsif
      (b = 3) then b <= '1'; else
      c <= '1'; end if;

    if (a = 2) then
      a <= '0';
    elsif (a = 3 or
             b = 4) then
      a <= '1';
    end  if;

  end process PROC_NAME;

  -- checking for whens under and if statment
  PROC_NAME : process () is

  begin

    if (a = '1') then
      d <= sig1 when b = '1'
           else sig2 when c = '0'
           else sig3 when d = '1'
           else sig4;
    else
      d <= '0';
    end if;

  end process;

end architecture ARCH;
