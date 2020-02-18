import git

repo = git.Repo('/')
o = repo.remotes.origin
o.pull()
print('Updated repo')