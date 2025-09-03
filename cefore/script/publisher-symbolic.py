import cefpyco
from time import sleep

chunkNum=0
with cefpyco.create_handle() as handle:
    handle.register("ccnx:/test_sim")
    while True:
        handle.send_data("ccnx:/test_sim", "hello", chunkNum)
        print("Send Data, ccnx:/test_sim, chunkNum=", chunkNum, sep='')
        chunkNum += 1
        sleep (1)
