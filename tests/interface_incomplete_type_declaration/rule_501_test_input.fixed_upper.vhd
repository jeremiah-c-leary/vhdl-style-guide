
entity fifo is
  generic (
    type GENERIC_DATA_TYPE;
    type GENERIC_DATA_TYPE;
    type GENERIC_DATA_TYPE
  );
  port (
    data_in : generic_data_type
  );
end entity fifo;

architecture rtl of fifo is

  component buffer is
    generic (
      type GENERIC_DATA_TYPE;
      type GENERIC_DATA_TYPE;
      type GENERIC_DATA_TYPE
    );
    port (
        data_in : generic_data_type
    );
  end component buffer;

begin

  buf1 : buffer
    generic map (
        generic_data_type => std_logic
    )
    port map (
        data_in => '0'
    );

end architecture rtl;
