#!/bin/bash
#
# UT Austin Villa start script for 3D Simulation Competitions
#


AGENT_BINARY=utaustinvilla
BINARY_DIR="."
LIBS_DIR="./libs"
NUM_PLAYERS=1

team="defender"
host="localhost"
port=3100


export LD_LIBRARY_PATH=$LIBS_DIR:$LD_LIBRARY_PATH

#killall -9 "$AGENT_BINARY" &> /dev/null


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

echo "UT Austin Villa 2019 3D Simulation Team"

opt="${opt} --host=${host} --port ${port} --team ${team} --modelfiledir models/models_a/w0d5vp0d9 --modelfiledir2 models/models_b/w0d75vp0d75"

DIR="$( cd "$( dirname "$0" )" && pwd )" 
cd $DIR

for ((i=1;i<=$NUM_PLAYERS;i++)); do
    case $i in
	-1)
	    echo "Running agent No. $i -- Type 0"
	    "$BINARY_DIR/$AGENT_BINARY" $opt --unum $i &> /dev/null &
	    #"$BINARY_DIR/$AGENT_BINARY" $opt --unum $i > stdout$i 2> stderr$i &
	    ;;
	1|7)
	    echo "Running agent No. $i -- Type 1"
	    "$BINARY_DIR/$AGENT_BINARY" $opt --unum $i --type 1 &> /dev/null &
	    #"$BINARY_DIR/$AGENT_BINARY" $opt --unum $i --type 1 > stdout$i 2> stderr$i &
	    ;;
	-1)
	    echo "Running agent No. $i -- Type 2"
	    "$BINARY_DIR/$AGENT_BINARY" $opt --unum $i --type 2 &> /dev/null &
	    #"$BINARY_DIR/$AGENT_BINARY" $opt --unum $i --type 2 > stdout$i 2> stderr$i &
	    ;;
	8|9)
	    echo "Running agent No. $i -- Type 3"
	    "$BINARY_DIR/$AGENT_BINARY" $opt --unum $i --type 3 &> /dev/null &
	    #"$BINARY_DIR/$AGENT_BINARY" $opt --unum $i --type 3 > stdout$i 2> stderr$i &
	    ;;
	*)
	    echo "Running agent No. $i -- Type 4"
	    "$BINARY_DIR/$AGENT_BINARY" $opt --unum $i --type 4 &> /dev/null &
	    #"$BINARY_DIR/$AGENT_BINARY" $opt --unum $i --type 4 > stdout$i 2> stderr$i &
	    ;;
    esac
    sleep 1
done


