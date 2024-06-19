
architecture RTL of FIFO is

begin

  -- Passing
  process begin
    if a = b then
    elsif a /= b then
    elsif a < b then
    elsif a <= b then
    elsif a > b then
    elsif a >= b then
    elsif a ?= b then
    elsif a ?/= b then
    elsif a ?< b then
    elsif a ?<= b then
    elsif a ?> b then
    elsif a ?>= b then
    end if;
  end process;

  -- missing spaces after operator
  process begin
    if a =b then
    elsif a /=b then
    elsif a <b then
    elsif a <=b then
    elsif a >b then
    elsif a >=b then
    elsif a ?=b then
    elsif a ?/=b then
    elsif a ?<b then
    elsif a ?<=b then
    elsif a ?>b then
    elsif a ?>=b then
    end if;
  end process;

  -- missing spaces before operator
  process begin
    if a= b then
    elsif a/= b then
    elsif a< b then
    elsif a<= b then
    elsif a> b then
    elsif a>= b then
    elsif a?= b then
    elsif a?/= b then
    elsif a?< b then
    elsif a?<= b then
    elsif a?> b then
    elsif a?>= b then
    end if;
  end process;

  -- missing spaces before and after operator
  process begin
    if a=b then
    elsif a/=b then
    elsif a<b then
    elsif a<=b then
    elsif a>b then
    elsif a>=b then
    elsif a?=b then
    elsif a?/=b then
    elsif a?<b then
    elsif a?<=b then
    elsif a?>b then
    elsif a?>=b then
    end if;
  end process;

  -- extra spaces before operator
  process begin
    if a     = b then
    elsif a     /= b then
    elsif a     < b then
    elsif a   <= b then
    elsif a   > b then
    elsif a   >= b then
    elsif a   ?= b then
    elsif a   ?/= b then
    elsif a   ?< b then
    elsif a   ?<= b then
    elsif a   ?> b then
    elsif a   ?>= b then
    end if;
  end process;

  -- extra spaces after operator
  process begin
    if a =    b then
    elsif a /=    b then
    elsif a <    b then
    elsif a <=    b then
    elsif a >    b then
    elsif a >=    b then
    elsif a ?=    b then
    elsif a ?/=    b then
    elsif a ?<    b then
    elsif a ?<=    b then
    elsif a ?>    b then
    elsif a ?>=    b then
    end if;
  end process;

  -- extra spaces before and after operator
  process begin
    if a    =    b then
    elsif a    /=    b then
    elsif a    <    b then
    elsif a    <=    b then
    elsif a    >    b then
    elsif a    >=    b then
    elsif a    ?=    b then
    elsif a    ?/=    b then
    elsif a    ?<    b then
    elsif a    ?<=    b then
    elsif a    ?>    b then
    elsif a    ?>=    b then
    end if;
  end process;

end architecture RTL;
