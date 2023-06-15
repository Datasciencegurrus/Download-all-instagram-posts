from instaloader import Instaloader, Profile

def download_posts_and_videos(username):
    L = Instaloader()
    profile = Profile.from_username(L.context, username)
    for post in profile.get_posts():
        if post.is_video:
            filename = f"{post.date_utc.strftime('%Y-%m-%d %H-%M-%S')}.mp4"
            L.download_post(post, target=filename)
            print(f"Downloaded: {filename}")
        else:
            filename = f"{post.date_utc.strftime('%Y-%m-%d %H-%M-%S')}.jpg"
            L.download_pic(post, filename=filename, target='.')
            print(f"Downloaded: {filename}")

username = ""  #enter username of target account
download_posts_and_videos(username)
