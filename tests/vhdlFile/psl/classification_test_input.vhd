
-- verification_unit
vunit identifier ( something ) {
  something
  something
}

vpkg identifier ( something ) {
  something
  something
}

vprop identifier ( something ) {
  something
  something
}

vmode identifier ( something ) {
  something
  something
}

entity fifo is

  default clock is rising_edge(i_clk);

  sequence identifier something something;

  property identifier something something;

  begin

    -- Unlabeled
    assert something something [report something];

    assume something something;

    restrict something something;

    restrict! something something;

    cover something something report something;

    fairness something something;

    strong fairness something something;

    -- labeled
    label1: assert something something [report something];

    label1: assume something something;

    label1: restrict something something;

    label1: restrict! something something;

    label1: cover something something report something;

    label1: fairness something something;

    label1: strong fairness something something;

end entity fifo;


architecture rtl of fifo is

  default clock is rising_edge(i_clk);

  sequence identifier something something;

  property identifier something something;

begin

  -- Unlabeled
  assert something something [report something];

  assume something something;

  restrict something something;

  restrict! something something;

  cover something something report something;

  fairness something something;

  strong fairness something something;

  -- labeled
  label1: assert something something [report something];

  label1: assume something something;

  label1: restrict something something;

  label1: restrict! something something;

  label1: cover something something report something;

  label1: fairness something something;

  label1: strong fairness something something;

end architecture rtl;

package my_pkg is

  sequence identifier something something;

  property identifier something something;

end package my_pkg;
