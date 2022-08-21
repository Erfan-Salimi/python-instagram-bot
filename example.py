from main import InstagramBot
from random import choice


bot = InstagramBot()
sample_comments = ["greate!", "Thanks", "👌👌", "Well🙏", "😍😍"]

bot.login("s_ali_mi1386", 'ali0250902109')
posts = bot.search_tag("python", 5)
for post in posts:
    bot.like_post(post)
    bot.comment(post, comment=choice(sample_comments))
    author = bot.get_post_writer(post)
    for p in bot.get_user_posts(author, 2):
        bot.like_post(p)
        bot.comment(p, comment=choice(sample_comments))
    bot.follow(author)

bot.end()