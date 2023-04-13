
architecture RTL of FIFO is

  procedure proc_name (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
  begin
  end procedure proc_name;

      procedure proc_name (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
  begin
  end procedure proc_name;

procedure proc_name (
    constant a : in integer;
    signal b : in std_logic;
    variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic) is
  begin
  end procedure proc_name;

  -- There must be an indent after the proctected type
  type t_protected_fifo is protected

    procedure reset_fifo (
      void : t_void
    );

        procedure reset_fifo (
      void : t_void
    );

  end protected t_protected_fifo;

begin

end architecture RTL;
