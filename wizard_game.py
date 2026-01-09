is_magician = False

is_expert = True

# check if magician AND expert : "you are a master magician"

# check if magician but not expert: "atleast you're getting there"

# if you're not a magician: "You need magic powers"

if is_magician and is_expert:
    print("You're a master magician!")
elif is_magician and not is_expert:  
    print("Atleast you're getting at it")
else:
    print("You need magic powers!")
    