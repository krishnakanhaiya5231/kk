# Function Definition
def greet_user(username):
    print("Hello, " + username + "!")

# Function call
greet_user("AWS")
greet_user("Linux")
greet_user("Python")
greet_user("DevOps")

# Loop for function call
topics_list=["AWS","DEVOPS","LINUX","PYTHON","DOCKER","K8s"]
for item in topics_list:
    greet_user(item)