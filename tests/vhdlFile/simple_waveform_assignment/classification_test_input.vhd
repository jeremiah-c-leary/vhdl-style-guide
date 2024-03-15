
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    FORCE_LABEL : sig1 <= transport a and c;

    FORCE_LABEL : sig1 <= a and c;

    sig1 <= a and c;

    check_value(to_integer(unsigned(v_normalized_chan)) <= config.max_channel, TB_FAILURE, "Sanity check: Check that channel number is supported.", scope, ID_NEVER, msg_id_panel, proc_call);
  
  end process;

end architecture RTL;
