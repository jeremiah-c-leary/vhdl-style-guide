
entity FIFO is
  port (
    I_WR_EN : inout std_logic := '0';
    I_DATA  : out   std_logic_vector(31 downto 0) :='1';
    I_RD_EN : in    std_logic :=         '0';
    O_DATA  : out   std_logic_vector(31 downto 0)
  );
end entity FIFO;
