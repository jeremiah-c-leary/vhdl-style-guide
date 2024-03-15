
architecture RTL of FIFO is

begin

  process
  begin

    loop
      a <= b;

    end loop;

    -- Violations below

    loop
      a <= b;
    end loop;


  end process;

end;
