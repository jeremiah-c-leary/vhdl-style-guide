
architecture RTL of FIFO is

begin

  -- Simple form
  a <= b;

  -- Simple form
  a <= b when 'a' else
       c when 'b' else
       d;

  -- Basic version
  with sel select
    out1 <= a when "00",
            b when "01",
            c when "10",
            d when others;

  --+-------------------
  --| Add labels:
  --+-------------------

  -- Simple form
  simple_label : a <= b;

  -- Simple form
  conditional_label : a <= b when 'a' else
       c when 'b' else
       d;

  -- Basic version
  select_label : with sel select
    out1 <= a when "00",
            b when "01",
            c when "10",
            d when others;

  --+-------------------
  --| Add postponed keyword
  --+-------------------

  -- Simple form
  simple_label : postponed a <= b;

  -- Simple form
  conditional_label : postponed a <= b when 'a' else
       c when 'b' else
       d;

  -- Basic version
  select_label : postponed with sel select
    out1 <= a when "00",
            b when "01",
            c when "10",
            d when others;

  --+-------------------
  --| With only postponed keyword
  --+-------------------

  -- Simple form
  postponed a <= b;

  -- Simple form
  postponed a <= b when 'a' else
       c when 'b' else
       d;

  -- Basic version
  postponed with sel select
    out1 <= a when "00",
            b when "01",
            c when "10",
            d when others;

  --+-------------------
  --| Test parenthesis
  --+-------------------

  a <= std_logic(to_unsigned(b, 4));


end architecture RTL;
