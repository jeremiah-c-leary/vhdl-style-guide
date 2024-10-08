
architecture RTL of FIFO is

  alias ident is << constant dut.test : std_logic >>;

  alias ident is << signal dut.test : std_logic >>;

  alias ident is << variable dut.test : std_logic >>;

begin

  probe_signal <= << constant some.hierarchy : std_logic >> or
                  << signal some.hieararchy : std_logic >> or
                  << variable some.hierarchy : std_logic >>;

  process (<< constant some.hierarchy : std_logic >>,
           << signal some.hieararchy : std_logic >>,
           << variable some.hierarchy : std_logic >>) is
  begin

    probe_signal <= << constant some.hierarchy : std_logic >> or
                    << signal some.hieararchy : std_logic >> or
                    << variable some.hierarchy : std_logic >>;

    if << constant some.hierarchy : std_logic >> or
                    << signal some.hieararchy : std_logic >> or
                    << variable some.hierarchy : std_logic >> then

    elsif << constant some.hierarchy : std_logic >> or
                    << signal some.hieararchy : std_logic >> or
                    << variable some.hierarchy : std_logic >> then
    else

        sig1 := func(<< signal some.hierarchy : std_logic >>, << signal some.hierarchy : std_logic >>, << variable some.hierarchy : std_logic >>);

        var1 := func(<< signal some.hierarchy : std_logic >>, << signal some.hierarchy : std_logic >>, << variable some.hierarchy : std_logic >>);

    end if;

    case << signal some.hierarchy : std_logic >> & << signal some.hierarchy : std_logic >> & << variable some.hierarchy : std_logic >> is
    end case;

  end process;

  -- Test external names with indexes

  probe_signal <= << constant some.hierarchy.hier(i) : std_logic >> or
                  << signal some.hieararchy(i) : std_logic >> or
                  << variable some.hierarchy.ab.cd.(i) : std_logic >>;

end architecture RTL;
