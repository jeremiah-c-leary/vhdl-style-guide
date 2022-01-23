
package body my_pkg is

  procedure some_proc (
    a : integer;
    b : integer
  ) is

    constant some_const : integer_vector :=
       some_proc(
         arg1, arg2, arg3, arg4,
         arg5, arg6, arg7
        ) ;
    variable a, b, c, d, e, f, g : integer;
    constant some_const          : integer_vector :=
                                                     some_proc(
                                                                arg1, arg2, arg3, arg4,
                                                                arg5, arg6, arg7
                                                               );
  begin

    some_var       := other_proc(a, b, c
                                 d, e, f, g, h
                                 i, j, k, l, m
                               );
    some_other_var := other_other_proc(z);

  end procedure some_proc;

end package body my_pkg;
