#!/bin/bash
#
# UT Austin Villa start penalty kicker script for 3D Simulation Competitions
#

AGENT_BINARY=utaustinvilla
BINARY_DIR="."
LIBS_DIR="./libs"
export LD_LIBRARY_PATH=$LIBS_DIR:$LD_LIBRARY_PATH

team="UTAustinVilla"
host="localhost"
port=3100

#killall -9 $AGENT_BINARY

usage()
{
  (echo "Usage: $0 [options]"
   echo "Available options:"
   echo "  --help                       prints this"
   echo "  HOST                         specifies server host (default: localhost)"
   echo "  -p, --port PORT              specifies server port (default: 3100)"
   echo "  -t, --team TEAMNAME          specifies team name") 1>&2
}


fParsedHost=false

while [ $# -gt 0 ]
do
  case $1 in

    --help)
      usage
      exit 0
      ;;

    -p|--port)
      if [ $# -lt 2 ]; then
        usage
        exit 1
      fi
      port="${2}"
      shift 1
      ;;

    -t|--team)
      if [ $# -lt 2 ]; then
        usage
        exit 1
      fi
      team="${2}"
      shift 1
      ;;

    *)
      if $fParsedHost;
      then
        echo 1>&2
        echo "invalid option \"${1}\"." 1>&2
        echo 1>&2
        usage
        exit 1
      else
        host="${1}"
	fParsedHost=true
      fi
      ;;
  esac

  shift 1
done

opt="${opt} --host=${host} --port ${port} --team ${team} --modelfiledir models/models_a/w0d5vp0d9"

DIR="$( cd "$( dirname "$0" )" && pwd )" 
cd $DIR

"$BINARY_DIR/$AGENT_BINARY" $opt --unum 2 --type 4 --pkshooter &> /dev/null &
#"$BINARY_DIR/$AGENT_BINARY" $opt --unum 2 --type 4 --pkshooter > stdoutsh 2> stderrsh &

sleep 2
