#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import random

def get_vim_command_of_the_day():
    # URL of the website
    url = "https://vim.rtorr.com/"

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all <li> tags containing Vim commands
        li_elements = soup.find_all("li")

        # Extract Vim commands from <li> tags
        vim_commands = []
        for li in li_elements:
            kbd_element = li.find("kbd")
            if kbd_element:
                # Get the text of the <kbd> element
                vim_command = kbd_element.text.strip()
                # Get the description after the <kbd> element
                description = kbd_element.find_next_sibling(text=True).strip()
                # Combine command and description
                vim_commands.append(f"{vim_command} {description}")

        if vim_commands:
            # Return a random Vim command
            return random.choice(vim_commands)
        else:
            return None
    else:
        return None

def main():
    # Get a random Vim command of the day
    vim_command = get_vim_command_of_the_day()

    if vim_command:
        print("Command of the Day for Vim:")
        # Print the Vim command
        print(vim_command)
    else:
        print("Failed to fetch the Vim command of the day.")

if __name__ == "__main__":
    main()

