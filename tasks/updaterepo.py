import git
from mpi4py import MPI

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
controller = False

repo = git.Repo('/home/user/cluster')
o = repo.remotes.origin
o.pull()

if my_rank == 0:
    controller = True

if controller:
    print('Updated repo on controller 0')
else:
    print('Updated repo on node',str(my_rank))
