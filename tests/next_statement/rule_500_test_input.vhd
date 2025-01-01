
architecture RTL of FIFO is

  function func1 return integer is begin

    loop

      label_next : next my_loop when condition;
      next my_loop when condition;
      next when condition;
      next;

    end loop;

  end function func1;

  function func1 return integer is begin

    loop

      label_next : NEXT my_loop when condition;
      NEXT my_loop when condition;
      NEXT when condition;
      NEXT;

    end loop;

  end function func1;

begin

end architecture RTL;
