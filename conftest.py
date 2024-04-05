"""Fixtures used by multiple tests."""

# pylint: skip-file

from os import environ as env
import subprocess

import pytest

BASE_URL = "http://sigma-storetoise-lb-698404422.eu-west-2.elb.amazonaws.com"

@pytest.fixture(scope="session", autouse=True)
def reset_user():
    user = "test_" + (env.get("USER")
                      if not env.get("GITHUB_REPOSITORY_OWNER")
                      else env.get("GITHUB_REPOSITORY_OWNER")).lower()
    subprocess.run(f"curl -X DELETE {BASE_URL}/storage/{user}".split(),
                   capture_output=True, check=True)
    print(f"{user} namespace reset.")


@pytest.fixture
def test_url():
    """The base API URL."""
    return BASE_URL


@pytest.fixture
def test_user():
    """A test username."""
    return "test_" + (env.get("USER") if not env.get("GITHUB_REPOSITORY_OWNER") else env.get("GITHUB_REPOSITORY_OWNER")).lower()

@pytest.fixture()
def run_shell_command():
    """Runs a command in the shell, returning any standard output."""

    def func(command):
        result = subprocess.run(command.split(), capture_output=True, check=True)

        return result.stdout.decode("UTF-8")

    return func

