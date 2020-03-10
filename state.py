class State(object):
    def run(self):
        assert 0, "run not implemented"
    def next(self, input):
        assert 0, "next not implemented"

class idle(State):
    print("lift is stationay..")

class moving(State):
    print("lift is moving..")