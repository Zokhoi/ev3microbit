# EV3/Micro:bit integration

Most of this repo follows [JorgePe's guide](https://github.com/jorgepe/microbit).

JorgePe's bluetooth hex file for micro:bit is included in `./mbit/` directory.

Use
```sh
hciconfig
```
To find the hci handle for your bluetooth adapter. Here we use `hci0`.

Then, discover micro:bit's characteristics and their handle by:
```sh
sudo gatttool -i hci0 -b <MAC-ADDRESS> -t random --characteristics
```

<details>
  <summary>Micro:bit bluetooth characteristics</summary>
  
Button A ('e95dda90-251d-470a-a062-fa1922dfa9a8') 0x27 <br />
Button B ('e95dda91-251d-470a-a062-fa1922dfa9a8') 0x2a <br />
LED Matrix ('e95d7b77-251d-470a-a062-fa1922dfa9a8') 0x2e <br />


handle = 0x0002, char properties = 0x0a, char value handle = 0x0003, uuid = 00002a00-0000-1000-8000-00805f9b34fb <br />
handle = 0x0004, char properties = 0x02, char value handle = 0x0005, uuid = 00002a01-0000-1000-8000-00805f9b34fb <br />
handle = 0x0006, char properties = 0x02, char value handle = 0x0007, uuid = 00002a04-0000-1000-8000-00805f9b34fb <br />
handle = 0x0009, char properties = 0x20, char value handle = 0x000a, uuid = 00002a05-0000-1000-8000-00805f9b34fb <br />
handle = 0x000d, char properties = 0x0a, char value handle = 0x000e, uuid = e95d93b1-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x0010, char properties = 0x14, char value handle = 0x0011, uuid = e97d3b10-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x0014, char properties = 0x02, char value handle = 0x0015, uuid = 00002a24-0000-1000-8000-00805f9b34fb <br />
handle = 0x0016, char properties = 0x02, char value handle = 0x0017, uuid = 00002a25-0000-1000-8000-00805f9b34fb <br />
handle = 0x0018, char properties = 0x02, char value handle = 0x0019, uuid = 00002a26-0000-1000-8000-00805f9b34fb <br />
handle = 0x001b, char properties = 0x12, char value handle = 0x001c, uuid = e95d9775-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x001e, char properties = 0x0c, char value handle = 0x001f, uuid = e95d5404-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x0020, char properties = 0x08, char value handle = 0x0021, uuid = e95d23c4-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x0022, char properties = 0x12, char value handle = 0x0023, uuid = e95db84c-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x0026, char properties = 0x12, char value handle = 0x0027, uuid = e95dda90-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x0029, char properties = 0x12, char value handle = 0x002a, uuid = e95dda91-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x002d, char properties = 0x0a, char value handle = 0x002e, uuid = e95d7b77-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x002f, char properties = 0x08, char value handle = 0x0030, uuid = e95d93ee-251d-470a-a062-fa1922dfa9a8 <br />
handle = 0x0031, char properties = 0x0a, char value handle = 0x0032, uuid = e95d0d2d-251d-470a-a062-fa1922dfa9a8 <br />
</details>


Also, save your micro:bit's MAC address in `config.json` as shown in `config.example.json`.