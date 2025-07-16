
package interfaces is

    view streaming of streaming_bus is
        valid, data : out;
        ack         : in;
        nested      : view inner_streaming_bus;
    end view streaming;

end package;

architecture rtl of entity1 is

    view streaming of streaming_bus is
        valid, data : out;
        ack         : in;
    end view;

  begin
    b1 : block

        view streaming of streaming_bus is
            valid, data : out;
            ack         : in;
        end view;

    begin

    end block;

end architecture rtl;
