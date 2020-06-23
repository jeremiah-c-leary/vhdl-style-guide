
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

  procedure AVERAGE_SAMPLES is
  begin
  End PROCEDURE AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
  begin
  end procedure AVERAGE_SAMPLES;  

  -- Violations below this line

   procedure AVERAGE_SAMPLES is
 begin
     end procedure AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES (constant x : in integer;
   constant a : in integer;
     signal b : in std_logic;
       variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic) is
  begin
  end procedure AVERAGE_SAMPLES;  

  -- Variations on end of procedure parameter and is keyword

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic)
    is
  begin
  end procedure AVERAGE_SAMPLES;  

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic
  ) is
  begin
  end procedure AVERAGE_SAMPLES;  

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic
  )
  is
  begin
  end procedure AVERAGE_SAMPLES;  

  -- Procedure declarative region

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
  variable var_1 : integer;
      variable var_2 : integer;
  begin
  end procedure AVERAGE_SAMPLES;  

  TEST_PROCESS : process

    procedure test_procedure (
      constant test1_c    : in boolean := true
     ) is
    begin
    end procedure test_procedure;

  begin

  end process TEST_PROCESS;

end package body FIFO_PKG;

architecture RTL of ENT is

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
  variable var_1 : integer;
      variable var_2 : integer;
  begin

    for i in 0 to 7 loop
       done_something <= 0;
    end loop;

    if a = '1' then
      d <= 0;
    end if;

  end procedure AVERAGE_SAMPLES;  

begin

end architecture RTL;
