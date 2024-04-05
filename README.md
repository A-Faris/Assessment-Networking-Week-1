# Storetoise CLI

## Scenario

Storetoise is a new tech startup that has raised far more funding than its ideas or execution warrant. Their flagship product is the Storetoise API, which allows users to insecurely store simple data online.

You've been hired as a contractor by Storetoise, and tasked with making a command-line interface app for the API.

You can find the Storetoise API and the full documentation on how to use it here:

> http://sigma-storetoise-lb-698404422.eu-west-2.elb.amazonaws.com/

## Setup

Please ensure you do every step below carefully. Not doing so will mean we can't assess your work and **will result in a score of zero**.

1. Create a repo named exactly `Assessment-Networking-Week-1`
2. Invite your coaches to it (they'll let you know they Github usernames)
3. Push all the code in this folder to your created repository
4. On your created repo, click on `Actions` in the top menu bar
   - If it's there, click on `I understand my workflows, go ahead and enable them`
5. Complete the assessment
6. Commit & push your code regularly

## Guidance

### General

- **Read all the instructions** carefully. Twice.
- **Use the tests** to guide your work.
- You are assessed on **both** the number of tests that pass and code quality, though **passing tests is more important**.
- You **are** allowed to us online documentation and Google to help you

### Specific

- The storetoise API is live and in use; to avoid confusion/crossed wires with other users, use only **your GitHub username** as a namespace when developing your solution
- The tests (both locally and on GH) will use a different username and namespace to you; don't hardcode your username anywhere
- If your solution relies on libraries that are not listed in `requirements.txt`, the tests will fail on GitHub
- You do **not** need to write any of your own tests (except when attempting the extension tasks)
- Make sure success and error messages are printed **exactly** as below. You will fail tests if they are not exactly the same.
- Work through the challenges in order; each one should make the next one easier.

## Tasks

Create a CLI app for the Storetoise service. The full functionality of the API has been broken down into a number of challenges.

Each challenge builds on the one before it; adding new features to the app should **never** lead to existing features breaking.

Complete each challenge in a a separate file, beginning with `storetoise_1.py`. At the start of each new challenge, copy all the code from the previous file into the new one, and then begin working in the **new** file.

### Challenge 1: View existing storage IDs

Write all your code in `storetoise_1.py` for this challenge.

`python3 storetoise_1.py --username XXXXX` should `print()` a list of existing storage IDs for username `XXXXX`. `-u` should be accepted as a short-form of the `--username` argument.

Storage IDs should be listed in **ascending numeric order** and separated by newlines (`\n`). **Nothing else should be printed**. For example, a namespace with three storage IDs (`100`, `200`, `300`) would display the following:

```sh
100
200
300
```

Passing an optional argument of `--number X` or `-n X` should limit the output to only `X` results. An invalid value for `X` (a non-integer, or a value outside the range 0-1000) should print the message `Number must be an integer between 0 and 1000.`.

At the end of this challenge, all the tests in `test_challenge_1.py` should pass.

### Challenge 2: View existing messages

Create a new file named `storetoise_2.py`. Copy **all** your code from the previous challenge into this file. Write all your code for this challenge in `storetoise_2.py`.

`python3 storetoise_2.py --username XXXXX --storage XXX` should display all the messages for user `XXXXX` under storage ID `XXX`. Short-form arguments for `--username` and `--storage` should also be accepted.

Each message should be displayed on a new line, with its index number. The format should be _exactly_ as in the example below.

```
0) hello
1) hi
2) i must have called a thousand times
```

- If no messages are available, print the message "No messages found for storage ID `XXX`."
- If a non-existent storage ID is requested, print the message "Cannot get messages for a non-existent storage ID."
- If an invalid storage ID (not a 3-digit integer) is requested, print the message "Storage ID must be a three-digit integer."

At the end of this challenge, all the tests in `test_challenge_2.py` should pass.

### Challenge 3: Adding messages

Create a new file named `storetoise_3.py`. Copy **all** your code from the previous challenge into this file. Write all your code for this challenge in `storetoise_3.py`.

`python3 storetoise_3.py --username XXXXX --storage XXX --message XXXXX` should add the given `message` to storage ID `XXX` for the given username. `-u`, `-s`, and `-m` short-form arguments should be accepted.

- If the task is successful, print `Message added to Storage 'XXX' successfully.`
- If a non-existent storage ID is requested, it should be automatically created.
- If an invalid storage ID (not a 3-digit integer) is requested, print the exact message `Storage ID must be a three-digit integer.`
- If the message has over 140 characters, print the exact message `Message must be 140 characters or fewer.`
- If the message has invalid characters (anything except lowercase letters or a space), print the exact message `Message must consist only of lowercase letters and spaces.`
- If there are already 10 messages under the storage ID for that user, print the exact message `Cannot add more than 10 messages to a storage ID.`

At the end of this challenge, all the tests in `test_challenge_3.py` should pass.

### Challenge 4: Deleting storage IDs

Create a new file named `storetoise_4.py`. Copy **all** your code from the previous challenge into this file. Write all your code for this challenge in `storetoise_4.py`.

`python3 storetoise_4.py --username XXXXX --storage XXX --delete` should delete the specified storage ID for the specified username. Short-form arguments should be accepted as `-d`.

- If the task is successful, print the message `Storage ID 'XXX' deleted successfully.` replacing `XXX` with the storage ID that has been deleted
- If an invalid storage ID (not a 3-digit integer) is requested, print the exact message `Storage ID must be a three-digit integer.`
- If a non-existent storage ID is requested, print the exact message `Cannot delete a non-existent storage ID.`

At the end of this challenge, all the tests in `test_challenge_4.py` should pass.

### (Optional) Challenge 5: Extensions

Create a new file named `storetoise_5.py`. Copy **all** your code from the previous challenge into this file.

Implement functionality to handle the following tasks:

- Deleting a single message from a storage ID
- Replacing a single message on a storage ID

There are no tests to guide you with the above tasks; write your own.
