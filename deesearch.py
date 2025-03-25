import os
import webbrowser
from googlesearch import search
import pyfiglet

# Function to search the web for links based on a query
def search_web(query_string):
    print(f"\nSearching the web for: {query_string}")
    results = list(search(query_string, num_results=5))  # Get top 5 results
    if results:
        print("Search results:")
        for idx, link in enumerate(results, start=1):
            print(f" {idx}. {link}")
        return results
    else:
        print("No results found.")
        return []

# Main function
def main():
    # Print the title using pyfiglet
    title = pyfiglet.figlet_format("DeeSearch")
    print(title)

    while True:
        query_string = input("Enter your search query (or 'exit' to quit): ")
        if query_string.lower() == 'exit':
            break

        links = search_web(query_string)

        # Ask user if they want to open a link
        if links:
            choice = input("Would you like to open a link? (y/n): ")
            if choice.lower() == 'y':
                link_number = int(input(f"Enter the number of the link to open (1-{len(links)}): "))
                if 1 <= link_number <= len(links):
                    link = links[link_number - 1]  # Adjust for zero-based index
                    webbrowser.open(link)
                else:
                    print("Invalid choice.")
            else:
                print("No link opened.")

if __name__ == "__main__":
    main()   