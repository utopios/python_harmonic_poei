import sys

sys.path.append("../")
sys.path.append("../tasks_api_folder")

from tasks_api_folder import tasks
from tasks_api_folder.tasks import Task


def initialized_tasks_db():
    tasks.start_tasks_db(str('temp'), 'tiny')

def stop_tasks_db():
    tasks.stop_tasks_db()

# def equivalent(t1, t2):
#     """Check if 2 tasks are equivalence"""
#     return ((t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done))


def equivalent(t1, t2, task_id):
    """Check if 2 tasks are equivalence"""
    return ((t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done) and t2.id == task_id)