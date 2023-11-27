
architecture RTL of FIFO is

  type state_machine is (idle, write, read, done);

begin

  state <= idle;
  state <= write;
  state <= read;
  state <= done;

  state <= IDLE;
  state <= Write;
  state <= ReAd;
  state <= dONe;

end architecture RTL;
