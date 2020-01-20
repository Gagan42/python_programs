from git import Repo

repo_dir = 'programs'
repo = Repo(repo_dir)
file_list = [
    'python_programs\due_date.py'
]
commit_message = 'Add simple python programs'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()