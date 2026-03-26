# Project Information and Statistics

import datetime
import platform

class ProjectInfo:
    def __init__(self):
        self.timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.user = platform.node()
        self.info = '''
        Project: My Project Info
        Owner: WOLFbl4
        Description: This project provides comprehensive information and statistics of the repository.
        '''

    def display_info(self):
        print(f'Current Date and Time (UTC): {self.timestamp}')
        print(f'Current User's Login: {self.user}')
        print(self.info)

if __name__ == '__main__':
    project_info = ProjectInfo()
    project_info.display_info()