
architecture RTL of FIFO is

  function func1 return integer is begin

    loop

      label_next : next my_loop WHEN condition;
      next my_loop WHEN condition;
      next WHEN condition;

    end loop;

  end function func1;

  function func1 return integer is begin

    loop

      label_next : next my_loop WHEN condition;
      next my_loop WHEN condition;
      next WHEN condition;

    end loop;

  end function func1;

begin

end architecture RTL;
