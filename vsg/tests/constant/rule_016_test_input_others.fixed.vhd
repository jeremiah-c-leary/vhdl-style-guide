
architecture rtl of fifo is

  constant AVMM_SLAVE_NULL : t_avmm_slave :=
  (
    (others => '0'),
    '0',
    '0'
  );

  constant cons1 : t_type :=
  (
 (others => '0'),
 (1 => '0', others => '1'),
 (others => '0')
 );

  constant cons2 : t_type :=
  (others => (valid => '0', data => (others => '0')),
 others => (1 => '0', (others => '0')
 );

begin

end architecture rtl;
