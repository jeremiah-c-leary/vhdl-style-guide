
architecture RTL of ENT is

begin

   -- These should pass the check
   wr_en <= '0' when q_wr_en = '1' else
            '1';

   w_foo <= I_FOO when ((I_BAR = '1') and
                        (I_CRUFT = '1')) else
            '0';

   w_foo <= I_FOO when ((I_BAR = 1 or (I_STUFF = 0 and
                                       I_CRUFT = 1) or
                         I_BLAH = 10)) else
            I_BAR;

   w_foo <= I_FOO when (I_BAR = 1 or ((I_STUFF = 0 and
                                       (I_CRUFT = 1 or I_BLAH = 10)
                                       and I_GRUB = 20) or
                                      I_STUB = 45)
                        and I_HUB = 23) else
            I_BAR;

   hbusreq_t <= '1' when
                         (
                          (dma_count>0 and mst_state=req_phase) or
                          (dma_count>1 and (mst_state=addr or mst_state=addr_data))
                         ) else
                '0';

   hbusreq_t <= '1' when
                         (dma_count>0 and mst_state=req_phase) or
                         (dma_count>1 and (mst_state=addr or mst_state=addr_data))
                         else
                '0';

   fifo_reset <= '1' when (
                           (mst_state=error_phase) or
                           (mst_in.hresp=ok_resp and r_mst_out.htrans/=busy and r_mst_out.hwrite='1' and mst_in.hready='1' and mst_state=data and dma_count=0)
                          ) else '0';

   -- These should fail the check
   wr_en <= '0' when q_wr_en = '1' else
         '1';

   w_foo <= I_FOO when ((I_BAR = '1') and
            (I_CRUFT = '1')) else
            '0';

   w_foo <= I_FOO when ((I_BAR = 1 or (I_STUFF = 0 and
                                         I_CRUFT = 1) or
                    I_BLAH = 10));

   w_foo <= I_FOO when (I_BAR = 1 or ((I_STUFF = 0 and
                                 (I_CRUFT = 1 or I_BLAH = 10)
                                            and I_GRUB = 20) or
            I_STUB = 45)
                                 and I_HUB = 23);

   w_foo <= I_FOO when (I_BAR = 1 or ((I_STUFF = 0 and
                           (I_CRUFT = 1 or
                                                    I_BLAH = 10)
                  and I_GRUB = 20) or
                                                 I_STUB = 45)
 and I_HUB = 23);

   hbusreq_t <= '1' when
(
(dma_count>0 and mst_state=req_phase) or
(dma_count>1 and (mst_state=addr or mst_state=addr_data))
) else
'0';

   fifo_reset <= '1' when (
(mst_state=error_phase) or
(mst_in.hresp=ok_resp and r_mst_out.htrans/=busy and r_mst_out.hwrite='1' and mst_in.hready='1' and mst_state=data and dma_count=0)
) else
                 '0';

end architecture RTL;
