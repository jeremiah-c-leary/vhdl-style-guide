
architecture RTL of FIFO is

  function func1 return integer is begin

    loop

      null;
      null_label : null;

    end loop;

  end function func1;

  function func1 return integer is begin

    loop

      null;
      null_label : null;
      null;
      null_label : null;

    end loop;

  end function func1;

begin

end architecture RTL;
