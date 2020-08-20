library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
 
entity example_generate is
  generic (
    g_DEBUG      : natural := 1        -- 0 = no debug, 1 = print debug
    );
end example_generate;
 
architecture behave of example_generate is
 
  signal r_VECTOR : std_logic_vector(15 downto 0) := (others => '0');
 
  signal w_VECTOR_MSB_1 : std_logic_vector(7 downto 0);
  signal w_VECTOR_MSB_2 : std_logic_vector(7 downto 0);
 
  signal w_VECTOR_TEST : std_logic_vector(15 downto 0);
   
begin
   
  -- Demonstrates Use Case #1: Replicating Logic
  -- Stores just the most significant byte in a new signal
  g_GENERATE_FOR: for ii in 0 to 7 generate
--    w_VECTOR_MSB_1(ii) <= r_VECTOR(ii+8);
  end generate g_GENERATE_FOR;
   
  -- This code has the same effect as above
  -- But the above is more compact, easier to read, and less error prone!
--  w_VECTOR_MSB_2(0) <= r_VECTOR(8);
--  w_VECTOR_MSB_2(1) <= r_VECTOR(9);
--  w_VECTOR_MSB_2(2) <= r_VECTOR(10);
--  w_VECTOR_MSB_2(3) <= r_VECTOR(11);
--  w_VECTOR_MSB_2(4) <= r_VECTOR(12);
--  w_VECTOR_MSB_2(5) <= r_VECTOR(13);
--  w_VECTOR_MSB_2(6) <= r_VECTOR(14);
--  w_VECTOR_MSB_2(7) <= r_VECTOR(15);
  
  -- This process is NOT synthesizable.  Everything else in this example is.
  p_MAIN_TEST : process is
  begin
    r_VECTOR <= X"DEAD";
    wait for 100 ns;
    r_VECTOR <= X"BEEF";
    wait for 100 ns;
    wait;
  end process;
   
end behave;
