import logging
import time
import cipclient

# uncomment the line below to enable debugging output to console
logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] (%(threadName)-10s) %(message)s")

# set up the client to connect to hostname "processor" at IP-ID 0x0A
cip = cipclient.CIPSocketClient("192.168.88.41", 0x03)

# initiate the socket connection and start worker threads
cip.start()
time.sleep(1.5)

# you can force this client and the processor to resync using an update request
cip.update_request()  # note that this also occurs automatically on first connection

# for joins coming from the processor going to this client
# digital_1 = cip.get("d", 135)  # returns the current state of digital join 1

# you should really subscribe to incoming (processor > client) joins rather than polling
def my_callback(sigtype, join, state):
    print(f"{sigtype} {join} : {state}")

cip.subscribe("d", 1, my_callback)  # run 'my_callback` when digital join 1 changes

cip.set("a", 33, 50)

# this will close the socket connection when you're finished
cip.stop()
