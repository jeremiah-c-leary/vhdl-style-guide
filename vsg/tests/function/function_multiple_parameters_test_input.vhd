
architecture ARCH of ENTITY_1 is

  function func_1 (a : integer; b : integer;
             c : unsigned(3 downto 0);
     signal d : std_logic_vector(7 downto 0);
       constant e : std_logic) return integer is
  begin

  end;

begin

end architecture ARCH;

package TEST_PKG is

  function func_1 (
    constant a : integer;
    signal b : integer;
    signal c : unsigned(3 downto 0);
    signal d : std_logic_vector(7 downto 0);
    constant e : std_logic)
  return integer is

end package TEST_PKG;
