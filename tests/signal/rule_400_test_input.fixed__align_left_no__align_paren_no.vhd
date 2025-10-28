architecture rtl of fifo is

  signal sig8 : record_type_3(
                              element1(7 downto 0),
                              element2(4 downto 0)(7 downto 0)
                              (
                                elementA(7 downto 0),
                                elementB(3 downto 0)
                              ),
                              element3(3 downto 0)(
                                elementC(4 downto 1),
                                elementD(1 downto 0)),
                              element5(
                                elementE(3 downto 0)(6 downto 0),
                                elementF(7 downto 0)
                              ),
                              element6(4 downto 0),
                              element7(7 downto 0)
                             );

  signal s : MY_TYPE := (
                    a => '0',
                                ddddd => (others => '0'),
                            ffff => (others => '0')
                );

  signal AxiMs : axi_ms_t (ar_id(IdRange_c), aw_id(IdRange_c),
                           ar_addr(AddrRange_c), aw_addr(AddrRange_c),
                           ar_user(UserRange_c), aw_user(UserRange_c), w_user(UserRange_c),
                           w_data(DataRange_c),
                           w_strb(ByteRange_c));

  signal AxiSm : axi_sm_t (r_id(IdRange_c), b_id(IdRange_c),
                           r_user(UserRange_c), b_user(UserRange_c),
                           r_data(DataRange_c));

begin

end architecture rtl;
