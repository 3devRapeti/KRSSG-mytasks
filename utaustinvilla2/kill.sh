#!/bin/bash
#
# IranOpen 2008 sample kill script for 3D Simulation Competitions
#

# Kill agents
AGENT="utaustinvilla"
killall -9 $AGENT
sleep 1


# Kill server
#SERVER="simspark"
#SERVER="rcssserver3d rcssmonitor3d simspark"
#killall -9 $SERVER
#sleep 1

