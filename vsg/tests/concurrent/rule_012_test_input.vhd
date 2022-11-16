
architecture RTL of FIFO is

begin




    -- These are passing
    ret <= (
      data  => (others => '-'),
      valid => '0',
      sop   => '0',
      eop   => '0',
      empty => (others => '0'),
      error => (others => '0')
    );

    -- These are failing

    ret <= (data  => (others => '-'), valid => '0', sop   => '0', eop   => '0', empty => (others => '0'), error => (others => '0'));


  -- This is not an array and should not be "fixed"

  d <=
       (d2 xor to_stdulogic(gen2)) &
       (d1 xor to_stdulogic(gen1));

end architecture RTL;
