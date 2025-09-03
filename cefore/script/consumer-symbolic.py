import cefpyco

with cefpyco.create_handle() as handle:
    while True:
        handle.send_symbolic_interest("ccnx:/test_sim")
        info = handle.receive()
        if info.is_succeeded and (info.name == "ccnx:/test_sim"):
            print("Success")
            print(info)
            # break
