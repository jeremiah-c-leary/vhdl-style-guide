
entity b is
  port (
    c : in    std_logic_vector(7       downto 0)
  );
end entity b;

architecture a of b is

  type my_array2 is array (natural range 0      to 7) of std_logic_vector(7   downto 0);

  subtype my_array3 is my_array2(open)(7   downto 0);

  subtype my_array4 is natural range 0      to 7;

begin

  x <= y(7     downto 0);

end architecture a;
