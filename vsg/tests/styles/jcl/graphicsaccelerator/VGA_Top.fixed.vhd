
library IEEE;
  use IEEE.STD_LOGIC_1164.ALL;

entity VGA_TOP is
  port (
    R         : out   std_logic;
    G         : out   std_logic;
    B         : out   std_logic;
    CLK       : in    std_logic;
    HS        : out   std_logic;
    VS        : out   std_logic;
    BUTTON    : in    std_logic;
    RESET     : in    std_logic;
    LED       : out   std_logic;
    ENABLES   : out   std_logic_vector(3 downto 0);
    SEGMENTS  : out   std_logic_vector(6 downto 0);
    INCOLOR   : in    std_logic_vector(2 downto 0);
    MOVEUP    : in    std_logic;
    MOVEDOWN  : in    std_logic;
    MOVELEFT  : in    std_logic;
    MOVERIGHT : in    std_logic;
    MOVEP1    : in    std_logic;
    MOVEP2    : in    std_logic
  );
end entity VGA_TOP;

architecture BEHAVIORAL of VGA_TOP is

  component DEBOUNCER is
    port (
      CLK    : in    std_logic;
      BUTTON : in    std_logic;
      DOUT   : out   std_logic
    );
  end component;

  component BRESENHAMER is
    port (
      X1          : in    std_logic_vector(9 downto 0);
      Y1          : in    std_logic_vector(8 downto 0);
      X2          : in    std_logic_vector(9 downto 0);
      Y2          : in    std_logic_vector(8 downto 0);
      CLK         : in    std_logic;
      STARTDRAW   : in    std_logic;
      WRITEENABLE : out   std_logic;
      SS          : out   std_logic_vector(3 downto 0);
      X           : out   std_logic_vector(9 downto 0);
      Y           : out   std_logic_vector(8 downto 0);
      RESET       : in    std_logic
    );
  end component;

  component SYNCHRONIZER is
    port (
      R        : out   std_logic;
      G        : out   std_logic;
      B        : out   std_logic;
      HS       : out   std_logic;
      VS       : out   std_logic;
      CLK      : in    std_logic;
      DATAIN   : in    std_logic_vector(2 downto 0);
      ADDRESSX : out   std_logic_vector(9 downto 0);
      ADDRESSY : out   std_logic_vector(8 downto 0)
    );
  end component;

  component FRAMEBUFFER is
    port (
      INX         : in    std_logic_vector(9 downto 0);
      INY         : in    std_logic_vector(8 downto 0);
      OUTX        : in    std_logic_vector(9 downto 0);
      OUTY        : in    std_logic_vector(8 downto 0);
      OUTCOLOR    : out   std_logic_vector(2 downto 0);
      INCOLOR     : in    std_logic_vector(2 downto 0);
      BUFFERWRITE : in    std_logic;
      CLK         : in    std_logic
    );
  end component;

  component SEVENSEGMENT is
    port (
      CLK      : in    std_logic;
      DATA     : in    std_logic_vector(15 downto 0);
      ENABLES  : out   std_logic_vector(3 downto 0);
      SEGMENTS : out   std_logic_vector(6 downto 0)
    );
  end component;

  component POINTER is
    generic (
      INITX : std_logic_vector(9 downto 0);
      INITY : std_logic_vector(8 downto 0)
    );
    port (
      MOVEUP    : in    std_logic;
      MOVEDOWN  : in    std_logic;
      MOVELEFT  : in    std_logic;
      MOVERIGHT : in    std_logic;
      MOVE      : in    std_logic;
      CLK       : in    std_logic;
      X         : out   std_logic_vector(9 downto 0);
      Y         : out   std_logic_vector(8 downto 0);
      SYNCX     : in    std_logic_vector(9 downto 0);
      SYNCY     : in    std_logic_vector(8 downto 0);
      HERE      : out   std_logic
    );
  end component;

  component FREQDIV is
    port (
      CLK  : in    std_logic;
      CLK2 : out   std_logic
    );
  end component;

  signal adx,      gpu_x     : std_logic_vector(9 downto 0);
  signal ady,      gpu_y     : std_logic_vector(8 downto 0);
  signal data                : std_logic_vector(2 downto 0);
  signal gim                 : std_logic_vector(22 downto 0);
  signal gpu_color_to_buffer : std_logic_vector(2 downto 0);
  signal bufferwrite         : std_logic;
  signal dout                : std_logic;
  signal ss                  : std_logic_vector(3 downto 0);
  signal clk2                : std_logic;
  signal p1region, p2region  : std_logic;
  signal rt                  : std_logic;
  signal gt                  : std_logic;
  signal bt                  : std_logic;
  signal x1,       x2        : std_logic_vector(9 downto 0);
  signal y1,       y2        : std_logic_vector(8 downto 0);

begin

  INS_FRAMEBUFFER : FRAMEBUFFER
    port map (
      INX         => gpu_x,
      INY         => gpu_y,
      OUTX        => adx,
      OUTY        => ady,
      OUTCOLOR    => data,
      INCOLOR     => inColor,
      BUFFERWRITE => bufferwrite,
      CLK         => Clk
    );

  INS_SYNCHRONIZER : SYNCHRONIZER
    port map (
      R        => rt,
      G        => gt,
      B        => bt,
      HS       => HS,
      VS       => VS,
      CLK      => Clk,
      DATAIN   => data,
      ADDRESSX => adx,
      ADDRESSY => ady
    );

  INST_DEBOUNCER : DEBOUNCER
    port map (
      CLK    => Clk,
      BUTTON => Button,
      DOUT   => dout
    );

  INST_BRESENHAMER : BRESENHAMER
    port map (
      WRITEENABLE => bufferwrite,
      X           => gpu_x,
      Y           => gpu_y,
      X1          => x1,
      Y1          => y1,
      X2          => x2,
      Y2          => y2,
      CLK         => Clk,
      SS          => ss,
      RESET       => reset,
      STARTDRAW   => dout
    );

  LED <= bufferwrite;

  R <= rt when (p1region='0' and p2region='0') else
       not rt;

  G <= gt when (p1region='0' and p2region='0') else
       not gt;

  B <= bt when (p1region='0' and p2region='0') else
       not bt;

  INST_SEVENSEGMENT : SEVENSEGMENT
    port map (
      CLK               => Clk,
      ENABLES           => Enables,
      SEGMENTS          => Segments,
      DATA(3 downto 0)  => ss,
      DATA(15 downto 4) => "000000000000"
    );

  INST_POINTER1 : POINTER
    generic map (
      INITX => "0000000100",
      INITY => "011110000"
    )
    port map (
      MOVEUP    => MoveUp,
      MOVEDOWN  => MoveDown,
      MOVELEFT  => MoveLeft,
      MOVERIGHT => MoveRight,
      MOVE      => MoveP1,
      CLK       => clk2,
      HERE      => p1region,
      X         => x1,
      Y         => y1,
      SYNCX     => adx,
      SYNCY     => ady
    );

  INST_FREQDIV : FREQDIV
    port map (
      CLK  => Clk,
      CLK2 => clk2
    );

  INST_POINTER2 : POINTER
    generic map (
      INITX => "1001111000",
      INITY => "011110000"
    )
    port map (
      MOVEUP    => MoveUp,
      MOVEDOWN  => MoveDown,
      MOVELEFT  => MoveLeft,
      MOVERIGHT => MoveRight,
      MOVE      => MoveP2,
      CLK       => clk2,
      HERE      => p2region,
      X         => x2,
      Y         => y2,
      SYNCX     => adx,
      SYNCY     => ady
    );

end architecture BEHAVIORAL;
