
package pkg is

  procedure my_proc is new my_generic_proc
    generic map (
      test => 2
    );

  function my_func is new my_generic_func
    generic map (
      test => 2
    );

  procedure MY_PROC is new my_generic_proc
    generic map (
      test => 2
    );

  function MY_FUNC is new my_generic_func
    generic map (
      test => 2
    );

  procedure My_proc is new my_generic_proc
    generic map (
      test => 2
    );

  function My_func is new my_generic_func
    generic map (
      test => 2
    );

end package;
