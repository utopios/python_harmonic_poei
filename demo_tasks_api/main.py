from init import *


def main():
    tasks.start_tasks_db(str('temp'), 'tiny')

    task = Task('start pytest', owner='me', done=False)

    tasks.add(task)

    tasks.stop_tasks_db()

if __name__ == "__main__":
    main()