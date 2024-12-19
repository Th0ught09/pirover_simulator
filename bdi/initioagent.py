import bdi.bdiagent as agent
import simclient.simrobot as initio


class InitioAgent(agent.Agent):
    def __init__(self):
        agent.Agent.__init__(self)
        self.initialised = 0
        self.robot = initio

    def getpercepts(self, beliefbase):
        dist = initio.getDistance()
        beliefbase["distance"] = dist
        irR = initio.irRight()
        beliefbase["obstacle_right"] = irR
        irL = initio.irLeft()
        beliefbase["obstacle_left"] = irL
        irLL = initio.irLeftLine()
        beliefbase["line_left"] = irLL
        irRL = initio.irRightLine()
        beliefbase["line_right"] = irRL
        super()
        return

    def getPercepts(self):
        self.getpercepts(self.beliefbase)

    def run_agent(self):
        if not (self.initialised):
            initio.init()
            self.initialised = 1
        super().run_agent()

    def init(self):
        initio.init()

    def cleanup(self):
        initio.cleanup()
