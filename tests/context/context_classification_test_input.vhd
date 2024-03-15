
context c1 is
  library ieee;
end context c1;

-- try multiline
context c2
is
  library ieee;
end context c2;

context
c3
is
  library ieee;
end
context
c3
;

context
c4
is
  library ieee;
end
;

context
c5
is
  library ieee;
end
context
;

-- Try single line
context c6 is library ieee; use ieee.std_logic_1164; end;

context c7 is library ieee; use ieee.std_logic_1164; end context;

context c8 is library ieee; use ieee.std_logic_1164; end context c8;

-- Check comments

context -- comment 1
c9 -- comment 2
is -- comment 3
  library ieee; -- comment 4
end -- comment 5
context -- comment 6
c9 -- comment 7
; -- comment 8
