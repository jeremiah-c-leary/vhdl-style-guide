
architecture RTL of FIFO is

  function func1 return integer is begin

    loop

      label_next : next my_loop when condition;
      next my_loop when condition;
      next when condition;

    end loop;

  end function func1;

  function func1 return integer is begin

    loop

      label_next : next my_loop when condition;
      next my_loop when condition;
      next when condition;

    end loop;

  end function func1;

begin

end architecture RTL;
