architecture arc of ent is

    signal a : std_logic_vector(7 downto 0);
    signal b : std_logic_vector(7 downto 0);

    procedure rst_procedure is
    begin
        a <= (others => '0');
        b <= (others => '0');
        c := d;
    end procedure;

    procedure rst_procedure is
    begin
        a <= (others => '0');
        b <= (others => '0');
        c := d;
    end procedure;

begin

    proc_p : process (clk_i, rst_n_i)
        procedure rst_procedure is
        begin
            a <= (others => '0');
            b <= (others => '0');
            c := d;
        end procedure;

        procedure rst_procedure is
        begin
            a <= (others => '0');
            b <= (others => '0');
            c := d;
        end procedure;

        procedure rst_procedure is
        begin
            a <= (others => '0');
            b <= (others => '0');
            c := d;
        end procedure;

    begin
        if rst_n_i = '0' then
            rst_procedure;
        elsif rising_edge(clk_i) then
            a <= (others => '1');
            b    <= (others => '1');
            c  := d;
        end if;
    end process proc_p;

end architecture arc;

package body my_package is

  procedure rst_procedure is
  begin
      a <= (others => '0');
      b <= (others => '0');
      c := d;
  end procedure;

  procedure rst_procedure is
  begin
      a <= (others => '0');
      b <= (others => '0');
      c := d;
  end procedure;

end package body;
