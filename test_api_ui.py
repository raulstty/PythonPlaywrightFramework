from playwright.sync_api import expect

from api.rooms_client import RoomsClient
from pages.rooms_page import RoomsPage


def test_rooms_shown_in_ui_match_api(rooms_client: RoomsClient, rooms_page: RoomsPage):
    api_rooms = rooms_client.get_rooms().json()["rooms"]
    rooms_page.open()
    expect(rooms_page.room_cards.first).to_be_visible()

    for card in rooms_page.room_cards.all():
        room_type = card.locator("h5.card-title").inner_text()
        matches = [room for room in api_rooms if room["type"] == room_type]
        assert matches, f"UI shows '{room_type}' but the API has no such room"
        text = " ".join(card.inner_text().split())
        assert any(
            " ".join(room["description"].split()) in text
            and f"{room['roomPrice']} per night" in text
            for room in matches
        ), f"UI card '{room_type}' does not match the API data"