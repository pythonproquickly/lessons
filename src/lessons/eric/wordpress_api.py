# pip install requests

import requests
import base64

wordpress_user = "username"
wordpress_password = "xxxxxxxx"
wordpress_credentials = wordpress_user + ":" + wordpress_password
wordpress_token = base64.b64encode(wordpress_credentials.encode())
wordpress_header = {"Authorization": "Basic " + wordpress_token.decode("utf-8")}
API_URL = "https://xxxx.com/wp-json/wp/v2/posts"


def read_wordpress_posts():
    response = requests.get(API_URL)
    return response.json()


def create_wordpress_post(data):
    response = requests.post(API_URL, headers=wordpress_header, json=data)
    return response


def main():
    posts = read_wordpress_posts()
    print(posts[:79])

    data = {
        "title": "Test wordpress py api",
        "status": "publish",
        "slug": "example-post",
        "content": "this is the post I am creating",
    }
    post = create_wordpress_post(data)
    print(post)


if __name__ == "__main__":
    main()