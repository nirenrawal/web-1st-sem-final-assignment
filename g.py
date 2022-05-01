
USERS = []
##############################################################

SESSIONS = []
##############################################################

COOKIE_SECRET = "THIS IS SECRET COOKIE KEY"


REGEX_ID = "^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
##############################################################

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
##############################################################

REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
##############################################################

REGEX_USERNAME = '^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$'
##############################################################

TABS = [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id": "home",  "href": "/home"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore",  "href": "/explore"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications",  "href": "/notifications"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages",  "href": "/messages"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks", "href": "/bookmarks"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists",  "href": "/lists"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile", "href": "/profile"},
    {"icon": "fa-solid fa-arrow-right-from-bracket", "title": "Logout", "id": "logout", "href": "/logout"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more",  "href": "/logout"}

]


TRENDS = [
    {"category": "Trending in Denmark", "title": "NFTs", "tweets_counter": "985K"},
    {"category": "Politics", "title": "Russia", "tweets_counter": "40k"},
    {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "50k"},
    {"category": "Music", "title": "Rock", "tweets_counter": "60k"},
    {"category": "News", "title": "Afganistan", "tweets_counter": "844k"},
]


TWEETS = [
    {"id": "1", "src": "3.jpg", "user_first_name": "Elon", "user_last_name": "Musk", "user_name": "elonmusk", "date": "April 25",
     "text": "Since I’ve been asked a lot.Buy stock in several companies that make products & services that *you* believe in.Only sell if you think their products & services are trending worse. Don’t panic when the market does.This will serve you well in the long-term.",  "like": "0"},
    {"id": "2", "src": "6.jpg", "user_first_name": "Barak", "user_last_name": "Obama", "user_name": "barakobama", "date": " April 23",
     "text": "When it comes to climate change, time really is running out. Earth Day is a reminder that if we pledge to do our part and then follow through on those commitments, we can help preserve and protect our planet for future generations."
    },
    {"id": "3", "src": "spaceX.jpeg", "user_first_name": "Space", "user_last_name": "X", "user_name": "spaceX",
     "date": "April 30", "text": "Second burn of the Merlin Vacuum engine complete; <15 minutes until Starlink satellites deploy", "image": "spaceX.jpeg"},
    {"id": "4", "src": "bbc.png", "user_first_name": "BBC", "user_last_name": "NEWS", "user_name": "BBCWORLD", "date": "May 1",
     "text": "A very happy labors to all the working people around the world", "image": "labors day.jpeg"},
]

ITEMS = [
    {"img": "barca.png", "title": "FC barcelona", "user_name": "FCBarcelona"},
    {"img": "bbc.png", "title": "BBC News world", "user_name": "BBCnewswrold"},
    {"img": "madrid.jpeg", "title": "RealMadrid", "user_name": "FCRealMadrid"},
]