
architecture ARCH of ENTITY is

  -- Basic component
  component COMP1 is
    port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic;
    );
  end component COMP1;

  -- Capitalization checks

  comPOnent CORm1 Is
    Port (
      port_1 : iN    std_logic;
      port_2 : in    std_LOgic;
      port_3 : inOut std_logic;
      port_4 : ouT   std_logic;
    );
  eNd comPonent CoMP1;

  -- Indentation checks

 component COMP1 is
    port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic;
    );
   end component COMP1;
 
  component COMP1 is
     port (
     port_1 : in    std_logic;
      port_2 : in    std_logic;
       port_3 : inout std_logic;
      port_4 : out   std_logic;
   );
  end component COMP1;

   component COMP1 is
   port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic;
      );
 end component COMP1;

  -- Blank line tests

  component COMP1 is

    port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic;
    );

  end component COMP1;
  component COMP1 is
    port (

      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic;

    );
  end component COMP1;

begin

end architecture ARCH;

