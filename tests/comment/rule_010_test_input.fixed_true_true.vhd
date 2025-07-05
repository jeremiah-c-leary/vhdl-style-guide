
-- failure
-- passed

context interfaces is

  library fpga;
    -- Comment 2
    context fpga.constants;
    -- Comment 3
    -- Comment 4
    -- Comment 5
    use fpga.fpga_if.all;
    -- Comment 6
    -- Comment 7
    -- use fpga.registers.all;
    use fpga.functions.all;

  -- Comment last

end context interfaces;


architecture RTL of FIFO is

  -- failure
  -- passed
  -- failure

begin

  -- failure
  -- passed
  -- failure

end architecture RTL;

architecture rtl of fifo is

  constant c_cons1 : t_type :=
  (
      -- Comment 1
   (
 -- Comment 2
     a => 1,
              -- Comment 3
     b => 2
   )
       -- Comment 4
  );

begin end architecture RTL;

architecture RTL of FIFO is

  -- pass

  constant c_const1 : natural := 0;
  constant c_const2 : natural := 1;

begin end architecture RTL;

library ieee;
-- Comment 1
architecture rtl of fifo is
  -- Comment 2
begin
  -- Comment 3
end architecture rtl;

library ieee;
-- Comment 1b
entity fifo is
  -- Comment 2b
end entity;

library ieee;
-- Comment 1c
package body fifo_pkg is
  -- Comment 2c
end package body;

library ieee;
-- Comment 1c
package fifo_pkg is
  -- Comment 2c
end package;

package body function_pkg is

  function init_axi4_aw (
    aw   : in axi4_aw_t;
    ival : std_logic := 'Z'
  ) return axi4_aw_t is
  begin
    return (
      -- AXI4 Lite  <<< HERE
      addr   => (aw.addr'range => ival),
      -- AXI 4 Full <<< AND HERE
      id     => (aw.id'range => ival),
      len    => (aw.len'range => ival)
    );
  end function init_axi4_aw;

end package body function_pkg;
