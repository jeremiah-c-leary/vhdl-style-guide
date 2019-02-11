
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
      INX         : in    std_logic_vector
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
      INITX : std_logic_vector
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

  signal adx,      GPU_X     : std_logic_vector(9 downto 0);
  signal ady,      GPU_Y     : std_logic_vector(8 downto 0);
  signal data                : std_logic_vector(2 downto 0);
  signal gim                 : std_logic_vector(22 downto 0);
  signal gpu_color_to_buffer : std_logic_vector(2 downto 0);
  signal bufferwrite         : std_logic;
  signal dout                : std_logic;
  signal ss                  : std_logic_vector(3 downto 0);
  signal clk2                : std_logic;
  signal p1region, p2Region  : std_logic;
  signal rt, Gt, Bt          : std_logic;
  signal x1,       X2        : std_logic_vector(9 downto 0);
  signal y1,       Y2        : std_logic_vector(8 downto 0);

begin

  INS_FRAMEBUFFER : FRAMEBUFFER
    port map (
      INX         => GPU_X,
      INY         => GPU_Y,
      OUTX        => Adx,
      OUTY        => Ady,
      OUTCOLOR    => data,
      INCOLOR     => inColor,
      BUFFERWRITE => BufferWrite,
      CLK         => CLK
    );

  INS_SYNCHRONIZER : SYNCHRONIZER
    port map (
      R        => Rt,
      G        => Gt,
      B        => Bt,
      HS       => HS,
      VS       => VS,
      CLK      => Clk,
      DATAIN   => data,
      ADDRESSX => Adx,
      ADDRESSY => Ady
    );

  INST_DEBOUNCER : DEBOUNCER
    port map (
      CLK    => Clk,
      BUTTON => Button,
      DOUT   => DOUT
    );

  INST_BRESENHAMER : BRESENHAMER
    port map (
      WRITEENABLE => BufferWrite,
      X           => GPU_X,
      Y           => GPU_Y,
      X1          => X1,
      Y1          => Y1,
      X2          => X2,
      Y2          => Y2,
      CLK         => Clk,
      SS          => SS,
      RESET       => reset,
      STARTDRAW   => Dout
    );

  LED <= BufferWrite;

  R <= Rt when (P1Region='0' and P2Region='0') else
       not Rt;

  G <= Gt when (P1Region='0' and P2Region='0') else
       not Gt;

  B <= Bt when (P1Region='0' and P2Region='0') else
       not Bt;

  INST_SEVENSEGMENT : SEVENSEGMENT
    port map (
      CLK               => Clk,
      ENABLES           => Enables,
      SEGMENTS          => Segments,
      DATA(3 downto 0)  => SS,
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
      CLK       => Clk2,
      HERE      => P1Region,
      X         => X1,
      Y         => Y1,
      SYNCX     => Adx,
      SYNCY     => Ady
    );

  INST_FREQDIV : FREQDIV
    port map (
      CLK  => Clk,
      CLK2 => CLK2
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
      CLK       => Clk2,
      HERE      => P2Region,
      X         => X2,
      Y         => Y2,
      SYNCX     => Adx,
      SYNCY     => Ady
    );

end architecture BEHAVIORAL;
