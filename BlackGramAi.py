import instaloader

username = 'Put your username inside this quote'
password = 'Put your password inside this quote'

L = instaloader.Instaloader()
# Login or load session

L.login(username, password)#this should be your own username and #password
profile = instaloader.Profile.from_username(L.context, username)

# in the line above, replace the username field by the username of 
#the person you want this bot to work for. If you want to find the 
#list of persons who do not follow you back, replace username by 
#your own username. If you want for someone else, use their username.

main_followers = profile.followers
follower_list = [] #people who follow you
for person in profile.get_followers():
  user_id = person.userid
  follower_list.append(person.username)

main_followees = profile.followees
followee_list = [] #people whom you follow
for person in profile.get_followees():
  user_id = person.userid
  followee_list.append(person.username)

req = []
for element in followee_list:
  if element not in follower_list:
req.append(element)

print(sorted(req))
