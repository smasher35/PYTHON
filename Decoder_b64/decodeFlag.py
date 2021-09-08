import base64
from progress.bar import Bar
from progress.bar import ShadyBar
import time
from termcolor import colored
from banner import banner


banner()                                                                                    
print("\n")
    
def decodeFile(message, base):
    # Encoding the Base16 encoded string into bytes
    base_bytes = message.encode("UTF-8")
    # Decoding the Base16 bytes
    if base == 16:
        message_bytes = base64.b16decode(base_bytes)
    elif base == 32:
        message_bytes = base64.b32decode(base_bytes)
    elif base == 64:
        message_bytes = base64.b64decode(base_bytes)
    else:
        return "[-] . Wrong base to decode please enter 16, 32 or 64"

    # Decoding the bytes to string
    decodedMessage = message_bytes.decode("UTF-8")
    return decodedMessage

base=0
flagFile = open("E:\\PROGRAMING\\PYTHON\\Decoder_b64\\encodedflag.txt", "r")
message = flagFile.read()
print(colored('[+] - ', 'green') + "Encoded file opened with success")
dot ="."
bar = ShadyBar(colored('[o] - ', 'yellow') + "Decoding", max=15)
for index in range(15):
    if index < 5:
        base = 16
    elif index >=5 and index < 10:
        base = 32
    else:
        base = 64
    decodedMessage = decodeFile(message, base )
    message = decodedMessage
    bar.next()
    time.sleep(0.01) # controls the speed of the progress bar
bar.finish()
for index in range(85):
    print("-",end = '')
print("")
print(colored('[+] - ', 'green')+ message)
for index in range(85):
    print("-",end = '')




