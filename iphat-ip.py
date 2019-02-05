from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
import socket, fcntl, struct, platform

# CHANGE THESE VARIABLES TO YOUR CONFIGURATION.
inf = "wlan0" # Change to whatever device you want the IP to be displayed for.
clr = "red"   # Change "red" to match the device you own ("red","yellow","bw")

inky_display = InkyPHAT(clr)
host= platform.uname()[1]
def get_ip_address(ifname):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])
inky_display.set_border(inky_display.WHITE)
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
font12 = ImageFont.truetype('fonts/Comfortaa.ttf', 12)
font28 = ImageFont.truetype('fonts/Comfortaa.ttf', 28)
addrtext = "My " + inf +" IP address is:"
ipaddr = get_ip_address(inf)
w, h = font12.getsize(addrtext)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)
w2, h2 = font28.getsize(ipaddr)
x2 = (inky_display.WIDTH / 2) - (w2 / 2)
y2 = (inky_display.HEIGHT / 2) - (h2 / 2)
draw.text((0, 0), host, inky_display.RED, font12)
draw.text((x, y-14), addrtext, inky_display.RED, font12)
draw.text((x2, y2+7), ipaddr, inky_display.RED, font28)
inky_display.set_image(img)
inky_display.show()
