
import requests
import os
import random
import praw
import os
import pprint

# Access the values from the config dictionary


class Reddit_Scraper:
    
    def __init__(self):
        self.NSFW_SUB_REDDITS = [
            "r/TrueBigDickStories",
            "r/SexStoriesGoneWild",
            "r/eroticliterature",
            "r/BDSMerotica",
            "r/Erotica",
            "r/sexystories",
            "r/sexstories",
            "r/gonewildstories",
            "r/incestsexstories",
        ]


        '''
        Wholesoem subreddits will do in future, let's do one thing at a time.
        '''
        self.wholesome_sub_reddits = {
        # To do: add more sub reddits
        }

    def return_subreddits(self) -> list[str]:
        return self.NSFW_SUB_REDDITS 
    
    def reddit_auth(self):
        config = {}
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        with open("./config.env", 'r') as file:
            for line in file:
                if line.strip():
                    key, value = line.strip().split('=')
                    config[key.strip()] = value.strip()
        
        return praw.Reddit(
            client_id = config['REDDIT_CLIENT_ID'],
            client_secret = config['REDDIT_CLIENT_SECRET'],
            user_agent = config['REDDIT_USER_AGENT'],
            user_name = config['REDDIT_USER_NAME'],
            password = config['REDDIT_PASSWORD']
        )


    def return_written_content(self, sub_reddit:str) -> dict:
        '''
        Should return a dictionary of the form:
        {
            'posts': [
                {
                    'title': 'title of the post',
                    'content': 'content of the post',
                    'author': 'author of the post',
                    'url': 'url of the post',
                    'upvotes': 'number of upvotes of the post',
                },
                ...
            ]
        }
        '''
        reddit = self.reddit_auth()
        content = {
            'posts': []
        }

        if sub_reddit in self.NSFW_SUB_REDDITS:
            sub_reddit = reddit.subreddit(sub_reddit)
            for post in sub_reddit.top(limit=14, time_filter='week'):
                post_data = {
                    'title': post.title,
                    'content': post.selftext,
                    'author': post.author,
                    'url': post.url,
                    'upvotes': post.ups
                }
                content['posts'].append(post_data)
                
        else:
            return { "not_nsfw": "to be implemented"}

        return content


def main():
    reddit_scraper = Reddit_Scraper()
    content = reddit_scraper.return_written_content("r/eroticliterature")
    pprint.pprint(content)

if __name__ == "__main__": 
    main()