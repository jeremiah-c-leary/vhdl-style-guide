architecture rtl of fifo is

  constant my_rec : t_my_rec :=
  (
    signal_one => '0',
    signal_onetwo => '0'

    signal_onetwothree => '0',
    signal_onetwothreefour => '0'
    -- Comment
    signal_onetwothreefourfive => '0',
    signal_onetwothreefourfivesix => '0'
  );

  constant C_DEFAULT_VALUES : t_address_en := (
    C_ADDRESS_CONTROL_A => false,
    C_ADDRESS_DATA_A => true,
    others => false

    C_ADDRESS_CONTROL_B => false,
    C_ADDRESS_DATA_B => true,
    others => false
    -- Comment
    C_ADDRESS_CONTROL_C => false,
    C_ADDRESS_DATA_C => true,
    others => false
  );

  constant my_rec : t_my_rec :=
  (
    signal_one=> '0',
    signal_onetwo                           => '0'

    signal_onetwothree          => '0',
    signal_onetwothreefour=> '0'
    -- Comment
    signal_onetwothreefourfive          => '0',
    signal_onetwothreefourfivesix    => '0'
  );

  constant C_DEFAULT_VALUES : t_address_en := (
    C_ADDRESS_CONTROL_A        => false,
    C_ADDRESS_DATA_A=> true,
    others                             => false

    C_ADDRESS_CONTROL_B    => false,
    C_ADDRESS_DATA_B    => true,
    others => false
    -- Comment
    C_ADDRESS_CONTROL_C       => false,
    C_ADDRESS_DATA_C      => true,
    others=> false
  );

  -- Test hierarcical assignments
  -- Desired alignment
  constant my_constant : my_type := (
    ENUM_1 => (
      A => 1,
      B => 2,
      C => 3
    ),
    ENUM_224 => (
      AA => 1,
      BB => 2,
      CC => 3
    )
  );

  -- Invalid alignment
  constant my_constant : my_type := (
    ENUM_1    => (
      A    => 1,
      B=> 2,
      C  => 3
    ),
    ENUM_224=> (
      AA=> 1,
      BB      => 2,
      CC   => 3
    )
  );

begin

end architecture rtl;
