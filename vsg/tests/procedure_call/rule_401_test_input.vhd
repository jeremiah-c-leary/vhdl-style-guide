
architecture rtl of fifo is

begin

  -- Valid formatting
  connect_ports(
    port_1 => data,
    port_2 => enable,
    port_3 => overflow,
    port_4 => underflow
  );

  -- Invalid formatting

  process
  begin

    connect_ports(
      port_1   => data,
      port_2=> enable,
      port_3 => overflow,
      port_4       => underflow
    );

  end process;

  connect_ports(
    port_1=> data,
    port_2 => enable,
    port_3     => overflow,
    port_4   => underflow
  );

end architecture;
