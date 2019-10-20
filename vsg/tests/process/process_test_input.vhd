
architecture ARCH of ENTITY is

begin

  process (one, two, three) IS begin

    -- This is a comment
    end process;

  process (one, two,
           three) is
  begin

 eNd  process;
  
prOCess  (one,
          two,
               three)   is
begIN
 -- This begin should not be detected
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
  END_PROC_NAME: process (one) is
  begin
  end process END_PROC_NAME;


  PROC_NAME :process (one) is

  begin
  
  end process PROC_NAME;


  PROC_NAME : process (one) is
    -- This is a comment
  begin
  
  end process PROC_NAME;

  PROC_NAME : process (one) is

    -- This is a comment
  begin
  
  end process PROC_NAME;

  PROC_NAME : process (one) is

    -- This is a comment

  begin
  
  end process PROC_NAME;


  PROC_NAME : process (one) is

    variable var_1 : std_logic_vector(1 downto 0);

  begin
  
  end process PROC_NAME;

  U_ENTITY1 : ENTITY1
    generic map (
        process1 => '1'
    )
    port map (
      process2 => '3';
      process_2 => '4' 
    );

  -- processes without sensitivity lists

  MAIN : process

    variable var_a : std_logic_vector(16 downto 0);
    variable var_b;

  begin

  end process MAIN;

  process

    variable var_a : std_logic_vector(16 downto 0);
    variable var_b;

  begin

  end process;

--PROC_NAME : process (one) is
--
--  begin
--
--  end process;

  TEST_PROCESS : process

    procedure test_procedure (
      constant test1_c    : in boolean := true
    ) is
    begin
    end procedure test_procedure;

  begin

  end process TEST_PROCESS;

  TEST : process is
  begin

  end process TEST;

end architecture ARCH;

