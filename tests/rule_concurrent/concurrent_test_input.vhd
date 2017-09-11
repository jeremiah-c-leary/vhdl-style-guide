
architecture ARCH of ENTITY is

begin

  a <= b;
 a<=b;
  a<=    b;
  a <=
       b;
    a <= b;

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

end architecture ARCH;
