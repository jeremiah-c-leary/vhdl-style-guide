
-- Test generic clause
package PACK1 is

  generic (

    -- Test function
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

    impure function funct1 return boolean;

    -- Remove pure/impure
    function funct1 return boolean;

    function funct1 return boolean;

    function funct1 return boolean;

    function funct1 return boolean

    );


end package PACK1;
