architecture RTL of ENTITY1 is

  signal instruction : bit_vector(15 downto 0);
  alias opcode : bit_vector(3 downto 0) is instruction(15 downto 12);

  signal data : std_logic_vector(OPCODE'range);

begin

  data <= OpCode;

  PROC_NAME : process () is
  begin

    data <= OpCOde;

    if (opCODE = "0110") then
      data <= opcode;
    end if;

  end process PROC_NAME;

end architecture RTL;

