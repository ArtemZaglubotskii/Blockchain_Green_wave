from __future__ import absolute_import
from __future__ import print_function


import os
import subprocess
import sys
import shutil
import asyncio


try:
    sys.path.append(os.path.join(os.path.dirname(
        __file__), '..', '..', '..', '..', 'tools'))  # tutorial in tests
    sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(
        os.path.dirname(__file__), "..", "..", "..")), 'tools'))  # tutorial in docs
    from sumolib import checkBinary
    import traci
except ImportError:
    sys.exit(
        "please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

netconvertBinary = checkBinary('netconvert')
sumoBinary = checkBinary('sumo')


# build/check network
retcode = subprocess.call(
    [netconvertBinary, "-c", "./cross3l.netccfg"], stdout=sys.stdout, stderr=sys.stderr)
print(">> Netbuilding closed with status %s" % retcode)
sys.stdout.flush()

# run simulation
retcode = subprocess.call(
    [sumoBinary, "-c", "./cross3l.sumocfg", "--no-step-log"], stdout=sys.stdout, stderr=sys.stderr)
print(">> Simulation closed with status %s" % retcode)
sys.stdout.flush()

# start the simulation and connect to it with the script: 

from src import parse

out_file = './out.xml'
net_file = './net.net.xml'
buckets=20
net = parse.parse_net(net_file)



step_length = 1

traci.start([checkBinary('sumo-gui'), '-c',"./cross3l.sumocfg", '--step-length', str(step_length)])

vehicles = []
start_vel = 5 
step = 0 
sidVehicle = {} # vehicles that want to do side move



# Run a simulation until all vehicles have arrived
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()



    step += 1

print(net)
traci.close()