
package body RTL is
  type t_my_type is protected body
    attribute mark_debug of wr_en : signal is "true";
    attribute mark_debug of almost_empty : signal is "true";
    attribute mark_debug of full : signal is "true";

    procedure rst_procedure is

      attribute mark_debug of wr_en : signal is "true";
      attribute mark_debug of almost_empty : signal is "true";
      attribute mark_debug of full : signal is "true";

    begin
    end procedure;
  end protected body;
end package body RTL;
