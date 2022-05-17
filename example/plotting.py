import sys
import os
BASEPATH = os.path.abspath(__file__).split('rpg_time_optimal', 1)[0]+'rpg_time_optimal/'
sys.path += [BASEPATH + 'src']
from trajectory import Trajectory
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path = './example'

traj = Trajectory(path + '/result_cpc_format.csv')
print('Total Time: %1.4fs' % traj.t_total)

fig_pos_xy = plt.figure(0, (3,3))
axhxy = fig_pos_xy.gca()
traj.plotPos(fig_pos_xy, '', plot_axis='xyq', arrow_size=3.0, arrow_nth=15, arrow_args={'color': 'k'})
axhxy.set_title('')
axhxy.grid(True)
fig_pos_xy.tight_layout()
fig_pos_xy.savefig(path + '/pos_xy.pdf')

fig_pos_xz = plt.figure(1, (3,3))
axhxz = fig_pos_xz.gca()
traj.plotPos(fig_pos_xz, '', plot_axis='xzq', arrow_size=3.0, arrow_nth=15, arrow_args={'color': 'k'})
axhxz.set_title('')
axhxz.grid(True)
fig_pos_xz.tight_layout()
fig_pos_xz.savefig(path + '/pos_xz.pdf')

fig_vel = plt.figure(2, (6, 2))
axhv = fig_vel.gca()
traj.plotVel(fig_vel, '', label=None)
axhv.grid(True)
fig_vel.legend(['$v_x$', '$v_y$', '$v_z$', '$\|v\|$'], loc='right')
fig_vel.tight_layout()
fig_vel.savefig(path + '/vel.pdf')

fig_prog = plt.figure(3, (6, 2))
axhm = fig_prog.gca()
traj.plotProgress(fig_prog, '')
axhm.grid(True)
fig_prog.tight_layout()
fig_prog.savefig(path + '/prog.pdf')

# print(traj.t_x.shape)
# print(traj.p.shape)
# print(traj.v.shape)

#增加画图
fig_thrust = plt.figure(4, (6, 2))
axht = fig_thrust.gca()
traj.plotThrust(fig_thrust, title='Thrust', plot_axis='u', astyle='-', ustyle=None)
axht.grid(True)
fig_thrust.tight_layout()
fig_thrust.savefig(path + '/thrust.pdf')

fig_traj = plt.figure(5, (10, 6))
axhtr = fig_traj.add_subplot(projection='3d')
traj.plotTraj(fig_traj, title='Trajectory', plot_axis='xyz')
axhtr.grid(True)
fig_traj.tight_layout()
fig_traj.savefig(path + '/trajectory.pdf')

fig_pt = plt.figure(6, (6, 6))
axhxt = fig_pt.add_subplot(3, 1, 1)
traj.plotPos_T(axhxt, title='Position_Time', label=None, plot_axis='x')
axhyt = fig_pt.add_subplot(3, 1, 2)
traj.plotPos_T(axhyt, title=' ', label=None, plot_axis='y')
axhzt = fig_pt.add_subplot(3, 1, 3)
traj.plotPos_T(axhzt, title=' ', label=None, plot_axis='z')
axhxt.grid(True)
axhyt.grid(True)
axhzt.grid(True)
fig_pt.tight_layout()
fig_pt.savefig(path + '/Position_Time.pdf')

fig_orientation = plt.figure(7, (6, 8))
axhorw = fig_orientation.add_subplot(4, 1, 1)
traj.plotOrientation(axhorw, title='Orientation', plot_axis='w')
axhorx = fig_orientation.add_subplot(4, 1, 2)
traj.plotOrientation(axhorx, title=' ', plot_axis='x')
axhory = fig_orientation.add_subplot(4, 1, 3)
traj.plotOrientation(axhory, title=' ', plot_axis='y')
axhorz = fig_orientation.add_subplot(4, 1, 4)
traj.plotOrientation(axhorz, title=' ', plot_axis='z')
axhorw.grid(True)
axhorx.grid(True)
axhory.grid(True)
axhorz.grid(True)
fig_orientation.tight_layout()
fig_orientation.savefig(path + '/Orientation.pdf')

fig_omega = plt.figure(8, (6, 6))
axhomx = fig_omega.add_subplot(3, 1, 1)
traj.plotOmega(axhomx, title='Bodyrate', plot_axis='x')
axhomy = fig_omega.add_subplot(3, 1, 2)
traj.plotOmega(axhomy, title=' ', plot_axis='y')
axhomz = fig_omega.add_subplot(3, 1, 3)
traj.plotOmega(axhomz, title=' ', plot_axis='z')
axhomx.grid(True)
axhomy.grid(True)
axhomz.grid(True)
fig_omega.tight_layout()
fig_omega.savefig(path + '/Bodyrate.pdf')