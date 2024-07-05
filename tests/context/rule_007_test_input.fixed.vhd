
context c1 is
  library ieee;
end context c1;

-- try multiline
context c1
is
  library ieee;
end context c1;

context
c1
is
 library ieee;
end
context
c1
;

context
c1
is
  library ieee;
end
;

context
c1
is
  library ieee;
end
context
;

-- Try single line
context c1 is
 library ieee; use ieee.std_logic_1164; end;

context c1 is
 library ieee; use ieee.std_logic_1164; end context;

context c1 is
 library ieee; use ieee.std_logic_1164; end context c1;

-- Check comments

context -- comment 1
c1 -- comment 2
is -- comment 3
  library ieee; -- comment 4
end -- comment 5
context -- comment 6
c1 -- comment 7
; -- comment 8
