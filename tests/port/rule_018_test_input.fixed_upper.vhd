
entity FIFO is

  port (
    I_PORT1 : in INTEGER;
    I_PORT2 : in STD_LOGIC;
    I_PORTA : in t_user2;
    I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
    I_PORT4 : in SIGNED(15 downto 0);
    I_PORT5 : in UNSIGNED(7 downto 0);
    I_PORT6 : in STD_ULOGIC;
    I_PORT7 : in t_user1
  );

end entity FIFO;


-- Violation below

entity FIFO is

  port (
    I_PORT1 : in INTEGER;
    I_PORT2 : in STD_LOGIC;
    I_PORTA : in t_user2;
    I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
    I_PORT4 : in SIGNED(15 downto 0);
    I_PORT5 : in UNSIGNED(7 downto 0);
    I_PORT6 : in STD_ULOGIC;
    I_PORT7 : in t_user1
  );

end entity FIFO;
