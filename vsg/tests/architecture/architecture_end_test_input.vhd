
architecture RTL of FIFO is

  component comp_a is
    port (
      end_signal : in std_logic;
      endsignal : in std_logic
    );
  end component comp_a;

begin

  endPort <= w_sig1;
  end_port <= w_sig1;

  u_compa : comp_a
    port map (
      end_signal => w_sig1,
      ENDAT_DATA_RC => endat_DATA_RC,
      endsignal => w_sig2
    );

  END_PROC : process () is
  begin
  end process END_PROC;

  ENDPROC : process () is
  begin
  end process ENDPROC;

end architecture RTL;

