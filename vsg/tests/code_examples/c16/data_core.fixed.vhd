
library IEEE;
  use IEEE.STD_LOGIC_1164.ALL;
  use IEEE.STD_LOGIC_ARITH.ALL;
  use IEEE.STD_LOGIC_UNSIGNED.ALL;

  --  Uncomment the following lines to use the declarations that are
  --  provided for instantiating Xilinx primitive components.
  --library UNISIM;
  --use UNISIM.VComponents.all;
  use work.cpu_pack.ALL;

entity DATA_CORE is
  port (
    CLK_I   : in    std_logic;
    T2      : in    std_logic;
    CLR     : in    std_logic;
    CE      : in    std_logic;

    -- select signals
    SX      : in    std_logic_vector( 1 downto 0);
    SY      : in    std_logic_vector( 3 downto 0);
    OP      : in    std_logic_vector( 4 downto 0);      -- alu op
    PC      : in    std_logic_vector(15 downto 0);      -- PC
    QU      : in    std_logic_vector( 3 downto 0);      -- quick operand
    SA      : in    std_logic_vector(4 downto 0);       -- select address
    SMQ     : in    std_logic;                          -- select MQ (H/L)

    -- write enable/select signal
    WE_RR   : in    std_logic;
    WE_LL   : in    std_logic;
    WE_SP   : in    SP_OP;

    -- data in signals
    IMM     : in    std_logic_vector(15 downto 0);      -- immediate data
    RDAT    : in    std_logic_vector( 7 downto 0);      -- memory/IO data

    -- memory control signals
    ADR     : out   std_logic_vector(15 downto 0);
    MQ      : out   std_logic_vector( 7 downto 0);

    Q_RR    : out   std_logic_vector(15 downto 0);
    Q_LL    : out   std_logic_vector(15 downto 0);
    Q_SP    : out   std_logic_vector(15 downto 0)
  );
end entity DATA_CORE;

architecture BEHAVIORAL of DATA_CORE is

  function b8 (A : std_logic) return std_logic_vector is
  begin
    return A & A & A & A & A & A & A & A;
  end;

  component ALU8 is
    port (
      CLK_I  : in    std_logic;
      T2     : in    std_logic;
      CE     : in    std_logic;
      CLR    : in    std_logic;

      ALU_OP : in    std_logic_vector( 4 downto 0);
      XX     : in    std_logic_vector(15 downto 0);
      YY     : in    std_logic_vector(15 downto 0);
      ZZ     : out   std_logic_vector(15 downto 0)
    );
  end component;

  component SELECT_YY is
    port (
      SY      : in    std_logic_vector( 3 downto 0);
      IMM     : in    std_logic_vector(15 downto 0);
      QUICK   : in    std_logic_vector( 3 downto 0);
      RDAT    : in    std_logic_vector( 7 downto 0);
      RR      : in    std_logic_vector(15 downto 0);
      YY      : out   std_logic_vector(15 downto 0)
    );
  end component;

  -- cpu registers
  --
  signal rr      : std_logic_vector(15 downto 0);
  signal ll      : std_logic_vector(15 downto 0);
  signal sp      : std_logic_vector(15 downto 0);

  -- internal buses
  --
  signal xx      : std_logic_vector(15 downto 0);
  signal yy      : std_logic_vector(15 downto 0);
  signal zz      : std_logic_vector(15 downto 0);
  signal adr_x   : std_logic_vector(15 downto 0);
  signal adr_z   : std_logic_vector(15 downto 0);
  signal adr_yz  : std_logic_vector(15 downto 0);
  signal adr_xyz : std_logic_vector(15 downto 0);

begin

  ALU_8 : ALU8
    port map (
      CLK_I  => CLK_I,
      T2     => T2,
      CE     => CE,
      CLR    => CLR,
      ALU_OP => OP,
      XX     => xx,
      YY     => yy,
      ZZ     => zz
    );

  SELYY : SELECT_YY
    port map (
      SY    => SY,
      IMM   => IMM,
      QUICK => QU,
      RDAT  => RDAT,
      RR    => rr,
      YY    => yy
    );

  ADR <= adr_xyz;
  MQ  <= zz(15 downto 8) when SMQ = '1' else
         zz(7 downto 0);

  Q_RR <= rr;
  Q_LL <= ll;
  Q_SP <= sp;

  -- memory address
  --
  SEL_AX : process (SA(4 downto 3), IMM) is

    variable sax : std_logic_vector(4 downto 3);

  begin

    sax := SA(4 downto 3);

    case sax is

      when SA_43_I16 =>
        adr_x <= IMM;
      when SA_43_I8S =>
        adr_x <= b8(IMM(7)) & IMM(7 downto 0);
      when others =>
        adr_x <= b8(SA(3)) & b8(SA(3));

    end case;

  end process SEL_AX;

  SEL_AZ : process (SA(2 downto 1), ll, rr, sp) is

    variable saz : std_logic_vector(2 downto 1);

  begin

    saz := SA(2 downto 1);

    case saz is

      when SA_21_0 =>
        adr_z <= X"0000";
      when SA_21_LL =>
        adr_z <= ll;
      when SA_21_RR =>
        adr_z <= rr;
      when others =>
        adr_z <= sp;

    end case;

  end process SEL_AZ;

  SEL_AYZ : process (SA(0), adr_z) is
  begin

    adr_yz <= adr_z + (X"000" & "000" & SA(0));

  end process SEL_AYZ;

  SEL_AXYZ : process (adr_x, adr_yz) is
  begin

    adr_xyz <= adr_x + adr_yz;

  end process SEL_AXYZ;

  SEL_XX : process (SX, ll, rr, sp, PC) is
  begin

    case SX is

      when SX_LL =>
        xx <= ll;
      when SX_RR =>
        xx <= rr;
      when SX_SP =>
        xx <= sp;
      when others =>
        xx <= PC;

    end case;

  end process SEL_XX;

  REGS : process (CLK_I) is
  begin

    if (CLK_I'event and CLK_I = '1') then
      if (CLR = '1') then
        rr <= X"0000";
        ll <= X"0000";
        sp <= X"0000";
      elsif (CE  = '1' and T2 = '1') then
        if (WE_RR = '1') then
          rr <= zz;
        end if;
        if (WE_LL = '1') then
          ll <= zz;
        end if;

        case WE_SP is

          when SP_INC =>
            sp <= adr_yz;
          when SP_LOAD =>
            sp <= adr_xyz;
          when SP_NOP =>
            null;

        end case;

      end if;
    end if;

  end process REGS;

end architecture BEHAVIORAL;
