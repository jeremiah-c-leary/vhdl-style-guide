
architecture ARCH of ENTITY is

begin

  a(5 downto 0) <= b;      -- Comment
 a<=b;             -- Comment
  a<=    (b); -- Comment
  a <=                 -- Comment
       b;     
    a <= b;       -- Comment

  process () is
  begin
     d<=c;
  end process;

  PROC_NAME:process () is
  begin
     d<=c;
  end process;

  a <= b;
 a <=b;

  a <= b or c
       d or e
      f or g
         h or i
     j or k;

label:a<=b;
 label :a<=b;
  label : a <= b;
  label : a <= b or c
               d or e;

  a <= b;
  b <= c or
       d or e
       and f;
  c <= d;

  a <= b when g = '0' else c;
  a <= b when g = '1' else -- Not an error
       c;

  a <= b when g = '1' else '1'; -- Not an error

end architecture ARCH;
