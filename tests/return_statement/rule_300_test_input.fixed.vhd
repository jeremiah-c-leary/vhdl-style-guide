
architecture RTL of FIFO is

  function func1 return integer is begin

    return my_value;
    return_label : return my_value;

  end function func1;

  function func1 return integer is begin

    return my_value;
    return my_value;
    return_label : return my_value;
    return_label : return my_value;

  end function func1;

begin

end architecture RTL;
