#Part 1: Implementing a Stack
class Stack:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2


#Part 2: Implementing a Queue
class Queue:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2


#Part 3: Solving Practical Problems
#Problem 1: Balanced Parentheses
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False


#Problem 2: Reverse a String
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"


#Problem 3: Hot Potato Simulation
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Sonam", "Ugyen", "Phuntsho", "Jigden", "Namgay", "Cheodey"]
print(hot_potato(names, 7))  # The winner's name will be printed

print()
print("Exercises Part")
print("--------------------")
#Evaluating Postfix expressions
def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit():  # If the token is a number, push it onto the stack
            stack.push(int(token))
        elif token in operators:  # If the token is an operator
            # Pop the top two numbers from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Apply the operator and push the result back onto the stack
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2  # Use integer division (//) if needed

            stack.push(result)

    # The result should be the only item left in the stack
    return stack.pop()

# Test the function
print(evaluate_postfix("5 3 +"))       # Should print 8
print(evaluate_postfix("10 2 * 3 +"))  # Should print 23
print(evaluate_postfix("10 2 8 * + 3 -"))  # Should print 23


#Two-stack Queue Implementation
class QueueWithTwoStacks:
    def _init_(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            # Transfer only if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Pop from stack_out, which now has the oldest elements on top
        if not self.stack_out:
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

# Test the simplified QueueWithTwoStacks
queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.dequeue())  # Should print 2
print(queue.is_empty()) # Should print False
queue.enqueue(4)
print(queue.dequeue())  # Should print 3
print(queue.dequeue())  # Should print 4
print(queue.is_empty()) # Should print True

print()
print("Task Scheduler")
print("--------------")
class TaskScheduler:
    def _init_(self):
        self.queue = []  # Initialize an empty list to serve as the queue

    def add_task(self, task):
        """Add a task to the scheduler."""
        self.queue.append(task)
        print(f"Task added: {task}")

    def process_task(self):
        """Process the next task in the queue."""
        if self.queue:
            task = self.queue.pop(0)  # Remove the task from the front of the queue
            print(f"Processing task: {task}")
            return task
        else:
            print("No tasks to process.")
            return None

    def is_empty(self):
        """Check if the task queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Get the number of tasks in the queue."""
        return len(self.queue)

# Example usage
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")

# Process all tasks
while not scheduler.is_empty():
    scheduler.process_task()

# Attempt to process a task when the queue is empty
scheduler.process_task()