
package pkg is

  PROCEDURE my_proc is new my_generic_proc
    generic map (
      test => 2
    );

end package;

architecture RTL of FIFO is

  procedure proc1 is begin end procedure proc1;

  PROCEDURE PROC1 IS BEGIN END PROCEDURE PROC1;

begin

end architecture RTL;
