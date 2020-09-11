
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    -- Test all possible combinations

    WAIT_LABEL : wait on sig1, sig2, sig3 until some condition met for some time_expression;

    WAIT_LABEL : wait on sig1, sig2, sig3 until some condition met;

    WAIT_LABEL : wait on sig1, sig2, sig3 for some time_expression;

    WAIT_LABEL : wait on sig1, sig2, sig3;

    WAIT_LABEL : wait until some condition met for some time_expression;

    WAIT_LABEL : wait until some condition met;

    WAIT_LABEL : wait for some time_expression;

    WAIT_LABEL : wait;

    -- Test without a label

    wait on sig1, sig2, sig3 until some condition met for some time_expression;

    wait on sig1, sig2, sig3 until some condition met;

    wait on sig1, sig2, sig3 for some time_expression;

    wait on sig1, sig2, sig3;

    wait until some condition met for some time_expression;

    wait until some condition met;

    wait for some time_expression;

    wait;

  end process;

end architecture RTL;
