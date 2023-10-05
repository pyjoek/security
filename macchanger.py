from optparse import OptionParser
import subprocess as sp

parser = OptionParser()

parser.add_option("-i","--interface",dest="interface",help = "Enter your interface to be used")
parser.add_option("-m","--macadres",dest = "macadres", help = "Enter your Mac Address")

(options, arguments) = parser.parse_args()

macadres = options.macadres
interface = options.interface

sp.call(f"sudo ifconfig {interface} down",shell=True)
sp.call(f"sudo ifconfig {interface} hw ether {macadres}",shell=True)
sp.call(f"sudo ifconfig {interface} up",shell=True)
