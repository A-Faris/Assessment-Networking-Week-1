"""Tests for challenge 2."""

# pylint: skip-file

import pytest


def test_get_messages_for_valid_storage_id(test_user, run_shell_command):

    output = run_shell_command(
        f"python3 storetoise_2.py --username {test_user} --storage 100")

    assert "0) an example message" in output
    assert "1) another example message" in output


def test_get_messages_for_valid_storage_id_short_name(test_user, run_shell_command):

    output = run_shell_command(
        f"python3 storetoise_2.py --username {test_user} --s 100")

    assert "0) an example message" in output
    assert "1) another example message" in output


def test_get_messages_for_valid_storage_id_short_names(test_user, run_shell_command):

    output = run_shell_command(f"python3 storetoise_2.py -u {test_user} -s 100")

    assert "0) an example message" in output
    assert "1) another example message" in output


@pytest.mark.parametrize("inp", ["23", "2000", "-12", "-123", "knives"])
def test_get_messages_rejects_invalid_storage_id(test_user, run_shell_command, inp):

    output = run_shell_command(
        f"python3 storetoise_2.py --username {test_user} --s {inp}")

    assert "Storage ID must be a three-digit integer." in output


@pytest.mark.parametrize("inp", ["101", "201", "907", "001", "080"])
def test_get_messages_rejects_non_existent_storage_id(test_user, run_shell_command, inp):

    output = run_shell_command(
        f"python3 storetoise_2.py --username {test_user} --s {inp}")

    assert "Cannot get messages for a non-existent storage ID." in output
