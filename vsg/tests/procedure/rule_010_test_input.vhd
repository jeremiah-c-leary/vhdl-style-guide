
package FIFO_PKG is

  procedure AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic);

  -- Violations below this line

    procedure AVERAGE_SAMPLES;

   procedure AVERAGE_SAMPLES (
   constant a : in integer;
       signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic);

end package FIFO_PKG;

package body FIFO_PKG is

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
    signal sig1 : std_logic;
    file file1 : something;
    variable var1 : integer;
  begin
  end procedure AVERAGE_SAMPLES;  

  procedure AVERAGE_SAMPLES (constant x : in integer;
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
    signal   sig1 : std_logic;
    file     file1 : something;
    variable var1 : integer;
  begin
  end procedure AVERAGE_SAMPLES;  

  -- Variations on end of procedure parameter and is keyword

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic)
    is
    signal   sig1 : std_logic;
    file     file1 : something;
    variable var1 : integer;
  begin
  end procedure AVERAGE_SAMPLES;  

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic
  ) is
    signal   sig1 : std_logic;
    file     file1 : something;
    variable var1 : integer;
  begin
  end procedure AVERAGE_SAMPLES;  

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic
  )
  is
    signal   sig1 : std_logic;
    file     file1 : something;
    variable var1 : integer;
  begin
  end procedure AVERAGE_SAMPLES;  


end package body FIFO_PKG;

architecture RTL of ENT is

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
    signal sig1 : std_logic;
    file file1 : something;
    variable var1 : integer;
  begin
  end procedure AVERAGE_SAMPLES;  

  procedure AVERAGE_SAMPLES (constant x : in integer;
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
    signal   sig1 : std_logic;
    file     file1 : something;
    variable var1 : integer;
  begin
  end procedure AVERAGE_SAMPLES;  

begin

  TEST_PROCESS : process

    procedure AVERAGE_SAMPLES (
      constant a : in integer;
      signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
      signal d : out std_logic) is
      signal sig1 : std_logic;
      file file1 : something;
      variable var1 : integer;
    begin
    end procedure AVERAGE_SAMPLES;  

  begin

  end process TEST_PROCESS;

  TEST_PROCESS : process

    procedure AVERAGE_SAMPLES (constant x : in integer;
      constant a : in integer;
      signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
      signal d : out std_logic) is
        signal     sig1 : std_logic;
        file     file1 : something;
        variable var1 : integer;
    begin
    end procedure AVERAGE_SAMPLES;  

  begin

  end process TEST_PROCESS;


end architecture RTL;
