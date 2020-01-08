
-- Comment
 -- Comment

architecture ARCh of ENTITY
begin
-- Comment
  --Comment

  PROC_1 : process (a) is
  begin
-- Comment
  -- Comment
    -- Comment
    a <= b        -- Comment
    c <= d        -- Comment
                  -- Comment
    e <= f         -- Comment
                  -- Comment
    -- Comment
     -- Comment
    -- Comment
   -- Comment

    if (a = 1) then    -- Comment
      a <= b          -- Comment
                       -- Comment
      c <= d           -- Comment
      e <= f           -- Comment
                   -- Comment
    end if

  end process PROC_1:

end architecture

entity ENTITY is
  generic (
    G_GENERIC_1 : std_logic := '1';-- Comment
    G_GENERIC_2 : std_logic := '0';   -- Comment
    -- Comment
    G_GENERIC_3 : std_logic := '1';
    G_GENERIC_3 : std_logic := '1'; -- Comment
    G_GENERIC_3 : std_logic := '1';  -- Comment
     -- Comment
    G_GENERIC_3 : std_logic := '1';  -- Comment
    G_GENERIC_3 : std_logic := '1';  -- Comment
    G_GENERIC_3 : std_logic := '1';  -- Comment
                                   -- Comment
    G_GENERIC_3 : std_logic := '1';  -- Comment
    G_GENERIC_3 : std_logic := '1';   -- Comment
    G_GENERIC_3 : std_logic := '1';  -- Comment
    G_GENERIC_3 : std_logic := '1';  -- Comment
    G_GENERIC_3 : std_logic := '1';   -- Comment
    ----------------------------------------------------------
    G_GENERIC_4 : std_logic_vector := "--";
    G_GENERIC_4 : std_logic_vector := "--" & "---"; -- Comment
    G_GENERIC_4 : std_logic_vector := "--";-- Comment --
    G_GENERIC_4 : string := "-- not a comment --";
    G_GENERIC_4 : string := "--not a comment--"; -- but this is.
    G_GENERIC_4 : string := "-- not a comment --";--but--this--is--
    G_GENERIC_4 : string := "-- not a comment --"--but this is.
  );
  port (
    I_PORT_1 : in   std_logic;  -- Comment
    I_PORT_1 : in   std_logic;   -- Comment
    -- Comment
    I_PORT_1 : in   std_logic;  -- Comment
    I_PORT_1 : in   std_logic; -- Comment
    I_PORT_1 : in   std_logic;  -- Comment
      -- Comment
    I_PORT_1 : in   std_logic;  -- Comment
    I_PORT_1 : in   std_logic;  -- Comment
    I_PORT_1 : in   std_logic;  -- Comment
                              -- Comment
    I_PORT_1 : in   std_logic;  -- Comment
    I_PORT_1 : in   std_logic;   -- Comment
    I_PORT_1 : in   std_logic;  -- Comment
    I_PORT_1 : in   std_logic;  -- Comment
    I_PORT_1 : in   std_logic;   -- Comment
    -- Comment
  );
end entity ENTITY;


-- End of file comments are okay
