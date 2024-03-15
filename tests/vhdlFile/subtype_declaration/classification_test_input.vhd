
architecture RTL of FIFO is


  subtype DIGITS is INTEGER range 0 to 9;

  subtype BIT_NEW is RESOLVE_VALUE BIT;

  -- EXAMPLE 1 : a resolved subtype
  subtype MY_STD_LOGIC is Resolved Std_ulogic;

  -- EXAMPLE 2: an integer subtype
  subtype MyBit is STD_LOGIC range '0' to '1';

  -- EXAMPLE 3 : an array subtype
  subtype ShortVector is STD_LOGIC_VECTOR(1 downto 0);

  subtype new_std_logic is (resolved) std_ulogic;

  -- Example 4 : subtype in subtype declaration
  subtype identifier is type_mark(type_mark(blah));

  subtype identifier is type_mark(type_mark
    (
     blah
    )
  );

  subtype t_data_axi_stream_m2s is t_axi_stream_m2s(
      st_keep(T_AXI_RANGE)
  );

  subtype t_data_axi_stream_m2s is t_axi_stream_m2s(
      st_strb2(0 downto 0),
      st_keep(T_AXI_RANGE)
  );

begin

end architecture RTL;
