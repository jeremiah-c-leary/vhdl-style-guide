
architecture rtl of fifo is

  type t_some_record is record
    element_1           : natural;
    some_other_element  : natural;
    yet_another_element : natural;
  end record;

  --Violations below

  type t_some_record is record
    element_1           : natural;
    some_other_element  : natural;
    yet_another_element : natural;
  end record;

  type t_some_record is record
    element_1           : natural;
    some_other_element  : natural;
    yet_another_element : natural;
  end record;

begin

end architecture rtl;
