from playwright.sync_api import expect

from api.rooms_client import RoomsClient
from pages.rooms_page import RoomsPage


def test_rooms_shown_in_ui_match_api(rooms_client: RoomsClient,rooms_page: RoomsPage):
    response = rooms_client.get_rooms()
    assert response.ok
    api_rooms =response.json()["rooms"]
    
    rooms_page.open()
    
    expect(rooms_page.room_cards).to_have_count(len(api_rooms))
    for room in api_rooms:
        card = rooms_page.room_card(room["type"])
        expect(card).to_contain_text(room["description"])
        expect(card).to_contain_text(f"{room['roomPrice']} per night")