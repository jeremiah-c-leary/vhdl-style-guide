-- Test Keywords
-- Gerard Sharp, November 2023
-- Public Domain

-- Making identifiers out of reserved keywords to test the awesome vsg project

entity null is             -- 'null' is a reserved keyword since 1987
  generic (
    vpkg       : positive; -- 'vpkg' is a reserved keyword since 2019
    default    : natural;  -- 'default' is a reserved keyword since 2008
    unaffected : natural   -- 'unaffected' is a reserved keyword since 1993
  );
  port (
    private : out   natural;   -- 'private' since 2019
    context : out   natural;   -- 'context' since 2008
    clk     : in    std_logic; -- legal
    rst     : in    std_logic  -- legal
  );
end entity null;  -- 'null' since 1987

architecture rol of null is -- 'rol' since 1993, 'null' since 1987

  signal view       : boolean;   -- 'view' since 2019
  signal procedural : natural;   -- 'procedural' reserved in 2002 and not in 2008
  signal open       : natural;   -- 'open' reserved since 1987
  signal wilbur     : std_logic; -- legal

  -- 'sequence' since 2008, 'reject' since 1993

  procedure sequence (reject: out natural) is  -- 'reject' since 1993

    variable reference : natural; -- 'reference' only in 2002

  begin

    reject := reference;

  end procedure sequence; -- 'sequence' since 2008

begin

  wilbur <= not rst when rising_edge(clk); -- this line is legal

end architecture rol;  -- 'rol' since 1993

-- Testing return is not triggered
entity b is
  generic (
    function foo (
      a : natural;
      b : DATA_TYPE
    ) return natural;
    impure function bar (
      a          : integer;
      b          : integer;
      constant c : integer
    ) return natural
  );
end entity b;
