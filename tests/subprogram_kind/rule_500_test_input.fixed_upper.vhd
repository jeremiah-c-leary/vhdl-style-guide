
package pkg is

  PROCEDURE my_proc is new my_generic_proc
    generic map (
      test => 2
    );

  PROCEDURE my_proc is new my_generic_proc
    generic map (
      test => 2
    );

  PROCEDURE my_proc is new my_generic_proc
    generic map (
      test => 2
    );

end package;

architecture RTL of FIFO is

  procedure proc1 is begin end PROCEDURE proc1;

  procedure proc1 is begin end PROCEDURE proc1;

  procedure proc1 is begin end PROCEDURE proc1;

begin

end architecture RTL;
