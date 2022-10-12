
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

   O_FOO <=
     (
   1 => func1(std_logic_vector(G_GEN1), G_GEN2),
               2 => func2(func3(G_GEN3), G_GEN3),
3 => func4(G_GEN4)
 );

end architecture RTL;
