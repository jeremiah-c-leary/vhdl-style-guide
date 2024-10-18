
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

      label_exit : exit my_loop when condition;
      exit my_loop when condition;
      exit when condition;
      exit;

    end loop;

  end function func1;

begin

end architecture RTL;
