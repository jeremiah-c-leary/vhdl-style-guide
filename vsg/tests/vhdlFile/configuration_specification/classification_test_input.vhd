
architecture RTL of ENTITY_NAME is

  for all : blah
    use entity work.blah(rtl);

  for all : blah
    use entity work.blah(rtl);
  end for;

  for others : blah
    use entity work.blah(rtl);
  end for;

  for first : blah
    use entity work.blah(rtl);
  end for;

  for first, second : blah
    use entity work.blah(rtl);
  end for;

  for first, second, third : blah
    use entity work.blah(rtl);
  end for;

  for first, second, third : blah
    use entity work.blah(rtl)
    generic map (
      G_ONE => a,
      G_TWO => b
    );
  end for;

  for first, second, third : blah
    use entity work.blah(rtl)
    generic map (
      G_ONE => a,
      G_TWO => b
    )
    port map (
      I_INPUT => a,
      O_OUTPUT => b
    );
  end for;

  for first, second, third : blah
    use entity work.blah(rtl)
    port map (
      I_INPUT => a,
      O_OUTPUT => b
    );
  end for;

  for first, second, third : blah
    generic map (
      G_ONE => a,
      G_TWO => b
    );
  end for;

  for first, second, third : blah
    generic map (
      G_ONE => a,
      G_TWO => b
    )
    port map (
      I_INPUT => a,
      O_OUTPUT => b
    );
  end for;

  for first, second, third : blah
    port map (
      I_INPUT => a,
      O_OUTPUT => b
    );
  end for;

begin

end architecture RTL;
