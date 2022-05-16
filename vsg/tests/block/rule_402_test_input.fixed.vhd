
architecture RTL of FIFO is

begin

  BLOCK_LABEL : block is

    attribute mark_debug of wr_en        : signal is "true";
    attribute mark_debug of almost_empty : signal is "true";
    attribute mark_debug of full         : signal is "true";

  begin
  end block BLOCK_LABEL;

end architecture RTL;
