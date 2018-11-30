
architecture ARCH of ENTITY1 is

  type a is (B, C, D, E ,F, G);

   type a is ( B, C,
    D, E,
    -- This is a comment
    F, G);

 type a is range 0 to 9;

  type interface IS record
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

  constant this_is_not_a_record : std_logic := "1";
  constant record_this_is_not   : std_logic := "0";

end package PACK;

library LIB1;
use blah.record.all;

entity ENTITY1 is
  generic (
    TYPE_GENERIC : std_logic := '0'
  );
  port (
    TYPE_PORT_NAME : std_logic;
    type_port_name_2 : std_logic
  );
end entity ENTITY1;

architecture ARCH of ENTITY1 is

  component ENTITY1 is
    generic (
      TYPE_GENERIC : std_logic := '0'
    );
    port (
      TYPE_PORT_NAME : std_logic;
      type_port_name_2 : std_logic
    );
  end component ENTITY1;

begin

  U_ENTITY : ENTITY1
    generic map (
      TYPE_GENERIC => '1'
    )
    port map (
      TYPE_PORT_NAME => '1';
      type_port_name_2 => '0'
    );

  TYPE_OUTPUT <= '1';

  process PROC1 (sig1) is

    type a is range 0 to 9;

  begin
    type_signal <= '0'
  end process PROC1;

end architecture ARCH;

