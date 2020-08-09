
architecture RTL of FIFO is



  type t_FROM_FIFO;

  -- Check records
  type t_FROM_FIFO is record
    wr_full  : std_logic;                -- FIFO Full Flag
    rd_empty : std_logic;                -- FIFO Empty Flag
    rd_dv    : std_logic;
    rd_data  : std_logic_vector(7 downto 0);
  end record t_FROM_FIFO;

  -- Check enumerated
  type state is (idle, first, second);

  -- Check array
  type RAM is array (31 downto 0) of integer range 0 to 255;

  -- Check integer type
  type word is range 31 downto 0;

  -- Check floating type
  type voltage_level is range -5.5 to +5.5;

  -- Access type
  type queue_element is access queue_element;

  -- File type
  type FT is file of SomeType;



begin

end architecture RTL;
