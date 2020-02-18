import git

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
cluster_size = comm.Get_size()

repo = git.Repo('/')
o = repo.remotes.origin
o.pull()
print('Updated repo')