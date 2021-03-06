
architecture RTL of ENT is

begin

   -- These should pass the check
   O_FOO <= (1 => q_foo(63 downto 32),
             0 => q_foo(31 downto  0));

   n_foo <= resize(unsigned(I_FOO) +
                   unsigned(I_BAR), q_foo'length);
   -- These should fail the check
   O_FOO <= (1 => q_foo(63 downto 32),
             0 => q_foo(31 downto  0));

   n_foo <= resize(unsigned(I_FOO) +
                   unsigned(I_BAR), q_foo'length);

end architecture RTL;
