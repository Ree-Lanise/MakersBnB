from playwright.sync_api import Page, expect
from flask import Flask, request, render_template, redirect, session
from lib.user_repository import UserRepository 
from app import app
# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the / page
    page.goto(f"http://{test_web_address}/")

    # We look at the <p> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "Makers BnB"
    expect(h1_tag).to_have_text("Makers BnB")

"""
We can render the places page
"""
def test_get_places(page, test_web_address):
    # We load a virtual browser and navigate to the /places page
    page.goto(f"http://{test_web_address}/places")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "Book a Place"
    expect(h1_tag).to_have_text("Book a Place")

"""
We can render the new place page
"""
def test_get_add_new_place(page, test_web_address):
    # We load a virtual browser and navigate to the /places page
    page.goto(f"http://{test_web_address}/places/new")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "List a new Place"
    expect(h1_tag).to_have_text("List a new Place")



'''
Test we can view spaces
'''

def test_get_view_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/places")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Book a Place")




""" we can render the login page """

def test_get_login(page, test_web_address):
    # we go to the correct page within a virtual browser
    page.goto(f"http://{test_web_address}/login")

    # We check the <h1> tag on that page
    h2_tag = page.locator("h2")

    # we assert that we expect it to say "login"
    expect(h2_tag).to_have_text("Login")

"""We have username and password headers"""

def test_input_user_pass(page, test_web_address):
    # we go to the login page
    page.goto(f"http://{test_web_address}/login")

    # we check the label headers 
    label_tags = page.locator("label")

    # we asser that we expect it to say username and password
    expect(label_tags).to_have_text(["Username *", "Password *", "Email *"])

"""Tests the login button redirects us to the main index page"""

def test_when_we_click_login_button(page, test_web_address):
    page.set_default_timeout(1000)
    # we go to login page
    page.goto(f"http://{test_web_address}/login")
    # we fill in fields and we click the button
    page.fill("input[name=user]", 'User')
    page.fill("input[name=pass]", 'Password')
    page.fill("input[name=email]", 'User@email.com')
    page.click("input[type=submit][value='Login']")
    # we check url and assert we have been redirected
    assert page.url == f"http://{test_web_address}/"

"""tests that we have to have input to login-otherwise throws an error"""
def test_we_have_details_before_login(page, test_web_address):
    page.set_default_timeout(1000)
    # we go to the login page 
    page.goto(f"http://{test_web_address}/login")
    # we click login before entering details
    page.click("input[type=submit][value='Login']")
    # we check the class t-error
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("Login Invalid - Please Try Again")

"""
tests that if you login as an existing user, it logs in that existing user 
and doesn't create a new user.
"""
def tests_login_as_existing_user(page, test_web_address, db_connection):
    db_connection.seed('seeds/Users.sql')
    repo = UserRepository(db_connection)
    
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=user]", 'Maria')
    page.fill("input[name=pass]", 'Password')
    page.fill("input[name=email]", 'maria@gmail.com')
    page.click("input[type=submit][value='Login']")
    
    assert not repo.find(6)
    
        

