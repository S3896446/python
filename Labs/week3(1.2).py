import requests

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        # Convert the response content (JSON data) to a Python list of dictionariesSet-ExecutionPolicy Unrestricted -Forc
        posts = response.json()

        # Print the posts
        for post in posts:
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
            print("=" * 30)
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_posts()
