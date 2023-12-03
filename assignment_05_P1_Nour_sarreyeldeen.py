import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

class FamilyMember:
    def __init__(self, name, family_name, birthdate):
        self.name = name
        self.family_name = family_name
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        self.children = []
        

def add_family_member(family_tree, name, family_name, birthdate, parent=None):
    new_member = FamilyMember(name, family_name, birthdate)
    if parent:
        parent.children.append(new_member)
    family_tree.append(new_member)

def allbirthdates(member):
    return member.birthdate.year, member.birthdate.month, member.birthdate.day

def display_sorted_birthdays(family_tree):
    sorted_birthdays = sorted(family_tree, key=allbirthdates)
    for member in sorted_birthdays:
        print(f"{member.name} {member.family_name}: {member.birthdate.strftime('%Y-%m-%d')}")

def find_relationship():
    x=0
def visualize_family_tree(family_tree):
    G = nx.DiGraph()

    for member in family_tree:
        G.add_node(f"{member.name} {member.family_name}\n{member.birthdate.strftime('%Y-%m-%d')}")

    for member in family_tree:
        for child in member.children:
            G.add_edge(f"{member.name} {member.family_name}\n{member.birthdate.strftime('%Y-%m-%d')}",
                       f"{child.name} {child.family_name}\n{child.birthdate.strftime('%Y-%m-%d')}")

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, font_size=8, font_color='black',
            node_size=800, node_color='skyblue', font_weight='bold', edge_color='gray', linewidths=1, alpha=0.5)
    plt.show()

def count_same_first_names(family_tree, first_name):
    same_first_name_count = sum(1 for member in family_tree if member.name == first_name)
    return same_first_name_count

def main():
    family_tree = []

    while True:
        print("-" * 30)
        print("1. Add Family Member")
        print("2. Display Sorted Birthdays")
        print("3. Find Relationship")
        print("4. Visualize Family Tree")
        print("5. Count Same First Names")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter member's name: ")
            family_name = input("Enter member's family name: ")
            birthdate = input("Enter member's birthdate (YYYY-MM-DD): ")
            parent_name = input("Enter parent's name (if any): ")

            parent = next((member for member in family_tree if member.name == parent_name), None)
            add_family_member(family_tree, name, family_name, birthdate, parent)

        elif choice == 2:
            display_sorted_birthdays(family_tree)

        elif choice == 3:
            h=0

        elif choice == 4:
            visualize_family_tree(family_tree)

        elif choice == 5:
            first_name = input("Enter first name to count: ")
            count = count_same_first_names(family_tree, first_name)
            print(f"There are {count} with that name.")

        elif choice == 6:
            break

if __name__ == "__main__":
    main()

