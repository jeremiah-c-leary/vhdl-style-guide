Example Formatting
------------------

The examples shown below illustrate the formatting enforced by VSG.
They show a subset of the rules:

* capitalization
* indentation
* column alignments

  * comments
  * :'s
  * assignment operators (<= and =>)

* vertical spacing

Entities
########

.. code-block:: vhdl

  entity GRP_DEBOUNCER is
    generic (
      N       : positive := 8;                      -- input bus width
      CNT_VAL : positive := 10000                   -- clock counts for debounce period
    );
    port (
      CLK_I  : in    std_logic := 'X';              -- system clock
      DATA_I : in    std_logic_vector(1 downto 0)   -- noisy input data
      DATA_O : out   std_logic_vector(1 downto 0);  -- registered stable output data
      STRB_O : out   std_logic                      -- strobe for new data available
    );
  end entity GRP_DEBOUNCER;

Architectures
#############

.. code-block:: vhdl

  architecture BEHAVIORAL of PIC is
  
    type state_type is (
      reset_s, get_commands, jump_int_method, start_polling,
      ack_txinfo_rxd, start_priority_check, tx_int_info_priority
    );
  
    signal next_s               : state_type :=reset_s;
    signal int_type             : unsigned(1 downto 0):="01";
    signal int_index, count_cmd : integer := 0;
  
    type prior_table is array (0 to 7) of unsigned(2 downto 0);
  
    signal pt                   : prior_table := (others => (others => '0'));
    signal int_pt               : unsigned(2 downto 0):="000";
    signal flag,      flag1     : std_logic := '0';
  
  begin
  
  end architecture BEHAVIORAL;

Component Declarations
######################

.. code-block:: vhdl

    component CPU is
      port (
        CLK_I        : in    std_logic;
        SWITCH       : in    std_logic_vector(9 downto 0);
  
        SER_IN       : in    std_logic;
        SER_OUT      : out   std_logic;
  
        TEMP_SPO     : in    std_logic;
        TEMP_SPI     : out   std_logic;
        TEMP_CE      : out   std_logic;
        TEMP_SCLK    : out   std_logic;
  
        SEG1         : out   std_logic_vector(7 downto 0);
        SEG2         : out   std_logic_vector( 7 downto 0);
        LED          : out   std_logic_vector( 7 downto 0);
  
        XM_ADR       : out   std_logic_vector(15 downto 0);
        XM_RDAT      : in    std_logic_vector( 7 downto 0);
        XM_WDAT      : out   std_logic_vector( 7 downto 0);
        XM_WE        : out   std_logic;
        XM_CE        : out   std_logic
      );
    end component;

Component Instantiations
########################

.. code-block:: vhdl

    INTERLEAVER_I0 : INTERLEAVER
      generic map (
        DELAY       => TREL1_LEN + TREL2_LEN + 2 + delay,
        WAY         => 0
      )
      port map (
        CLK         => clk,
        RST         => rst,
        D           => tmp0,
        Q           => tmp1
      );

Concurrent Assignments
######################

.. code-block:: vhdl

    nCounter       <= x"FFFFFF" when Counter=x"FFFFFF" and Button='1' else
                      x"000000" when Counter=x"000000" and Button='0' else
                      Counter + 1 when Button='1' else
                      Counter - 1;
    nextHistory    <= '0' when Counter=x"000000" else
                      '1';
    nButtonHistory <= nextHistory & ButtonHistory(1);
    Dout           <= '1' when ButtonHistory="01" else
                      '0';
