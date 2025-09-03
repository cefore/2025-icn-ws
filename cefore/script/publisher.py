import cefpyco

with cefpyco.create_handle() as handle:
    handle.register("ccnx:/test")
    while True:
        info = handle.receive()
        if info.is_succeeded and (info.name == "ccnx:/test") and (info.chunk_num == 0):
            handle.send_data("ccnx:/test", "hello", 0)
            print(info)
