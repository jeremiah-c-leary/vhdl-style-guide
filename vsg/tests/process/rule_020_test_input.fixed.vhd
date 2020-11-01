
architecture ARCH of ENTITY is

begin

  process (a, b, c, d)
  begin
  end process;

  process (a,
           b,
           c,
           d)
  begin
  end process;

  process (a,
           b,
           c,
           d
          )
  begin
  end process;

  -- Violations

  process (a,
           b,
           c,
           d)
  begin
  end process;

  process (a,
           b,
           c,
           d)
  begin
  end process;

  process (a,
           b,
           c,
           d
           )
  begin
  end process;

  process (a,
           b,
           c,
           d
       )
  begin
  end process;


end architecture ARCH;

