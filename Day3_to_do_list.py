#Write function
def write_to_file(file, content):
    with open(file, "w") as f:
        f.write(content)

#Read function
def read_from_file(file):
    with open(file, 'r') as f:
        return f.read()

#Delete function
def delete_from_file(file, string_to_delete):
    with open(file, 'r') as f: #Read lines
        lines = f.readlines()
    
    with open(file, 'w') as f: #Delete line
        for line in lines:
            if line.strip("\n") != string_to_delete:
                f.write(line)


def main():
    file = "to_do.txt"
    welcome = input("Welcome to your to-do list. What do you want to do? (read/write/delete): ").strip().lower()

    if welcome == "read":
        print(read_from_file(file))
    elif welcome == "write":
        content = input("Enter the content you want to write: ")
        write_to_file(file, content)
    elif welcome == "delete":
        string_to_delete = input("Enter the string you want to delete: ")
        delete_from_file(file, string_to_delete)
    else:
        print("Invalid command. Please enter 'read', 'write', or 'delete'.")

if __name__ == "__main__":
    main()
