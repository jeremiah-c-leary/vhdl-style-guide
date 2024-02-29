
architecture rtl of fifo is

begin

  connect_ports(port_1 => data, port_2 => enable, port_3 => overflow, port_4 => underflow);

  connect_ports(port_1 => data, port_2 => enable, port_3 => overflow, port_4 => underflow);

  connect_ports(port_1 => data,port_2 => enable,port_3 => overflow,port_4 => underflow);

  connect_ports(port_1 => data, port_2 => enable, port_3 => overflow, port_4 => underflow
 );

  connect_ports(port_1 => data,port_2 => enable,port_3 => overflow,port_4 => underflow
  );

  connect_ports
  (port_1 => data
    ,port_2 => enable,port_3 => overflow
,port_4 => underflow
  );


  process
  begin

    connect_ports(port_1   => data,port_2=> enable,port_3 => overflow,port_4       => underflow
    );

  end process;

  -- Test without formal part

  connect_ports(data, enable, overflow, underflow);

  connect_ports(data,enable,overflow,underflow
  );

end architecture;
