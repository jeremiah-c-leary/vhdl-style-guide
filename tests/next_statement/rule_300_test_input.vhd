
architecture RTL of FIFO is

  function func1 return integer is begin

    loop

      next_label : next my_loop when condition;
      next_label : next my_loop when condition;
      next my_loop when condition;
      next my_loop when condition;
      next when condition;
      next when condition;
      next;
      next;

    end loop;

  end function func1;

  function func1 return integer is begin

    loop

            next_label : next my_loop when condition;
next_label : next my_loop when condition;
            next my_loop when condition;
next my_loop when condition;
            next when condition;
next when condition;
            next;
next;

    end loop;

  end function func1;

begin

end architecture RTL;
