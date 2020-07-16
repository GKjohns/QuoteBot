import praw










def main():

    reddit = praw.Reddit(
        client_id="wizRreVm_MG4ZQ",
        client_secret="YWVII1qb3s2ULNUykaBWPec5HLs",
        # password="1guiwevlfo00esyy",
        user_agent="yerrrrr",
        username="kyledrogo"
    )
    print(reddit)

if __name__ == '__main__':
    main()
