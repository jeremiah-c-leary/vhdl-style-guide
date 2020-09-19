
architecture RTL of FIFO is

begin

  -- Simple form
  a <= b when 'a' else
       c when 'b' else
       d;

  -- with guarded
  a <= guarded b when 'a' else
       c when 'b' else
       d;

  -- with transport delay mechanism
  a <= transport b when 'a' else
       c when 'b' else
       d;

  -- with inertial delay machanism
  a <= inertial b when 'a' else
       c when 'b' else
       d;

  -- with reject delay mechanism
  a <= reject 10 ns inertial b when 'a' else
       c when 'b' else
       d;

  -- with guarded and transport delay mechanism
  a <= guarded transport b when 'a' else
       c when 'b' else
       d;

  -- with guarded and inertial delay machanism
  a <= guarded inertial b when 'a' else
       c when 'b' else
       d;

  -- with guarded and reject delay mechanism
  a <= guarded reject 10 ns inertial b when 'a' else
       c when 'b' else
       d;

  -- Variations on else's
  a <= b when 'a' else c;

  a <= b when 'a' else c when 'b' else d;

end architecture RTL;
