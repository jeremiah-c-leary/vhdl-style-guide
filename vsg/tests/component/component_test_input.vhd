
architecture ARCH of ENTITY is

  -- Basic component
  component comp1 is
    port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic
    );
  end component comp1;

  -- Capitalization checks

  comPOnent CORm1 Is
    Port (
      port_1 : iN    std_logic;
      port_2 : in    std_LOgic;
      port_3 : inOut std_logic;
      port_4 : ouT   std_logic
    );
  eNd comPonent CoMP1;

  -- Indentation checks

 component  comp1
    port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic
    );
   end component  comp1;
 
  component comp1  is
     port (
     port_1 : in    std_logic;
      port_2 : in    std_logic;
       port_3 : inout std_logic;
      port_4 : out   std_logic
   );
  end component;

   component   comp1 is
   port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic
      );
 end  component comp1;

  -- Blank line tests

  component comp1 is

    port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic
    );

  end component comp1;
  component COMP1 is
    port (

      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic

    );
  end component COMP1;


  component comp1
    is
    port (
      port_1 : in    std_logic;
      port_2 : in    std_logic;
      port_3 : inout std_logic;
      port_4 : out   std_logic

    );
  end component comp1;
  -- This is a comment

begin

end architecture ARCH;

