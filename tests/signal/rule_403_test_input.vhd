
architecture RTL of FIFO is





    -- These are passing
    signal ret : my_type := (
      data  => (others => '-'),
      valid => '0',
      sop   => '0',
      eop   => '0',
      empty => (others => '0'),
      error => (others => '0')
    );

    -- These are failing

    signal ret : my_type := (data  => (others => '-'), valid => '0', sop   => '0', eop   => '0', empty => (others => '0'), error => (others => '0'));


  -- This is not an array and should not be "fixed"

  signal d : my_type :=
       (d2 xor to_stdulogic(gen2)) &
       (d1 xor to_stdulogic(gen1));

  signal new_phase : my_type := (not sig1) or
               sig2 or
               sig3;

  -- Test functions/constant in array

  signal data_concurrent : my_type :=
  (
    c_enum_list(ENUM_LITERAL_1) => 1,
    others       => 'X'
  );

begin

end architecture RTL;
