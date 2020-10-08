"""
updatingFunctions.py

Created on 2020-10-07
Updated on 2020-10-08

Copyright Ryan Kan 2020

Description: A file which handles the processes that are needed to update The Challenge.
"""

# IMPORTS
import re
import socket
from base64 import b64decode

import requests
import simplejson as json


# FUNCTIONS
def check_internet_connection():
    """
    Checks whether the user is connected to the internet or not.

    Returns:
        bool: Whether the user is connected to the internet or not.
    """

    try:
        socket.create_connection(("www.example.com", 80), 1.25)  # Tries to connect to the IANA's example website

    except OSError:
        return False

    return True


def check_token(token):
    """
    Checks whether the given is correct or not.

    Args:
        token (Optional[str]): The github access token.

    Returns:
        bool: Whether the token is correct or not.
    """

    # Check if token is None
    if token is None:
        return False

    # Form header
    header = {"Authorization": "token %s" % token}

    request = requests.get("https://api.github.com/repos/Ryan-Kan/The-Challenge/commits/master", headers=header)

    # Check if got response
    try:
        request.raise_for_status()
        return True

    except requests.HTTPError:
        return False


def get_most_recent_version(token):
    """
    Gets the most recent version of The Challenge from GitHub.

    Args:
        token (Optional[str]): The github access token.

    Returns:
        Union[None, str]: The most recent version.
        Union[None, dict]: The files of the most recent version.
    """

    # Generate the header
    header = {"Authorization": "token %s" % token}

    # Get the latest commit's SHA
    latest_commit = requests.get("https://api.github.com/repos/Ryan-Kan/The-Challenge/commits/master", headers=header)
    latest_commit_sha = json.loads(latest_commit.text)["sha"]

    # Get the latest commit's files
    latest_commit_files = requests.get(
        f"https://api.github.com/repos/Ryan-Kan/The-Challenge/git/trees/{latest_commit_sha}?recursive=true",
        headers=header)
    latest_commit_files = json.loads(latest_commit_files.text)["tree"]

    # Find the url to the latest version file
    version_file = ""
    for file in latest_commit_files:
        if file["path"].find("version.py") != -1:
            version_file = file["url"]
            break

    # Check if the version file's url was found
    if version_file != "":
        # Get the contents of the version file
        version_file_content = requests.get(version_file, headers=header)
        version_file_content = str(b64decode(json.loads(version_file_content.text)["content"]), encoding="UTF-8")

        # Find the version that is in the file
        most_recent_version = re.findall('"([^"]*)"', version_file_content)[0]
        return most_recent_version, latest_commit_files

    else:
        return None, None