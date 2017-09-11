
architecture ARCH of ENTITY is

begin

  process (one, two, three) IS begin


    end process;

  process (one, two,
           three) is
  begin

 eNd  process;
  
prOCess  (one,
          two,
               three)   is
begIN

 end proCEss;

    Process  (one,
          two,
               three
       ) iS
  beGIn

    end  process;

proCEss (one, two, three
          )   Is -- This is a comment
  begin

  End process;

    process (one, two, three
            )is
begin

  end Process;
  a<=b;
  c<=d;

proc_name : process (one, two, three) is
  begin
  end process proc_name;

-- Checking for missing "is" keyword
  process (one, two, three)
  begin
  end process;

  process (one,
           two,
           three)

  begin
  end process;

  a<=b;
  PROC_NAME:process (one) is
  begin
  end process PROC_NAME;

end architecture ARCH;

