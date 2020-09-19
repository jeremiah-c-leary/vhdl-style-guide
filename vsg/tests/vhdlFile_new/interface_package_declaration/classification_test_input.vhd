
-- Test generic clause
package PACK1 is

  generic ( 

    package pack1 is new fifostuff generic map (<>);

    package pack1 is new fifostuff generic map (default);

    package pack1 is new fifostuff generic map ( A => B, C => D)


    );

    
end package PACK1;
