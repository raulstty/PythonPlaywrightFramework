
from api.posts_client import PostsClient


def test_get_post(posts_client: PostsClient):
    response = posts_client.get_post(1)
    assert response.status == 200
    body = response.json()
    assert body["id"] == 1
    assert body["userId"] == 1
    
def test_list_posts_filtered_by_user(posts_client: PostsClient):
    response = posts_client.list_posts(user_id=1)
    assert response.ok
    posts = response.json()
    assert len(posts)>0
    assert all(post["userId"] == 1 for post in posts)
    
def test_create_post(posts_client: PostsClient):
    payload = {"title":"foo","body":"bar","userId":1}
    response = posts_client.create_post(payload)
    assert response.status == 201
    body = response.json()
    assert body["title"] == "foo"
    assert "id" in body
    
def test_nagative_condition(posts_client : PostsClient):
    response = posts_client.get_post(9999)
    assert response.status == 404