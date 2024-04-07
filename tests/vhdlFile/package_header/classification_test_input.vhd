
-- Test generic clause
package PACK1 is

  generic (
    -- Test constants
    constant con1, con2 : in std_logic := 0;
    constant con1, con2 : std_logic := 0;
    constant con1, con2 : in std_logic;
    constant con1, con2 : std_logic;

    -- Test signals
    signal sig1, sig2 : in      std_logic bus := 0;
    signal sig1, sig2 : out     std_logic bus := 0;
    signal sig1, sig2 : inout   std_logic bus := 0;
    signal sig1, sig2 : buffer  std_logic bus := 0;
    signal sig1, sig2 : linkage std_logic bus := 0;

    signal sig1, sig2 : in      std_logic bus;
    signal sig1, sig2 : out     std_logic bus;
    signal sig1, sig2 : inout   std_logic bus;
    signal sig1, sig2 : buffer  std_logic bus;
    signal sig1, sig2 : linkage std_logic bus;

    signal sig1, sig2 : std_logic bus := 0;
    signal sig1, sig2 : std_logic bus := 0;
    signal sig1, sig2 : std_logic bus := 0;
    signal sig1, sig2 : std_logic bus := 0;
    signal sig1, sig2 : std_logic bus := 0;

    signal sig1, sig2 : std_logic := 0;
    signal sig1, sig2 : std_logic := 0;
    signal sig1, sig2 : std_logic := 0;
    signal sig1, sig2 : std_logic := 0;
    signal sig1, sig2 : std_logic := 0;

    signal sig1, sig2 : std_logic;
    signal sig1, sig2 : std_logic;
    signal sig1, sig2 : std_logic;
    signal sig1, sig2 : std_logic;
    signal sig1, sig2 : std_logic;

    -- Test signals
    variable sig1, sig2 : in      std_logic := 0;
    variable sig1, sig2 : out     std_logic := 0;
    variable sig1, sig2 : inout   std_logic := 0;
    variable sig1, sig2 : buffer  std_logic := 0;
    variable sig1, sig2 : linkage std_logic := 0;

    variable sig1, sig2 : in      std_logic ;
    variable sig1, sig2 : out     std_logic ;
    variable sig1, sig2 : inout   std_logic ;
    variable sig1, sig2 : buffer  std_logic ;
    variable sig1, sig2 : linkage std_logic ;

    variable sig1, sig2 : std_logic := 0;
    variable sig1, sig2 : std_logic := 0;
    variable sig1, sig2 : std_logic := 0;
    variable sig1, sig2 : std_logic := 0;
    variable sig1, sig2 : std_logic := 0;

    variable sig1, sig2 : std_logic;
    variable sig1, sig2 : std_logic;
    variable sig1, sig2 : std_logic;
    variable sig1, sig2 : std_logic;
    variable sig1, sig2 : std_logic;

    -- Test unknown
    sig1, sig2 : in      std_logic bus := 0;
    sig1, sig2 : out     std_logic bus := 0;
    sig1, sig2 : inout   std_logic bus := 0;
    sig1, sig2 : buffer  std_logic bus := 0;
    sig1, sig2 : linkage std_logic bus := 0;

    sig1, sig2 : in      std_logic bus;
    sig1, sig2 : out     std_logic bus;
    sig1, sig2 : inout   std_logic bus;
    sig1, sig2 : buffer  std_logic bus;
    sig1, sig2 : linkage std_logic bus;

    sig1, sig2 : std_logic bus := 0;
    sig1, sig2 : std_logic bus := 0;
    sig1, sig2 : std_logic bus := 0;
    sig1, sig2 : std_logic bus := 0;
    sig1, sig2 : std_logic bus := 0;

    sig1, sig2 : std_logic := 0;
    sig1, sig2 : std_logic := 0;
    sig1, sig2 : std_logic := 0;
    sig1, sig2 : std_logic := 0;
    sig1, sig2 : std_logic := 0;

    sig1, sig2 : std_logic;
    sig1, sig2 : std_logic;
    sig1, sig2 : std_logic;
    sig1, sig2 : std_logic;
    sig1, sig2 : std_logic;

    -- Test files
    file fil1, fil2 : std_logic;
    file fil1, fil2 : std_logic;

    -- Test Types
    type typ1;
    type typ1;

    -- Test Procedures
    procedure proc1 parameter (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) is proc_name;

    procedure proc1 parameter (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) is <>;

    procedure proc1 (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) is proc_name;

    procedure proc1 (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) is <>;

    procedure proc1 is proc_name;

    procedure proc1 is <>;

    procedure proc1;

    -- Test functions
    pure function funct1 parameter (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) return boolean is <>;

    pure function funct1 parameter (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) return boolean is func1;

    impure function funct1 parameter (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) return boolean is <>;

    impure function funct1 parameter (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) return boolean is func1;

    -- Remove Parameter
    pure function funct1 (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) return boolean is <>;

    pure function funct1 (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) return boolean is func1;

    impure function funct1 (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) return boolean is <>;

    impure function funct1 (
      signal sig1, sig2 : in      std_logic bus := 0;
      constant con1, con2 : in std_logic := 0;
      variable sig1, sig2 : in      std_logic := 0;
      sig1, sig2 : in      std_logic bus := 0;
      file fil1, fil2 : std_logic;
      type typ1) return boolean is func1;

    -- Remove formal_parameter_list
    pure function funct1 return boolean is <>;

    pure function funct1 return boolean is func1;

    impure function funct1 return boolean is <>;

    impure function funct1 return boolean is func1;

    -- Remove interface_subprogram_default
    pure function funct1 return boolean;

    pure function funct1 return boolean;

    impure function funct1 return boolean;

    impure function funct1 return boolean

    );

    generic map (
       A => B,
       C => D,
       E, F
    );

end package PACK1;
