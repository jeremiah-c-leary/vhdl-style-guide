
architecture RTL of FIFO is

  procedure rst_procedure is

    attribute mark_debug of wr_en : signal is "true";
    attribute mark_debug of almost_empty : signal is "true";
    attribute mark_debug of full : signal is "true";

  begin
  end procedure;

begin

  PROC_1 : process

    attribute mark_debug of wr_en : signal is "true";
    attribute mark_debug of almost_empty : signal is "true";
    attribute mark_debug of full : signal is "true";

    procedure rst_procedure is

      attribute mark_debug of wr_en : signal is "true";
      attribute mark_debug of almost_empty : signal is "true";
      attribute mark_debug of full : signal is "true";

    begin
    end procedure;

  begin

  end process;

end architecture RTL;
