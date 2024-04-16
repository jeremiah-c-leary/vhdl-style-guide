
context c1 is

  library ieee;

end context c1;

-- try multiline
context c2 is

  library ieee;

end context c2;

context c3 is

  library ieee;

end context c3;

context c4 is

  library ieee;

end context c4;

context c5 is

  library ieee;

end context c5;

-- Try single line
context c6 is

  library ieee;
    use ieee.std_logic_1164;

end context c6;

context c7 is

  library ieee;
    use ieee.std_logic_1164;

end context c7;

context c8 is

  library ieee;
    use ieee.std_logic_1164;

end context c8;

-- Check comments

context c9 is -- comment 1

  -- comment 2
  -- comment 3

  library ieee; -- comment 4

end context c9; -- comment 5

-- comment 6
-- comment 7
-- comment 8
