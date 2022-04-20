

library ieee;


  use ieee.std_logic_1164.all;



architecture rtl of fifo is




  signal a : std_logic;




  constant b : std_logic;



  component my_comp is


    generic (


      G_GENERIC : std_logic


   );



   port (


     I_INPUT : in std_logic;


     O_OUTPUT : out std_logic


  );


  end component;



begin


  a <= b;




  c <= d;


end architecture rtl;

architecture rtl of fifo is

  signal sig1 : std_logic;

begin

end architecture;

