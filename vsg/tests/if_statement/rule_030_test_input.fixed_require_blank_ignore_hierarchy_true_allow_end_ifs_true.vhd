
architecture RTL of FIFO is

begin

  process

  begin

    if a then
      if b then
        if c then
          c <= d;
        end if;

        a <= b;
      end if;

      b <= c;
    end if;

    z <= a;

    -- Violations below

    if a then
      if b then
        if c then
          c <= d;
        end if;

        a <= b;
      end if;

      b <= c;
    end if;

    z <= a;

  end process;

end architecture RTL;

-- Test allow_end_ifs option

architecture RTL of FIFO is

begin

  process begin

    if a then
      if b then
        if c then
          c <= d;
        end if;
      end if;
    end if;

  end process;

end architecture RTL;

-- Test allow_end_case

architecture RTL of FIFO is

begin

  process begin

    case x is

       when 32 =>

       if a then
         if b then
           if c then

             case y is

               when 64 =>
                 if x then
                 end if;

             end case;

           end if;
         end if;
       end if;

    end case;

    case x is

       when 32 =>

       if a then
         if b then
           if c then
             case y is

               when 64 =>
                 if x then
                 end if;

             end case;

           end if;
         end if;
       end if;

    end case;

  end process;

end architecture RTL;

-- Test allow_end_loop

architecture RTL of FIFO is

begin

  process begin

    loop

       if a then
         if b then
           if c then

             loop

                 if x then
                 end if;

             end loop;

           end if;
         end if;
       end if;

    end loop;

    loop

       if a then
         if b then
           if c then
             loop
                 if x then
                 end if;

             end loop;

           end if;
         end if;
       end if;

    end loop;

  end process;

end architecture RTL;

-- Test allow_end_subpogram_body

architecture RTL of FIFO is

  procedure proc1 is
  begin
    if a then
      if b then
        if c then
          c <= d;
        end if;

        a <= b;
      end if;

      b <= c;
    end if;

  end procedure proc1;

  procedure proc1 is
  begin
    if a then
      if b then
        if c then
          c <= d;
        end if;

        a <= b;
      end if;

      b <= c;
    end if;

  end procedure proc1;

begin

end architecture RTL;

-- Test no blank line and end ifs

architecture RTL of FIFO is

  procedure proc1 is
  begin
    if a then
      if b then
        if c then
          c <= d;
        end if;
      end if;
    end if;

  end procedure proc1;

begin

end architecture RTL;
