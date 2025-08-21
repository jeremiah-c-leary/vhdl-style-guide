
architecture ARCH of ENTITY is

begin

  -- Passing

  PROC_2 : process (a) is
  begin

    a   := b or -- c = '2';
           c or
           d = '1';
    c1  := d;
    e12 := f and g and h
           or i and j;

    case CASE_LOGIC is
      when a = 1 =>

        a := b or
             c and
             d = '1';

      when b = 1 =>

        if a = 1 then
           c12 := d or e or
                  f and g;
           e1  := f and x or y;
        end if;

    end case;

    a :=
         b;

  end process PROC_2;

  -- Violations

  PROC_2 : process (a) is
  begin

    a   := b or -- c = '2';
           c or
           d = '1';
    c1  := d;
    e12 := f and g and h
           or i and j;

    case CASE_LOGIC is
      when a = 1 =>

        a := b or
             c and
             d = '1';

      when b = 1 =>

        if a = 1 then
           c12 := d or e or
                  f and g;
           e1  := f and x or y;
        end if;

    end case;

    a :=
         b;

  end process PROC_2;

  -- Check that array assignments are ignored.
  PROC_2 : process is
  begin
    a :=
    (
      0 => f.a,
      1 => f.b,
      2 => f.c
    );
  end process PROC_2;

  -- Check that conditional assignments are ignored.
  PROC_3 : process is
  begin
    a := 0 when b = '0' or
                                 a = '1' else 10;
  end process PROC_3;

end architecture ARCH;
