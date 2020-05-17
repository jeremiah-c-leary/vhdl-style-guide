
package PACK is

  component COMP is
    generic (
      GENERIC_1 : std_logic := '0'
    );
    port (
      PORT_1 : in    std_logic;
      PORT_2 : inout std_logic;
      PORT_3 : out   std_logic;
    );
  end component COMP;

end  package PACK;


PACKAGE PACK -- This is a comment

  component COMP is
    generic (
      GENERIC_1 : std_logic := '0'
    );
    port (
      PORT_1 : in    std_logic;
      PORT_2 : inout std_logic;
      PORT_3 : out   std_logic;
    );
  end component COMP;

end PACKAGE  pack;
  package PACK  IS

  component COMP is
    generic (
      GENERIC_1 : std_logic := '0'
    );
    port (
      PORT_1 : in    std_logic;
      PORT_2 : inout std_logic;
      PORT_3 : out   std_logic;
    );
  end component COMP;

   END package PACK;

package  pack is
  component COMP is
    generic (
      GENERIC_1 : std_logic := '0'
    );
    port (
      PORT_1 : in    std_logic;
      PORT_2 : inout std_logic;
      PORT_3 : out   std_logic;
    );
  end component COMP;
end  PACK;

package PACK
  is
  component COMP is
    generic (
      GENERIC_1 : std_logic := '0'
    );
    port (
      PORT_1 : in    std_logic;
      PORT_2 : inout std_logic;
      PORT_3 : out   std_logic;
    );
  end component COMP;

end  package;

package my_pkg is

  constant MY_CONST : integer := 5;

end package my_pkg;

package pkg_my is

  constant MY_CONST : integer := 5;

end package pkg_my;
