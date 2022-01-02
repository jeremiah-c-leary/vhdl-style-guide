
package FIFO_PKG is

  procedure AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES (constant a : in integer; signal b : in std_logic; variable c : in std_logic);

  procedure AVERAGE_SAMPLES (
    constant a : in integer;    -- constant a
    signal b : in std_logic;    -- signal b
    variable ccc : in std_logic -- variable ccc
    -- line starting with comment
  );

  procedure AVERAGE_SAMPLES (
    constant a : in integer; -- constant a
    signal b : in std_logic; -- signal b
    variable ccc : in std_logic); -- variable ccc

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer; -- constant a
    signal b : in std_logic;        -- signal b
    variable ccc : in std_logic   -- variable ccc
  );

  procedure AVERAGE_SAMPLES (
    constant a : in integer;    -- constant a
    signal b : in std_logic;   -- signal b
    variable ccc : in std_logic); -- variable ccc

  procedure AVERAGE_SAMPLES (  -- parameters
    constant a : in integer;
    signal b : in std_logic;
    variable ccc : in std_logic);

end package FIFO_PKG;

package body FIFO_PKG is

  procedure AVERAGE_SAMPLES (
    constant a : in integer;    -- constant a
    signal b : in std_logic;    -- signal b
    variable ccc : in std_logic -- variable ccc
    -- line starting with comment
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES (  -- parameters
    constant a : in integer;
    signal b : in std_logic;
    variable ccc : in std_logic
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer; -- constant a
    signal b : in std_logic;        -- signal b
    variable ccc : in std_logic   -- variable ccc
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

end package body FIFO_PKG;

architecture RTL of ENT is

  procedure AVERAGE_SAMPLES (
    constant a : in integer;    -- constant a
    signal b : in std_logic;    -- signal b
    variable ccc : in std_logic -- variable ccc
    -- line starting with comment
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES (  -- parameters
    constant a : in integer;
    signal b : in std_logic;
    variable ccc : in std_logic
    -- line starting with comment
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer; -- constant a
    signal b : in std_logic;        -- signal b
    variable ccc : in std_logic   -- variable ccc
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

begin

  TEST_PROCESS : process

  procedure AVERAGE_SAMPLES (
    constant a : in integer;    -- constant a
    signal b : in std_logic;    -- signal b
    variable ccc : in std_logic -- variable ccc
    -- line starting with comment
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES ( -- parameters
    constant a : in integer;
    signal b : in std_logic;
    variable ccc : in std_logic
    -- line starting with comment
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer; -- constant a
    signal b : in std_logic;        -- signal b
    variable ccc : in std_logic   -- variable ccc
  ) is
  begin
  end procedure AVERAGE_SAMPLES;

  begin

  end process TEST_PROCESS;

end architecture RTL;

