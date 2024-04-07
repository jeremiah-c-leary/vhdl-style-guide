
entity adder_tree is
   generic ( in_width: integer := 14; out_width: integer := 15 ); 
   port (
         Q:       out STD_LOGIC_VECTOR( (out_width-1) downto 0 )
   );
end entity;
