
package pkg is

  procedure my_proc is new my_generic_proc
    generic map (
      test => 2
    );

  function my_func is new my_generic_func
    generic map (
      test => 2
    );

  procedure my_proc is new MY_GENERIC_PROC
    generic map (
      test => 2
    );

  function my_func is new MY_GENERIC_FUNC
    generic map (
      test => 2
    );

  procedure my_proc is new My_Generic_Proc
    generic map (
      test => 2
    );

  function my_func is new My_Generic_Func
    generic map (
      test => 2
    );

end package;
