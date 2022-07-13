
architecture rtl of fifo is

begin

  connect_ports(port_1 => data, port_2 => enable, port_3 => overflow, port_4 => underflow);

  connect_ports(
 port_1 => data, port_2 => enable, port_3 => overflow, port_4 => underflow);

  connect_ports(port_1 => data,
 port_2 => enable,
 port_3 => overflow,
 port_4 => underflow);

  connect_ports(port_1 => data, port_2 => enable, port_3 => overflow, port_4 => underflow
 );

  connect_ports(
    port_1 => data,
    port_2 => enable,
    port_3 => overflow,
    port_4 => underflow
  );

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

end architecture;
