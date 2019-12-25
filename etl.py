from extract import extract_projects, extract_tasks
from load import load_projects, load_tasks
from transform import clean_projects, clean_tasks

def projects_data():
    load_projects(clean_projects())
    
def tasks_data():
    load_tasks(clean_tasks())
    
def main():
    projects_data()
    tasks_data()


main()
