
architecture RTL of FIFO is

  function func1 return integer is begin

    loop

      label_exit : exit my_loop WHEN condition;
      exit my_loop WHEN condition;
      exit WHEN condition;

    end loop;

  end function func1;

  function func1 return integer is begin

    loop

      label_exit : exit my_loop WHEN condition;
      exit my_loop WHEN condition;
      exit WHEN condition;

    end loop;

  end function func1;

begin

end architecture RTL;
