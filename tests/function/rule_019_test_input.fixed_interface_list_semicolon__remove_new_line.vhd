package test_pack is

  function average_samples (
    sample                 : signed;
    constant num_samples   : in integer := 0;
    file my_file           : text;
    variable sample_number : in integer;
    signal sample          : out std_logic
  ) return integer;

  function average_samples (sample : signed; constant num_samples : in integer := 0; file my_file : text; variable sample_number : in integer; signal sample : out std_logic) return integer;

  function average_samples (
    sample : signed; constant num_samples : in integer := 0; file my_file : text; variable sample_number : in integer; signal sample : out std_logic) return integer;

  function average_samples (sample : signed; constant num_samples : in integer := 0; file my_file : text; variable sample_number : in integer; signal sample : out std_logic
  ) return integer;

  function average_samples (
    sample                 : signed;
    constant num_samples   : in integer := 0;
    file my_file           : text;
    variable sample_number : in integer;
    signal sample          : out std_logic) return integer;

  function average_samples
  (
    sample                 : signed;
    constant num_samples   : in integer := 0;
    file my_file           : text;
    variable sample_number : in integer;
    signal sample          : out std_logic) return integer;

  function average_samples (
    sample                 : signed;
    constant num_samples   : in integer := 0;
    file my_file           : text ;
    variable sample_number : in integer;

    signal sample          : out std_logic
  ) return integer;

end package;

package body test_pack is

  function average_samples (
    sample                 : signed;
    constant num_samples   : in integer := 0;
    file my_file           : text;
    variable sample_number : in integer;
    signal sample          : out std_logic
  ) return integer is
  begin
    return sample_number + 1;
  end function;


end package body;
