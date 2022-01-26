
package FIFO_PKG is

  procedure AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES (constant a : in integer := 0; signal b : in std_logic := 'X'; variable c : in std_logic := 'X');

  procedure AVERAGE_SAMPLES (
    constant a : in integer        := 0;
    signal b   : in std_logic      := 'X';
    variable c : in std_logic      := 'X';
    some_sig   : inout t_some_type := '0');

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer          := 0;
    signal b : in std_logic   := 'X';
    variable ccc : in std_logic   := 'X';
    some_sig   : inout t_some_type          := '0');

end package FIFO_PKG;

package body FIFO_PKG is

  procedure AVERAGE_SAMPLES (
    constant a : in integer   := 0;
    signal b   : in std_logic := 'X';
    variable c : in std_logic := 'X') is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer          := 0;
    signal b : in std_logic   := 'X';
    variable ccc : in std_logic   := 'X') is
  begin
  end procedure AVERAGE_SAMPLES;

end package body FIFO_PKG;

architecture RTL of ENT is

  procedure AVERAGE_SAMPLES (
    constant a : in integer   := 0;
    signal b   : in std_logic := 'X';
    variable c : in std_logic := 'X') is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer          := 0;
    signal b : in std_logic   := 'X';
    variable ccc : in std_logic   := 'X') is
  begin
  end procedure AVERAGE_SAMPLES;

begin

  TEST_PROCESS : process

  procedure AVERAGE_SAMPLES (
    constant a : in integer   := 0;
    signal b   : in std_logic := 'X';
    variable c : in std_logic := 'X') is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer          := 0;
    signal b : in std_logic   := 'X';
    variable ccc : in std_logic   := 'X') is
  begin
  end procedure AVERAGE_SAMPLES;

  begin

  end process TEST_PROCESS;

end architecture RTL;
