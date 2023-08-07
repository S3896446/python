import requests

def get_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        # Convert the response content (JSON data) to a Python list of dictionariesSet-ExecutionPolicy Unrestricted -Forc
        todos = response.json()

        # Print the todos
        for todo in todos:
            print(f"Todo UserID: {todo['userId']}")
            print(f"Todo ID: {todo['id']}")
            print(f"Title: {todo['title']}")
            print(f"Completed: {todo['completed']}")
            print("=" * 30)
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_todos()
