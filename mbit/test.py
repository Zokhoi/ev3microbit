# Testfile created by Stanley Skarshaug 16.07.2021 - Norway
# Used to test VSCode extensions for micro:bit development

from microbit import *

while True:
    print("skarshaugs.no")
    for x in range(3):
        display.show(Image.HEART_SMALL)
        sleep(500)
        display.show(Image.HEART)
        sleep(500)
        print("blog.skarshaugs.no")
    display.scroll('skarshaugs.no')