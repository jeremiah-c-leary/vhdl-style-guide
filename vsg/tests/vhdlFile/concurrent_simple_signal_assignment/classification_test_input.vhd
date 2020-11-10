
architecture RTL of FIFO is

begin

  -- Simple form
  a <= b;

  -- with guarded
  a <= guarded b;

  -- with transport delay mechanism
  a <= transport b;

  -- with inertial delay machanism
  a <= inertial b;

  -- with reject delay mechanism
  a <= reject 10 ns inertial b;

  -- with guarded and transport delay mechanism
  a <= guarded transport b;

  -- with guarded and inertial delay machanism
  a <= guarded inertial b;

  -- with guarded and reject delay mechanism
  a <= guarded reject 10 ns inertial b;

end architecture RTL;
