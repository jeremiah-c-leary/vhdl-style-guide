
architecture ARCH of ENTITY
begin

  PROC_1 : process (a) is
  begin
    -- Comment
    -- Comment
    -- Comment
    -- Comment
    if (a = 1) then
      a <= b;
      c <= d;
      e <= f;
  -- This is a comment
      -- to describe the elsif
        -- code
    elsif (a = 0) then
      a <= z;
-- Yet more code comments
        -- for the next elsif
    elsif (b = 1) then
      a <= e;
        -- and finally comments for the
-- else code
    else
      a <= w;
    end if
    
  end process PROC_1:

  -- Nothing should be detected in the following process
  PROC_1 : process (a) is
  begin
    -- Comment
    -- Comment
    -- Comment
    -- Comment
    if (a = 1) then
      a <= b;
      c <= d;
      e <= f;
    -- This is a comment
    -- to describe the elsif
    -- code
    elsif (a = 0) then
      a <= z;
    -- Yet more code comments
    -- for the next elsif
    elsif (b = 1) then
      a <= e;
    -- and finally comments for the
    -- else code
    else
      a <= w;
    end if
    
  end process PROC_1:


end architecture

