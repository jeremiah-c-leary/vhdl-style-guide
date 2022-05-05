
architecture rtl of fifo is

  -- Type attributes
  signal a : something'ASCENDING;
  signal a : something'BASE;
  signal a : something'HIGH;
  signal a : something'IMAGE(x);
  signal a : something'LEFT;
  signal a : something'LEFTOF(x);
  signal a : something'LOW;
  signal a : something'POS(x);
  signal a : something'PRED(x);
  signal a : something'RIGHT;
  signal a : something'RIGHTOF(x);
  signal a : something'SUCC(x);
  signal a : something'VAL(x);
  signal a : something'VALUE(x);

  -- Array attributes
  signal a : something'ASCENDING(n);
  signal a : something'HIGH(n);
  signal a : something'LEFT(n);
  signal a : something'LENGTH(n);
  signal a : something'LOW(n);
  signal a : something'RANGE(n);
  signal a : something'REVERSE_RANGE(n);
  signal a : something'RIGHT(n);

  -- Signal attributes
  signal a : something'ACTIVE;
  signal a : something'DELAYED(t);
  signal a : something'DRIVING;
  signal a : something'DRIVING_VALUE;
  signal a : something'EVENT;
  signal a : something'LAST_EVENT;
  signal a : something'LAST_ACTIVE;
  signal a : something'LAST_VALUE;
  signal a : something'QUIET(t);
  signal a : something'STABLE(t);
  signal a : something'TRANSACTION;

  -- Other attributes
  signal a : something'INSTANCE_NAME;
  signal a : something'PATH_NAME;
  signal a : something'SIMPLE_NAME;

begin

end architecture rtl;
