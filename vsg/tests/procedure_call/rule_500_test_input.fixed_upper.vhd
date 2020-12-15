
architecture rtl of fifo is

begin

  PROCEDURE_CALL_LABEL : postponed wr_en(a, b);

  PROCEDURE_CALL_LABEL : postponed wr_en(a, b);


  process_label : process
  begin

    PROCEDURE_CALL_LABEL : wr_en(a, b);

    PROCEDURE_CALL_LABEL : wr_en(a, b);

  end process;

end architecture rtl;
