
architecture ARCH of ENTITY1 is

begin

  PROC_1 : process (A) is
  begin

    for index in 4 to 23 loop
       sig1(1) <= '0';
    end loop;

  end process PROC_1;

  PROC_2 : process (B) is
  begin

    if (A = 1) then
       for index in 3 to 72 loop
        sig1(index) <= '1';
       for j in 0 to 32 loop
          sig2(index) <= '0';
         end loop;
      end loop;
    elsif (B = 0) then
      for index in 2 to 16 loop
        sig3(index) <= '1';
      end loop;
    end if;

  end process PROC_2;

  PROC_3 : process (C) is
  begin

    label : for index in 10 to 200 loop
      sig1(index) <= '1';
    end loop;

    Label: for index in 10 to 200 loop
      sig1(index) <= '1';
    end loop;

    LABEL :for index in 10 to 200 loop
      sig1(index) <= '1';
    end loop;

    LABEL   : for index in 10 to 200 loop
      sig1(index) <= '1';
    end loop;

    LABEL :    for index in 10 to 200 loop
      sig1(index) <= '1';
    end loop;

    LABEL : for      index in 10 to 200 loop
      sig1(index) <= '1';
    end loop;

  end process PROC_3;

  -- Deeply nested for loop
  PROC_4 : process (C) is
  begin

    for a in 0 to 1 loop               -- 2
      for a_a in 0 to 1 loop           -- 3
        for a_a_a in 0 to 1 loop       -- 4
          for a_a_a_a in 0 to 1 loop   -- 5
            a <= b;                    -- 6
          end loop;                    -- 5
          for a_a_b in 0 to 1 loop     -- 5
            for a_a_b_a in 0 to 1 loop -- 6
              a <= c;                  -- 7
            end loop;                  -- 6
          end loop;                    -- 5
        end loop;                      -- 4
      end loop;                        -- 3
      for a_b in 0 to 1 loop           -- 3
        for a_b_a in 0 to 1 loop       -- 4
          a <= d;                      -- 5
        end loop;                      -- 4
        for a_b_b in 0 to 1 loop       -- 4
          for a_b_b_a in 0 to 1 loop   -- 5
            a <= e;                    -- 6
          end loop;                    -- 5
        end loop;                      -- 4
      end loop;                        -- 3
    end loop;                          -- 2

  end process PROC_4;

  -- Deeply nested for loop
  PROC_5 : process (C) is

    procedure nested_loop_p (a : in integer )is -- 2
    begin                              -- 2
      for j in 0 to 1 loop             -- 3
        for i in 0 to 3 loop           -- 4
          DATA(4 * j + i) := '1';      -- 5
        end loop;                      -- 4
      end loop;                        -- 3
    end procedure nested_loop_p;       -- 2

  begin

  end process PROC_4;


end architecture ARCH;
