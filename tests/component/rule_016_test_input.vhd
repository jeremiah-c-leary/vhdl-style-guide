
architecture RTl of FIFO is

  component fifo is
    port (
       a : in std_logic
    );
  end component fifo;

  -- Failures below

  component fifo is
    port (
       a : in std_logic
    );

  end component fifo;

  component fifo is
    port (
       a : in std_logic
    );




  end component fifo;

begin

end architecture RTL;
