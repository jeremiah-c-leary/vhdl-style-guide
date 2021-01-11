
architecture RTL of FIFO is

  function PARITY
   (signal X : in std_logic_vector;
    signal Y : out std_logic) return integer;

  impure function PARITY
   (signal X : in std_logic_vector;
    signal Y : out std_logic) return integer;

  pure function PARITY
   (signal X : in std_logic_vector;
    signal Y : out std_logic) return integer;

  function Proc_1 (constant In1: in Integer; variable O1: out Integer) return string;

  function Proc_2 (signal Sig: inout Bit) return string;

  function sum2num(signal a: in signed(3 downto 0);
                    signal b: in signed(3 downto 0);
                    signal sum : out signed (3 downto 0)) return std_logic_vector;

  -- Test parameter keyword
  function Proc_2 parameter (signal Sig: inout Bit) return integer;

  -- Test subprogram header
  function Proc_2
    generic (G1: INTEGER; G2: INTEGER := G1; G3, G4, G5, G6: INTEGER)
    parameter (signal Sig: inout Bit) return natural;

  -- Test subprogram header with generic_map_aspect
  function Proc_2
    generic (G1: INTEGER; G2: INTEGER := G1; G3, G4, G5, G6: INTEGER)
    generic map (complex_fixed_left => 3, complex_fixed_right => -12,
                 complex_fixed_formal_pkg => fixed_dsp_pkg)
    parameter (signal Sig: inout Bit) return string;

begin


end architecture RTL;
