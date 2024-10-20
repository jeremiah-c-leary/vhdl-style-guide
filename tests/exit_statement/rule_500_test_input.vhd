
architecture RTL of FIFO is

  function func1 return integer is begin

    loop

      label_exit : exit my_loop when condition;
      exit my_loop when condition;
      exit when condition;
      exit;

    end loop;

  end function func1;

  function func1 return integer is begin

    loop

      label_exit : EXIT my_loop when condition;
      EXIT my_loop when condition;
      EXIT when condition;
      EXIT;

    end loop;

  end function func1;

begin

end architecture RTL;
