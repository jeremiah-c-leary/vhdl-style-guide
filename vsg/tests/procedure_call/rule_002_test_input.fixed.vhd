
architecture rtl of fifo is

begin

  postponed wr_en(a, b);

  wr_en(a, b);

  process_label : process
  begin

    procedure_call_label : wr_en(a, b);

  end process;

end architecture rtl;
