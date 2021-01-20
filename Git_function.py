import os
class to_Git(object):
    """
    Git function will clone the repository from GitHub, add the files, commit them and push to main branch
    
    """
    
    def __init__(self, repo=''):
        """
        Constructor
            
        Parameters
        ----------
            @repo: repository to clone and push
        """
        self.file_name = 'file_name'
        self.repo = repo
        self.message = 'message'
    
    def add_file(self, file_name = ''):
        """
        Adding the file to tracking
        
        Parameters
        ----------
            @file_name: name of file to push
        """
        self.file_name = file_name
        os.system(f'git add {self.file_name}')
        print(f'file {self.file_name} was added to tracking')
    
    def add_commit(self, message=''):
        """
        Add commit to tracking file
        
        Parameters
        ----------
            @message: message to commit
        """
        os.system(f'git commit -m {message}')
        print(f'commit {message} was added to tracking file {self.file_name}')
        self.message = str(message)
        
    def push(self):
        """
        Push the tracking file/s to repository 
        
        """
        os.system(f'git push')
        print(f'{self.file_name} was added to {self.repo} with commit {self.message}')
        
    def get_repo(self, store_to=''):
        """
        Get the full repository from source
        and store it to defined directory
        
        Parametrs:
        ----------
            @store_to: set the directory where the repository
                       should be stored
        """
        os.system(f'git clone {self.repo} {store_to}')
        print(f'repository {self.repo} was clone to {store_to}')

# Example to use        
# from Git_function import *

file_name = './Code/task_done.ipynb'
message= 'finished task'
repo='https://github.com/leomuskul/JKU-cloud-computing_WS20.git'

git_ = to_Git(repo=repo)

git_.add_file(file_name)
git_.add_commit(message)
git_.push()
