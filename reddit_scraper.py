import praw

REDDIT_SESSION_DATA = {
    'client_id': 'wizRreVm_MG4ZQ',
    'client_secret': 'YWVII1qb3s2ULNUykaBWPec5HLs',
    # password="1guiwevlfo00esyy",
    'user_agent': 'yerrrrr',
    'username': 'kyledrogo'
}

def get_random_post(session_data):

    reddit = praw.Reddit(**session_data)
    post_generator = reddit.subreddit('quotes').random_rising()
    post = next(post_generator)

    return post.title


def main():

    quote = get_random_post(REDDIT_SESSION_DATA)
    print(quote)


if __name__ == '__main__':
    main()
