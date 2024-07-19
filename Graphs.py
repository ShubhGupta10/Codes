import matplotlib.pyplot as plt
def line_graph():
    # Simple line plot
    n=int(input("Enter the number of enteries\t:"))
    x=[];y=[]
    for i in range(1,n+1):
        print(i)
        a=int(input("Enter value on X-Axis \t:"))
        b=int(input("Enter value on Y-Axis \t:"))
        x.append(a);y.append(b)
    print(x,y)
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Plot')
    plt.show()
# Initialize an empty dictionary to store lists
user_lists = {}
n=int(input("Enter no. of lists\t:"))
for i in range(n):
    # Ask the user for the name of the list
    list_name = input("Enter the name for the list: ")

    # Create an empty list with the given name
    user_lists[list_name] = []

    # Ask the user to enter elements for the list
    while True:
        element = input(f"Enter an element for the list '{list_name}' (or type 'done' to finish): ")
        if element.lower() == 'done':
            break
        user_lists[list_name].append(element)

    # Display the list
    print(f"The list '{list_name}' contains: {user_lists[list_name]}")
print(user_lists)
for j in user_lists.items():
    print(j)
    print(j[1])
    #Bar Chart
    plt.figure(figsize=(14,7))
    plt.bar(states,deaths,color='green')
    plt.xlabel("States");plt.ylabel("Number of deaths")
    plt.xticks(rotation=45)
    plt.show()
