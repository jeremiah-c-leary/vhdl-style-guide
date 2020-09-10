
architecture RTL of FIFO is

  function PARITY is new uninstantiated_subprogram_name [name1, name2 return integer]
    generic map (
      GEN1 => 3,
      GEN2 => 4,
      GEN5 => 6
    );

  function PARITY is new uninstantiated_subprogram_name
    generic map (
      GEN1 => 3,
      GEN2 => 4,
      GEN5 => 6
    );

  function PARITY is new uninstantiated_subprogram_name [name1, name2 return integer];

  function PARITY is new uninstantiated_subprogram_name;


  procedure PARITY is new uninstantiated_subprogram_name [name1, name2 return integer]
    generic map (
      GEN1 => 3,
      GEN2 => 4,
      GEN5 => 6
    );

  procedure PARITY is new uninstantiated_subprogram_name
    generic map (
      GEN1 => 3,
      GEN2 => 4,
      GEN5 => 6
    );

  procedure PARITY is new uninstantiated_subprogram_name [name1, name2 return integer];

  procedure PARITY is new uninstantiated_subprogram_name;

begin


end architecture RTL;
