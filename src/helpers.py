import os
import requests
import datetime
from bs4 import BeautifulSoup

CURRENT_DATETIME = datetime.datetime.now()


def readBoolEnvVar(key: str, default_value: bool):
    return os.getenv(key, default_value).lower() in ('true', 't', '1')


def print_criteria_not_met(team_name: str):
    print(f"✗ - {team_name} didn't meet the criteria")


def print_not_in_season(team_name: str):
    print(f"✗ - {team_name} are not in season")


def generate_email_subject(team_name: str) -> str:
    return f"{team_name} Chick Fil A Reminder"


def fetch_soup(url: str) -> BeautifulSoup:
    """ 
    Makes HTTP GET request to the URL and loads it into BS4 for further parsing 
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup


def check_yesterday(game_date: datetime) -> bool:
    """ 
    Checks to see if the day of the game was yesterday 
    """

    return (CURRENT_DATETIME.date() - game_date == datetime.timedelta(days=1))
