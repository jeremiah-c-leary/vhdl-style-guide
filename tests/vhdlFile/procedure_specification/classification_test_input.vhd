
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

  -- Test parenthesis procedure interface
  procedure proc_3 (signal sig1: in std_logic_vector(3 downto 0));

  procedure proc_3 (constant con1: in std_logic_vector(3 downto 0));

  procedure proc_3 (variable var1: in std_logic_vector(3 downto 0));

  procedure proc_3 (sig1: in std_logic_vector(3 downto 0));

  -- Test default assignments
  procedure proc_4 (
    constant a : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'));
    variable b : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'));
    signal   c : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'))
  ) is
  begin
    b <= a;
  end procedure proc_4;

  -- Test default assignments
  procedure proc_4 (
    variable b : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'));
    signal   c : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'));
    constant a : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'))
  ) is
  begin
    b <= a;
  end procedure proc_4;

  -- Test default assignments
  procedure proc_4 (
    signal   c : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'));
    constant a : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'));
    variable b : in t_slv_array(0 to 1)(7 downto 0) := (others => (others => '0'))
  ) is
  begin
    b <= a;
  end procedure proc_4;

  -- Test parenthesis
  package body demo_pkg is
    procedure demo(any:natural) is
    begin
      func0(a, (proc0(b,c)) = (1 downto 0 => '0'), (others => '0'), d, e);
    end procedure;
  end package body;

begin


end architecture RTL;
