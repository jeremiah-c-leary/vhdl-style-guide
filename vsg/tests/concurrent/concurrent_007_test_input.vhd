

architecture RTL of ENTITY1 is


begin

  -- These should pass with "allow_single_line" option enabled
  -- These should fail with "allow_single_line" option disabled
  O_FOO <= w_foo when (w_foo_en = '1') else 'Z';
  O_BAR <= w_bar when (w_bar_en = '0') else '1';
  O_BAR <= w_bar when (w_bar_en = '1') else
           '0';

  -- These should fail with "allow_single_line" option enabled
  O_FOO <= w_foo when (w_foo_en = '1') else w_bar when (w_bar_en = '1') else 'Z'; 
  O_FOO <= w_foo when (w_foo_en = '1') else w_bar when (w_bar_en = '1') else
           'Z'; 

end architecture RTL;
