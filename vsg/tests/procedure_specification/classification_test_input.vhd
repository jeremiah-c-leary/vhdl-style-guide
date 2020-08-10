
architecture RTL of FIFO is



  procedure PARITY
   (signal X : in std_logic_vector;
    signal Y : out std_logic);

  procedure Proc_1 (constant In1: in Integer; variable O1: out Integer);

  procedure Proc_2 (signal Sig: inout Bit);

  procedure sum2num(signal a: in signed(3 downto 0); 
                    signal b: in signed(3 downto 0);
                    signal sum : out signed (3 downto 0));

  -- Test parameter keyword
  procedure Proc_2 parameter (signal Sig: inout Bit);

  -- Test subprogram header
  procedure Proc_2
    generic (G1: INTEGER; G2: INTEGER := G1; G3, G4, G5, G6: INTEGER)
    parameter (signal Sig: inout Bit);

  -- Test subprogram header with generic_map_aspect
  procedure Proc_2
    generic (G1: INTEGER; G2: INTEGER := G1; G3, G4, G5, G6: INTEGER)
    generic map (complex_fixed_left => 3, complex_fixed_right => -12,
                 complex_fixed_formal_pkg => fixed_dsp_pkg)
    parameter (signal Sig: inout Bit);

begin


end architecture RTL;
