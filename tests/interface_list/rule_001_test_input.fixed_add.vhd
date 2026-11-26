
entity FIFO is
  generic (
    G_WIDTH : integer := 8;
    G_DEPTH : integer := 16;
  );
  port (
    I_CLK  : in    std_logic;
    O_DATA : out   std_logic_vector(7 downto 0);
  );
end entity FIFO;

entity FIFO is
  generic (
    G_WIDTH : integer := 8;
  );
  port (
    I_CLK  : in    std_logic;
    O_DATA : out   std_logic_vector(7 downto 0); -- comment
    -- trailing comment
  );
end entity FIFO;

architecture RTL of FIFO is

  component FIFO is
    port (
      I_CLK : in    std_logic ;
    );
  end component FIFO;

  procedure proc (
    a : in    integer;
    b : out   integer;
  ) is
  begin
  end procedure proc;

  function func (a : integer; b : integer;) return integer is
  begin
    return a;
  end function func;

  function func2 (a : integer;) return integer;

begin

end architecture RTL;
