class Task:
    def __init__(self, task_id, description, priority, completed=False):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.completed = completed

    def getTask_id(self):
        return self.task_id
    
    def getDescription(self):
        return self.description
    
    def getPriority(self):
        return self.priority
    
    def getCompleted(self):
        return self.completed
    
    def setTask_id(self, new_taskid):
        self.task_id = new_taskid

    def setDescription(self, new_description):
        self.description = new_description

    def setPriority(self, new_priority):
        self.priority = new_priority

    def setCompleted(self, new_completed):
        self.completed = new_completed

    def __str__(self):
        return f"Task {self.task_id}: {self.description} (Priority: {self.priority}, Completed: {self.completed})"


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, task):
        new_node = Node(task)
        if self.__size == 0 or task.priority > self.front.task.priority:
            new_node.next = self.front
            self.front = new_node
            self.__size += 1
        else:
            current = self.front
            while current.next and task.priority <= current.next.task.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            print("Your Queue is Empty! Enqueue first.")
        removed_task = self.front.task
        self.front = self.front.next
        self.__size -= 1
        return removed_task

   
class Stack:
    def __init__(self):
        self.top = None

    def push(self, task):
        new_node = Node(task)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        removed_task = self.top.task
        self.top = self.top.next
        return removed_task

    def is_empty(self):
        return self.top is None


class TaskManager:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.task_history = Stack()
        self.task_counter = 1

    def add_task(self, description, priority):
        new_task = Task(self.task_counter, description, priority)
        self.task_counter += 1
        self.task_queue.enqueue(new_task)

    def get_task(self, task_id):
        current = self.task_queue.front
        while current:
            if current.task.task_id == task_id:
                print(current.task)
                return current.task
            current = current.next
        print(f"Task with ID {task_id} not found.")
        return None

    def mark_highest_priority_completed(self):
        if not self.task_queue.is_empty():
            completed_task = self.task_queue.dequeue()
            completed_task.completed = True
            self.task_history.push(completed_task)
            print(f"Task {completed_task.task_id} is completed.")
        else:
            print("Task queue is empty.")

    def display_all_tasks(self):
        current = self.task_queue.front
        while current:
            print(current.task)
            current = current.next

    def display_incomplete_tasks(self):
        current = self.task_queue.front
        while current:
            if not current.task.completed:
                print(current.task)
            current = current.next

    def display_last_completed_task(self):
        last_completed = self.task_history.pop()
        if last_completed:
            print(f"Last Completed Task: {last_completed}")
        else:
            print("No completed tasks yet.")


task_manager = TaskManager()

while True:
    print("\nTask Manager Menu:")
    print("1. Add a new task")
    print("2. Get a task by ID")
    print("3. Mark highest priority task as completed")
    print("4. Display all tasks in order of priority")
    print("5. Display only incomplete tasks")
    print("6. Display last completed task")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            description = input("Enter description: ")
            priority = int(input("Enter priority: "))
            task_manager.add_task(description, priority)
        elif choice == 2:
            task_id = int(input("Enter task ID: "))
            task_manager.get_task(task_id)
        elif choice == 3:
            task_manager.mark_highest_priority_completed()
        elif choice == 4:
            task_manager.display_all_tasks()
        elif choice == 5:
            task_manager.display_incomplete_tasks()
        elif choice == 6:
            task_manager.display_last_completed_task()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

        #Task Class:

#The Task class represents a task with attributes such as task_id, description, priority, and completed.
#The __str__ method provides a formatted string representation of the task when it needs to be printed.
#Node Class:

#The Node class defines a node for a linked list. Each node contains a task and a reference to the next node in the list.
#PriorityQueue Class:

#The PriorityQueue class implements a priority queue using a linked list. Tasks are enqueued in order of priority.
#The enqueue method adds tasks to the queue, maintaining order based on priority.
#The dequeue method removes and returns the task with the highest priority from the queue.
#The is_empty method checks if the priority queue is empty.
#Stack Class:

#The Stack class implements a stack using a linked list.
#The push method adds tasks to the top of the stack.
#The pop method removes and returns the task from the top of the stack.
#The is_empty method checks if the stack is empty.
#TaskManager Class:

#The TaskManager class manages the overall functionality of the task management system.
#It has a task_queue (PriorityQueue) to store tasks and a task_history (Stack) to track completed tasks.
#The add_task method creates a new task and adds it to the priority queue.
#The get_task method searches for a task by ID in the priority queue and prints its details.
#The mark_highest_priority_completed method dequeues the task with the highest priority, marks it as completed, and adds it to the task history stack.
#The display_all_tasks method prints details of all tasks in the priority queue.
#The display_incomplete_tasks method prints details of tasks that are not completed in the priority queue.
#The display_last_completed_task method prints details of the last completed task from the task history stack.
#Sample Usage:

#An instance of the TaskManager class (task_manager) is created.
#A while loop presents a menu to the user, allowing them to interact with the task management system.
#The user can add tasks, retrieve tasks by ID, mark tasks as completed, and display task details based on various criteria.
#In summary, this code provides a simple command-line task management system using object-oriented programming principles and linked list data structures. It organizes tasks based on priority and completion status, demonstrating a modular and extensible design. The user interface loop ensures a user-friendly interaction while handling potential input errors.
