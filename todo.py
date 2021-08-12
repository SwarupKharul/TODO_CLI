import sys
import os.path
from datetime import datetime


def add_to_list(st):
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFileBefore:
            data = todoFileBefore.read()
        with open("todo.txt", 'w') as todoFileAfter:
            todoFileAfter.write(st + '\n' + data)
    else:
        with open("todo.txt", 'w') as todoFile:
            todoFile.write(st + '\n')
    print('Added todo: "{}"'.format(st))


def show_list():
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFileBefore:
            data = todoFileBefore.readlines()
        ct = len(data)
        st = ""
        for line in data:
            st = '[{}] {}'.format(ct, line) + st
            ct -= 1
        sys.stdout.buffer.write(st.encode('utf8'))
    else:
        print("There are no pending todos!")


def del_from_list(num):
    # Function to Delete the task from the List. (If available)
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFileBefore:
            data = todoFileBefore.readlines()
        ct = len(data)
        if num > ct or num <= 0:
            print(f"Error: todo #{num} does not exist. Nothing deleted.")
        else:
            with open("todo.txt", 'w') as todoFileAfter:
                for line in data:
                    if ct != num:
                        todoFileAfter.write(line)
                    ct -= 1
            print("Deleted todo #{}".format(num))
    else:
        print("Error: todo #{} does not exist. Nothing deleted.".format(num))


def mark_done(num):
    # Function to mark the given task as Done. (If available)
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFileBefore:
            data = todoFileBefore.readlines()
        ct = len(data)
        if num > ct or num <= 0:
            print("Error: todo #{} does not exist.".format(num))
        else:
            with open("todo.txt", 'w') as todoFileAfter:
                flag = 0
                if os.path.isfile('done.txt'):  # Produces output according to the availability of done.txt file.
                    flag = 1
                    with open("done.txt", 'r') as doneFileBefore:
                        doneData = doneFileBefore.read()
                with open("done.txt", 'w') as doneFileAfter:
                    for line in data:
                        if ct == num:
                            doneFileAfter.write("x " + datetime.today().strftime('%Y-%m-%d') + " " + line)
                        else:
                            todoFileAfter.write(line)
                        ct -= 1
                    if flag == 1:
                        doneFileAfter.write(doneData)
            print("Marked todo #{} as done.".format(num))
    else:
        print("Error: todo #{} does not exist.".format(num))



def print_help():
    help = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(help.encode('utf8'))


def generate_report():
    # Function to Generate the Report.
    countTodo = 0
    countDone = 0
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFile:
            todoData = todoFile.readlines()
        countTodo = len(todoData)
    if os.path.isfile('done.txt'):
        with open("done.txt", 'r') as doneFile:
            doneData = doneFile.readlines()
        countDone = len(doneData)
    st = datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(countTodo, countDone)
    sys.stdout.buffer.write(st.encode('utf8'))

def main():
    if len(sys.argv) == 1:
        print_help()
    elif sys.argv[1] == 'help':
        print_help()
    elif sys.argv[1] == 'ls':
        show_list()
    elif sys.argv[1] == 'report':
        generate_report()
    elif sys.argv[1] == 'add':
        if len(sys.argv) > 2:
            add_to_list(sys.argv[2])
        else:
            print("Error: Missing todo string. Nothing added!")
    elif sys.argv[1] == 'del':
        if len(sys.argv) > 2:
            del_from_list(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for deleting todo.")
    elif sys.argv[1] == 'done':
        if len(sys.argv) > 2:
            mark_done(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for marking todo as done.")

    else:
        print('Option Not Available. Please use "./todo help" for Usage Information')

if __name__=="__main__":
    main()