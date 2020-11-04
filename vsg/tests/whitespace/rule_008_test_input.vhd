
entity FIFO is
  port (
    READ : std_logic_vector(3 downto 0)
  );
end;


architecture RTL of FIFO is

    signal data : std_logic_vector(3 downto 0);

begin

end architecture RTL;

-- Violations below

entity FIFO is
  port (
    READ : std_logic_vector   (3 downto 0)
  );
end;


architecture RTL of FIFO is

    signal data : std_logic_vector (3 downto 0);

begin

end architecture RTL;
