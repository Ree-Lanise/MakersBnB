from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the / page
    page.goto(f"http://{test_web_address}")

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


