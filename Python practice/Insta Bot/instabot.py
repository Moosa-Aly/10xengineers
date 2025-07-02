from instabot import Bot
bot = Bot()
bot.login(username="moosa.rauf",password="moosa8080")
bot.follow("sadiesink_")                                                   #follow the account
bot.upload_photo("D:/Downloads/python.jpg",caption = "I love python")      #uploads photo with caption
bot.unfollow("sadiesink_")                                                 #unfollows the account
bot.send_message("I love python", ["saim_arif06","itx_taha_hussain"])      #send the message
followers = bot.get_user_followers("moosa.rauf")                           #print the followers list
for follower in followers:
    print(bot.get_user_info(follower))
followings = bot.get_user_following("moosa.rauf")                          #print the following list
for following in followings:
    print(bot.get_user_info(following))




