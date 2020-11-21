
architecture RTL of FIFO is

begin

  -- These are passing

  a <= b;                     -- Comment 1
  a <= when c = '0' else '1'; -- Comment 2
  a <= b;                     -- Comment 3
  a <= when c = '0' else '1'; -- Comment 4

  -- Failing variations

  a <= b;                     -- Comment 1
  a <= when c = '0' else '1'; -- Comment 2
  a <= b;                     -- Comment 3
  a <= when c = '0' else '1'; -- Comment 4

  process  -- comment process
  begin -- comment begin

    a <= b; -- Comment
    b <= c;         -- Comment
    c <= d;      -- Comment
  end process;  -- comment end process

  x <= z when b = c else -- comment a
       y when c = d else -- comment b
       x when d = e;     -- comment c
  z <= w when e = f else -- comment d
       x when f = g else -- comment e
       z;                -- comment f

  INST : INST_1  -- instantiation comment
    port map (   -- port map comment
      a => '0' -- port comment
    );  -- end port map comment

  assert True -- assert comment
    report "Hello" -- report comment
    severity Warning; -- severity comment

  procedure_call(  -- procedure call comment
    a => b,  -- procedure call parameter 1
    c => d   -- procedure call parameter 2
  ); -- procedure call end parenthesis

  -- Block
  block_label : block  -- Block comment
  begin -- block begin comment
    a <= b; -- comment z
    c <= d; -- comment y
    e <= f; -- comment x
  end block; -- end block comment

  -- Generate statements

  for_generate_label : for i in 0 to 200 generate -- for generate comment
    ab <= bc; -- comment zz
    ac <= ad; -- coment za
    ae <= af; -- comment ab
  end generate; -- end for generate label

  a <= b; -- comment
  c <= d; -- comment
  -- comment line

end architecture RTL;
