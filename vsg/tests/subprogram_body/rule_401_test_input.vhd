architecture arc of ent is

    signal a : std_logic_vector(7 downto 0);
    signal b : std_logic_vector(7 downto 0);

    procedure rst_procedure is

      attribute mark_debug of wr_en : signal is "true";
      attribute mark_debug of almost_empty : signal is "true";
      attribute mark_debug of full : signal is "true";

    begin
    end procedure;

begin

    proc_p : process (clk_i, rst_n_i)
        procedure rst_procedure is

          attribute mark_debug of wr_en : signal is "true";
          attribute mark_debug of almost_empty : signal is "true";
          attribute mark_debug of full : signal is "true";

        begin
        end procedure;

        procedure rst_procedure is

          attribute mark_debug of wr_en : signal is "true";
          attribute mark_debug of almost_empty : signal is "true";
          attribute mark_debug of full : signal is "true";

        begin
        end procedure;

        procedure rst_procedure is

          attribute mark_debug of wr_en : signal is "true";
          attribute mark_debug of almost_empty : signal is "true";
          attribute mark_debug of full : signal is "true";

        begin
        end procedure;

    begin
    end process proc_p;

end architecture arc;

package body my_package is

  procedure rst_procedure is

    attribute mark_debug of wr_en : signal is "true";
    attribute mark_debug of almost_empty : signal is "true";
    attribute mark_debug of full : signal is "true";

  begin
  end procedure;

  procedure rst_procedure is

    attribute mark_debug of wr_en : signal is "true";
    attribute mark_debug of almost_empty : signal is "true";
    attribute mark_debug of full : signal is "true";

  begin
  end procedure;

end package body;
