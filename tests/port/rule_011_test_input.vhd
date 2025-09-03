
entity FIFO is
  port (
    I_WR_EN  : in  std_logic;
    I_DATA   : out std_logic_vector(31 downto 0);
    IO_RD_EN : inout  std_logic;
    O_DATA   : out std_logic_vector(31 downto 0)
  );
end entity FIFO;


entity FIFO is
  port (
    WR_EN : in  std_logic;
    DATA  : out std_logic_vector(31 downto 0);
    RD_EN : inout  std_logic;
    DATA  : out std_logic_vector(31 downto 0)
  );
end entity FIFO;

architecture rtl of fifo is

  component foo is
    port (
      WR_EN : in std_logic;
      DATA : out std_logic;
      RD_EN : inout std_logic
    );
  end component foo;

begin

  U_FOO : foo
    port map (
      WR_EN => '0',
      DATA => '1'
    );

end architecture rtl;
