import sys
import os
BASEPATH = os.path.abspath(__file__).split('time_optimal_trajectory', 1)[0]+'time_optimal_trajectory/'
sys.path += [BASEPATH + 'src']
from track import Track
from quad import Quad
from integrator import RungeKutta4
from planner import Planner
from trajectory import Trajectory
from plot import CallbackPlot

track = Track(BASEPATH + "/tracks/track.yaml")
quad = Quad(BASEPATH + "/quads/quad.yaml")

cp = CallbackPlot(pos='xy', vel='xya', ori='xyzw', rate='xyz', inputs='u', prog='mn')
planner = Planner(quad, track, RungeKutta4, {'tolerance': 0.3, 'nodes_per_gate': 40, 'vel_guess': 3.0})
planner.setup()
planner.set_iteration_callback(cp)
x = planner.solve()

traj = Trajectory(x, NPW=planner.NPW, wp=planner.wp)
traj.save(BASEPATH + '/example/result_cpc_format.csv', False)
traj.save(BASEPATH + '/example/result.csv', True)

