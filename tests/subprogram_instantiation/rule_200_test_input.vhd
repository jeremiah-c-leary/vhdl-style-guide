package test is

  function my_func is new my_generic_func
    generic map (
      test => 2
    );

  procedure my_proc is new my_generic_proc
    generic map (
      test => 2
    );

  function my_func is new my_generic_func
    -- A comment
    generic map (
      test => 2
    );

  procedure my_proc is new my_generic_proc
    -- A comment
    generic map (
      test => 2
    );

  function my_func is new my_generic_func

    generic map (
      test => 2
    );

  procedure my_proc is new my_generic_proc

    generic map (
      test => 2
    );

end package test;
