
architecture rtl of test is

  begin

    a <= (y)sll(y)srl(y)sla(y)sra(y)rol(y)ror(y);

    a <= (x)sll(y);
    a <= (x)srl(y);
    a <= (x)sla(y);
    a <= (x)sra(y);
    a <= (x)rol(y);
    a <= (x)ror(y);

    a <= y sll y srl y sla y sra y rol y ror y;

    a <= x sll y;
    a <= x srl y;
    a <= x sla y;
    a <= x sra y;
    a <= x rol y;
    a <= x ror y;

  end architecture rtl;
