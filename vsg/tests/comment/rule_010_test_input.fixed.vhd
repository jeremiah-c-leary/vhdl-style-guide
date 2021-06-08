
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
