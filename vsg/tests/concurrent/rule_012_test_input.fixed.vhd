
architecture RTL of FIFO is

begin




    -- These are passing
    ret <=
 (
      data  => (others => '-'),
      valid => '0',
      sop   => '0',
      eop   => '0',
      empty => (others => '0'),
      error => (others => '0')
    );

    -- These are failing

    ret <=
 (
 data  => (others => '-'),
 valid => '0',
 sop   => '0',
 eop   => '0',
 empty => (others => '0'),
 error => (others => '0')
 );




end architecture RTL;
