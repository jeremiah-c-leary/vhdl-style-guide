
architecture RTL of BLOCK_EXAMPLE is

begin

  -- correct block format
  BLK : block is

    generic (
      A : std_logic;
      B : integer;
      E, F : positive
    );
    generic map (
      A => B,
      B => C,
      E => X,
      F => Z
    );

    port (
      A : std_logic;
      B : integer;
      E, F : positive
    );
    port map (
      A => B,
      B => C,
      E => X,
      F => Z
    );

  begin

  end block BLK;

  -- correct block format
  BLK : block is

    generic map (
      A => B,
      B => C,
      E => X,
      F => Z
    );

    port (
      A : std_logic;
      B : integer;
      E, F : positive
    );
    port map (
      A => B,
      B => C,
      E => X,
      F => Z
    );

  begin

  end block BLK;

  -- correct block format
  BLK : block is

    generic (
      A : std_logic;
      B : integer;
      E, F : positive
    );
    port (
      A : std_logic;
      B : integer;
      E, F : positive
    );
    port map (
      A => B,
      B => C,
      E => X,
      F => Z
    );

  begin

  end block BLK;

  -- correct block format
  BLK : block is

    generic (
      A : std_logic;
      B : integer;
      E, F : positive
    );
    generic map (
      A => B,
      B => C,
      E => X,
      F => Z
    );

    port map (
      A => B,
      B => C,
      E => X,
      F => Z
    );

  begin

  end block BLK;

  -- correct block format
  BLK : block is

    generic (
      A : std_logic;
      B : integer;
      E, F : positive
    );
    generic map (
      A => B,
      B => C,
      E => X,
      F => Z
    );

    port (
      A : std_logic;
      B : integer;
      E, F : positive
    );

  begin

  end block BLK;

end architecture RTL;

