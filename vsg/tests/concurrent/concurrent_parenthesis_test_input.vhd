
architecture RTL of ENT is

begin

   -- These should pass the check
   wr_en <= '0' when q_wr_en = '1' else
            '1';

   w_foo <= I_FOO when ((I_BAR = '1') and
                        (I_CRUFT = '1')) else
            '0';

   O_FOO <= (1 => q_foo(63 downto 32),
             0 => q_foo(31 downto  0));

   n_foo <= resize(unsigned(I_FOO) +
                   unsigned(I_BAR), q_foo'length);

   w_foo <= I_FOO when ((I_BAR = 1 or (I_STUFF = 0 and
                                       I_CRUFT = 1) or
                         I_BLAH = 10));

   w_foo <= I_FOO when (I_BAR = 1 or ((I_STUFF = 0 and
                                       (I_CRUFT = 1 or I_BLAH = 10)
                                       and I_GRUB = 20) or
                                      I_STUB = 45)
                        and I_HUB = 23);

   -- These should fail the check
   wr_en <= '0' when q_wr_en = '1' else
        '1';

   w_foo <= I_FOO when ((I_BAR = '1') and
            (I_CRUFT = '1')) else
            '0';

   O_FOO <= (1 => q_foo(63 downto 32),
            0 => q_foo(31 downto  0));

   n_foo <= resize(unsigned(I_FOO) +
            unsigned(I_BAR), q_foo'length);

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

end architecture RTL;
