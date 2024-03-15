
entity BLOCK_EXAMPLE is
end entity BLOCK_EXAMPLE;

architecture RTL of BLOCK_EXAMPLE is

begin

  BLK : block is
  begin

    LABEL : assert TRUE
      report "This is a string"
      severity WARNING;

    -- Simple form
    a <= b;

    GEN : for ii in 0 to 7 generate

      -- Simple form
      a <= b when 'a' else
           c when 'b' else
           d;

      LABEL : assert TRUE
        report "This is a string"
        severity WARNING;

      BLK2 : block is
      begin
        assert TRUE
          report "This is a string"
          severity WARNING;


        -- Basic version
        with sel select
          out1 <= a when "00",
                  b when "01",
                  c when "10",
                  d when others;

        GEN2 : for jj in 0 to 7 generate

          -- Simple form
          simple_label : a <= b;

          assert TRUE
            report "This is a string"
            severity WARNING;


        end generate GEN2;

      end block BLK2;

    end generate GEN;

  end block BLK;


  BLK : block is
  begin

    -- Simple form
    conditional_label : a <= b when 'a' else
         c when 'b' else
         d;

    IF_GEN_LABEL: if a = x generate

        -- Basic version
        select_label : with sel select
          out1 <= a when "00",
                  b when "01",
                  c when "10",
                  d when others;

        BLK2 : block is
        begin

            LABEL : assert TRUE
              report "This is a string";
            -- Simple form
            simple_label : postponed a <= b;

            GEN2 : for jj in 0 to 7 generate

                -- Simple form
                conditional_label : postponed a <= b when 'a' else
                     c when 'b' else
                     d;
                LABEL : assert TRUE
                  report "This is a string";

                BLK3: block is
                begin

                  LABEL : assert TRUE
                    report "This is a string";

                end block BLK3;

            end generate GEN2;

            BLK4 : block is
            begin

              CASE_GEN_LABEL : case a & B & c generate

                when "000" =>

                  LABEL : assert TRUE
                    report "This is a string";

                    -- Basic version
                    select_label : postponed with sel select
                      out1 <= a when "00",
                              b when "01",
                              c when "10",
                              d when others;
                    BLK4A : block is
                    begin

                      LABEL : assert TRUE
                        report "This is a string";
                      -- Simple form
                      postponed a <= b;

                    end block BLK4A;
                when "001" =>

                  -- Simple form
                  postponed a <= b when 'a' else
                       c when 'b' else
                       d;

                  IF_GEN_LABELA: if a = y generate

                    LABEL : assert TRUE
                      severity WARNING;

                    -- Basic version
                    postponed with sel select
                      out1 <= a when "00",
                              b when "01",
                              c when "10",
                              d when others;

                    BLK4B : block is
                    begin
                      LABEL : assert TRUE
                        severity WARNING;

                      -- Simple form
                      conditional_label : postponed a <= b when 'a' else
                           c when 'b' else
                           d;
                    end block BLK4B;

                  end generate IF_GEN_LABELA;

               end generate CASE_GEN_LABEL;

            end block BLK4;

            BLK5 : block is
            begin
                postponed assert TRUE
                  report "This is a string";

                -- Simple form
                conditional_label : postponed a <= b when 'a' else
                     c when 'b' else
                     d;
            end block BLK5;

        end block BLK2;

    end generate IF_GEN_LABEL;

    GEN : for ii in 0 to 7 generate

                -- Simple form
                conditional_label : postponed a <= b when 'a' else
                     c when 'b' else
                     d;
                postponed assert TRUE
                  report "This is a string";

        GEN2 : for jj in 0 to 7 generate
                postponed assert TRUE
                  report "This is a string";

                -- Simple form
                conditional_label : postponed a <= b when 'a' else
                     c when 'b' else
                     d;
          IF_GEN_LABEL2 : if b = y generate

                -- Simple form
                conditional_label : postponed a <= b when 'a' else
                     c when 'b' else
                     d;

            BLK2 : block is
            begin

                LABEL : postponed assert TRUE
                  report "This is a string";
                -- Simple form
                conditional_label : postponed a <= b when 'a' else
                     c when 'b' else
                     d;
            end block BLK2;

          elsif x = z generate

            BLK2 : block is
            begin

                -- Simple form
                conditional_label : postponed a <= b when 'a' else
                     c when 'b' else
                     d;

                LABEL : postponed assert TRUE
                  report "This is a string";
            end block BLK2;

        end generate IF_GEN_LABEL2;

        end generate GEN2;
    end generate GEN;

  end block BLK;

end architecture RTL;
