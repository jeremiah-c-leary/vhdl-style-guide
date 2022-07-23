
-- This is a single-line comment

/* This is a delimited comment */

/*
This
is

a
delimited -- something
     
comment
*/

/*/* This is a /* delimited comment */

architecture RTL of FIFO is

  signal fifo_wr : std_logic; /* This is
   a delimited
  comment
  */

begin

end architecture RTL;
