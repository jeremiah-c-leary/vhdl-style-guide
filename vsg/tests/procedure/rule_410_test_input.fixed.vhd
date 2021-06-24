
package FIFO_PKG is

  procedure AVERAGE_SAMPLES;

  procedure AVERAGE_SAMPLES (constant a : in integer; signal b : in std_logic);

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b   : in std_logic);

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b   : in std_logic);

end package FIFO_PKG;

package body FIFO_PKG is

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b   : in std_logic) is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b   : in std_logic) is
  begin
  end procedure AVERAGE_SAMPLES;

end package body FIFO_PKG;

architecture RTL of ENT is

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b   : in std_logic) is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b   : in std_logic) is
  begin
  end procedure AVERAGE_SAMPLES;

begin

  TEST_PROCESS : process

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b   : in std_logic) is
  begin
  end procedure AVERAGE_SAMPLES;

  -- Violations below this line

  procedure AVERAGE_SAMPLES (
    constant a : in integer;
    signal b   : in std_logic) is
  begin
  end procedure AVERAGE_SAMPLES;

  begin

  end process TEST_PROCESS;

end architecture RTL;
