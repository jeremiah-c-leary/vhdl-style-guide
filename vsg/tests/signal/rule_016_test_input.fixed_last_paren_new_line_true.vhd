

architecture ARCH of ENTITY is

  signal sig1, sig2 : std_logic;

  signal sig1, sig2 : std_logic_vector(0 downto 0);

  signal sig1, sig2 : std_logic_vector(some_func(a, b, c) downto other_func(e, f, g));

  signal sig1, sig2, sig3,
     sig4, sig5, sig6 : std_logic;


  -- Test record types with assignments
  signal sig_a : t_record_type(
    data(31 downto 0),
    empty(7 downto 0),
    error(0 downto 0)
  );

  signal sig_a : t_record_type(data(31 downto 0), empty(7 downto 0), error(0 downto 0));

  signal sig_a : t_record_type
  (
    data(31 downto 0),
    empty(7 downto 0),
    error(0 downto 0)
  );

  signal sig_a : t_record_type
  (
    data(31 downto 0),
    empty(7 downto 0),
    error(0 downto 0)
 );

  signal sig_a : t_record_type
  (
    data(31 downto 0), empty(7 downto 0), error(0 downto 0)
 );

  -- Open Paren

  signal sig_a : t_record_type
  (
    (
      data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0)
    ),
    (
      data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0)
    )
  );

  signal sig_a : t_record_type
  ((data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0)
    ),(data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0)
    )
  );

  -- Close Paren

  signal sig_a : t_record_type
  (
    (
      data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0)),
    (
      data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0))
  );

  -- Comment on last line check

  signal sig_a : t_record_type
  (
    (
      data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0)),
    (
      data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0))
 ); -- Comment

  signal sig_a : t_record_type
  (
    (
      data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0)),
    (
      data1(31 downto 0),
      empty1(7 downto 0),
      error1(0 downto 0))
  ); -- Comment

begin

end architecture ARCH;

