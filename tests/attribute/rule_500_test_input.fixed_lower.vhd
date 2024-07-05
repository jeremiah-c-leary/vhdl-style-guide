
architecture rtl of fifo is

  -- Type attributes
  signal a : something'ascending;
  signal a : something'base;
  signal a : something'high;
  signal a : something'image(x);
  signal a : something'left;
  signal a : something'leftof(x);
  signal a : something'low;
  signal a : something'pos(x);
  signal a : something'pred(x);
  signal a : something'right;
  signal a : something'rightof(x);
  signal a : something'succ(x);
  signal a : something'val(x);
  signal a : something'value(x);

  -- Array attributes
  signal a : something'ascending(n);
  signal a : something'high(n);
  signal a : something'left(n);
  signal a : something'length(n);
  signal a : something'low(n);
  signal a : something'range(n);
  signal a : something'reverse_range(n);
  signal a : something'right(n);

  -- Signal attributes
  signal a : something'active;
  signal a : something'delayed(t);
  signal a : something'driving;
  signal a : something'driving_value;
  signal a : something'event;
  signal a : something'last_event;
  signal a : something'last_active;
  signal a : something'last_value;
  signal a : something'quiet(t);
  signal a : something'stable(t);
  signal a : something'transaction;

  -- Other attributes
  signal a : something'instance_name;
  signal a : something'path_name;
  signal a : something'simple_name;

begin

end architecture rtl;
