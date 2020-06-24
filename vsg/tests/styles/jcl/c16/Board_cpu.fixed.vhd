--
-- This is the top level VHDL file.
--
-- It iobufs for bidirational signals (towards an optional
-- external fast SRAM.
--
-- Pins fit the AVNET Virtex-E Evaluation board
--
-- For other boards, change pin assignments in this file.
--

library IEEE;
  use IEEE.std_logic_1164.all;
  use IEEE.std_logic_unsigned.all;
  use work.cpu_pack.ALL;

library UNISIM;
  use UNISIM.VComponents.all;

entity BOARD_CPU is
  port (
    CLK40         : in    std_logic;
    SWITCH        : in    std_logic_vector(9 downto 0);

    SER_IN        : in    std_logic;
    SER_OUT       : out   std_logic;

    TEMP_SPO      : in    std_logic;
    TEMP_SPI      : out   std_logic;

    CLK_OUT       : out   std_logic;
    LED           : out   std_logic_vector(7 downto 0);
    ENABLE_N      : out   std_logic;
    DEACTIVATE_N  : out   std_logic;
    TEMP_CE       : out   std_logic;
    TEMP_SCLK     : out   std_logic;
    SEG1          : out   std_logic_vector(7 downto 0);
    SEG2          : out   std_logic_vector(7 downto 0);

    XM_ADR        : out   std_logic_vector(14 downto 0);
    XM_CE_N       : out   std_logic;
    XM_OE_N       : out   std_logic;
    XM_WE_N       : inout std_logic;
    XM_DIO        : inout std_logic_vector(7 downto 0)
  );
end entity BOARD_CPU;

architecture BEHAVIORAL of BOARD_CPU is

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

  signal xm_wdat  : std_logic_vector( 7 downto 0);
  signal xm_rdat  : std_logic_vector( 7 downto 0);
  signal mem_t    : std_logic;
  signal xm_we    : std_logic;
  signal we_n     : std_logic;
  signal del_we_n : std_logic;
  signal xm_ce    : std_logic;
  signal lclk     : std_logic;

begin

  CP : CPU
    port map (
      CLK_I  => CLK40,
      SWITCH => SWITCH,

      SER_IN  => SER_IN,
      SER_OUT => SER_OUT,

      TEMP_SPO => TEMP_SPO,
      TEMP_SPI => TEMP_SPI,

      XM_ADR(14 downto 0) => XM_ADR,
      XM_ADR(15)          => open,
      XM_RDAT             => xm_rdat,
      XM_WDAT             => xm_wdat,
      XM_WE               => xm_we,
      XM_CE               => xm_ce,
      TEMP_CE             => TEMP_CE,
      TEMP_SCLK           => TEMP_SCLK,
      SEG1                => SEG1,
      SEG2                => SEG2,
      LED                 => LED
    );

  ENABLE_N     <= '0';
  DEACTIVATE_N <= '1';
  CLK_OUT      <= lclk;

  mem_t   <= del_we_n;    -- active low
  we_n    <= not xm_we;
  XM_OE_N <= xm_we;
  XM_CE_N <= not xm_ce;

  P147 : IOBUF
    port map (
      I  => xm_wdat(7),
      O  => xm_rdat(7),
      T  => mem_t,
      IO => XM_DIO(7)
    );

  P144 : IOBUF
    port map (
      I  => xm_wdat(0),
      O  => xm_rdat(0),
      T  => mem_t,
      IO => XM_DIO(0)
    );

  P142 : IOBUF
    port map (
      I  => xm_wdat(6),
      O  => xm_rdat(6),
      T  => mem_t,
      IO => XM_DIO(6)
    );

  P141 : IOBUF
    port map (
      I  => xm_wdat(1),
      O  => xm_rdat(1),
      T  => mem_t,
      IO => XM_DIO(1)
    );

  P140 : IOBUF
    port map (
      I  => xm_wdat(5),
      O  => xm_rdat(5),
      T  => mem_t,
      IO => XM_DIO(5)
    );

  P139 : IOBUF
    port map (
      I  => xm_wdat(2),
      O  => xm_rdat(2),
      T  => mem_t,
      IO => XM_DIO(2)
    );

  P133 : IOBUF
    port map (
      I  => xm_wdat(4),
      O  => xm_rdat(4),
      T  => mem_t,
      IO => XM_DIO(4)
    );

  P131 : IOBUF
    port map (
      I  => xm_wdat(3),
      O  => xm_rdat(3),
      T  => mem_t,
      IO => XM_DIO(3)
    );

  P63 : IOBUF
    port map (
      I  => we_n,
      O  => del_we_n,
      T  => '0',
      IO => XM_WE_N
    );

  process (CLK40) is
  begin

    if (CLK40'event and CLK40 = '1') then
      lclk <= not lclk;
    end if;

  end process;

end architecture BEHAVIORAL;
