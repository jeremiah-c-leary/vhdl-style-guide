
architecture RTL of ENT is

begin

   --  Align left = no align paren = no

   n_foo <= resize(unsigned(I_FOO) +
       unsigned(I_BAR), q_foo'length);

   n_foo <=
     resize(unsigned(I_FOO) +
       unsigned(I_BAR), q_foo'length);

   n_bar <= (a or b) and c
     xor z and x or
     w and z;

   n_bar <=
     (a or b) and c
     xor z and x or
     w and z;

   --  Align left = no align paren = yes

   n_foo <= resize(unsigned(I_FOO) +
       unsigned(I_BAR), q_foo'length);

   n_foo <=
     resize(unsigned(I_FOO) +
       unsigned(I_BAR), q_foo'length);

   n_bar <= (a or b) and c
     xor z and x or
     w and z;

   n_bar <=
     (a or b) and c
     xor z and x or
     w and z;

   -- Align left = yes and align paren = no

   n_foo <= resize(unsigned(I_FOO) +
       unsigned(I_BAR), q_foo'length);

   n_foo <=
     resize(unsigned(I_FOO) +
       unsigned(I_BAR), q_foo'length);

   n_bar <= (a or b) and c
     xor z and x or
     w and z;

   n_bar <=
     (a or b) and c
     xor z and x or
     w and z;

   -- Align left = yes and align paren = yes

   n_foo <= resize(unsigned(I_FOO) +
       unsigned(I_BAR), q_foo'length);

   n_foo <=
     resize(unsigned(I_FOO) +
       unsigned(I_BAR), q_foo'length);

   n_bar <= (a or b) and c
     xor z and x or
     w and z;

   n_bar <=
     (a or b) and c
     xor z and x or
     w and z;

   -- Test detection of arrays

   test <= my_function(    arg1      =>   input,
       arg2   =>   input2);

   test <= (    arg1      =>   input,
 arg2   =>   input2);

end architecture RTL;
