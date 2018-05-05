
architecture ARCH of ENTITY1 is

  type a is (B, C, D, E ,F, G);

   type a is ( B, C,
    D, E,
    -- This is a comment
    F, G);

 type a is range 0 to 9;

  type interface is record
    data : std_logic_vector(31 downto 0);
    chip_select : std_logic;
    wr_en : std_logic;
    rd_en : std_logic;
 
  end record;

begin

end architecture ARCH;

package PACK is

  type A is (B, C, D, E ,F, G);

  type  a is  (B, C,
    D, E,
    -- This is a comment
      F, G);

  TYPE a is range 0 to 9;

  type a  is (--This is a comment
    A, B,
    -- comment
    C
  );

  a <= b;
  type a is (
    A, B,

    -- comment
    C
  );
  a <= b;

    subtype a is range 0 to 9;


  type memory is array (DEPTH - 1 downto 0) of
       STD_LOGIC_VECTOR(WIDTH-1 downto 0);

  type interface is record
    data : std_logic_vector(31 downto 0);
    chip_select : std_logic;
   wr_en : std_logic;
      rd_en : std_logic;
  end record;


  subtype a is 
    range 0 to 9;


  type interface is
  record
    data : std_logic_vector(31 downto 0);
    chip_select : std_logic;
    wr_en : std_logic;
    rd_en : std_logic;
  end record;
    
end package PACK;

library LIB1;
use blah.record.all;

