from requests_html import HTMLSession

time = {"second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800, "month": 2629744, "year": 31556926}

# INFO: Add channels by adding them as an arry of dicts like so:
#       {"name": "Channel Name", "url": "https://www.youtube.com/c/[user]/videos"}
#       The link can be found by navigating to the 'Videos' tab of the channel desired
channels = [
    {"name": "All Gas No Brakes", "url": "https://www.youtube.com/channel/UCtqxG9IrHFU_ID1khGvx9sA/videos"},
    {"name": "Ally Hills", "url": "https://www.youtube.com/c/AllyHills/videos"},
    {"name": "Arpi Park", "url": "https://www.youtube.com/c/ArpiPark/videos"},
    {"name": "BionicPIG", "url": "https://www.youtube.com/c/BionicPIGtv/videos"},
    {"name": "brutalmoose", "url": "https://www.youtube.com/c/brutalmoose/videos"},
    {"name": "Cherdleys", "url": "https://www.youtube.com/c/Cherdleys/videos"},
    {"name": "Chubbyemu", "url": "https://www.youtube.com/c/ChubbyemuGames/videos"},
    {"name": "Corridor Crew", "url": "https://www.youtube.com/c/corridorcrew/videos"},
    {"name": "Danny Gonzalez", "url": "https://www.youtube.com/c/Danny100/videos"},
    {"name": "Drew Gooden", "url": "https://www.youtube.com/c/DrewGooden1/videos"},
    {"name": "Eddy Burback", "url": "https://www.youtube.com/c/EddyBurback/videos"},
    {"name": "How To Drink", "url": "https://www.youtube.com/c/howtodrink/videos"},
    {"name": "Kurtis Conner", "url": "https://www.youtube.com/user/kurtisconner/videos"},
    {"name": "Linus Tech Tips", "url": "https://www.youtube.com/c/LinusTechTips/videos"},
    {"name": "Marques Brownlee", "url": "https://www.youtube.com/c/mkbhd/videos"},
    {"name": "My Analog Journal", "url": "https://www.youtube.com/c/MyAnalogJournal/videos"},
    {"name": "PhilipSoloTV", "url": "https://www.youtube.com/c/PhilipSoloTV/videos"},
    {"name": "Scott Cramer", "url": "https://www.youtube.com/c/ScottsTOL/videos"},
    {"name": "theneedledrop", "url": "https://www.youtube.com/c/theneedledrop/videos"},
    {"name": "Whang!", "url": "https://www.youtube.com/c/WhangWhangWhang/videos"}
    ]

session = HTMLSession()
class Channel:
    """Object defining a channel with videos"""

    def __init__(self, name, url, range_value=1, range_unit="week"):
        self.name = name
        self.page_url = url
        self.range = self.calcRange(range_value, range_unit)
        self.videos = []

    def getVideos(self):
        v = session.get(self.page_url)
        v.html.render()
        posts = v.html.find("a#video-title")
        metadata = v.html.find("div#metadata-line")
        for i, video in enumerate(posts):
            tmp = {}
            ranges = metadata[i].find("span")[1].text.split()
            test = 0
            if ranges[0].isdigit():
                test = self.calcRange(int(ranges[0]), str(ranges[1]))
            else:
                test = self.calcRange(int(ranges[1]), str(ranges[2]))
            if self.range >= test:
                tmp['link'] = "https://youtube.com" + str(video.attrs['href'])
                tmp['title'] = str(video.attrs['title'])
                self.videos.append(tmp)
    
    def calcRange(self, val, unit):
        for u in time.keys():
            if str(unit).find(str(u)) != -1:
                return time[u] * val
        return -1
    
    def outString(self):
        for video in self.videos:
            print(str(video["title"]).upper())
            print(str(video["link"]))
            print("----------")
        print("++++++++++")

# *** CONSTRUCTION IN PROGRESS BELOW ***
#class Video:
#    """Object defining a video"""
#
#    def __init__(self, link, title):
#        self.link = link
#        self.title = title
#    
#    def outString(self):
#        print(str(self.title.upper()))
#        print(str(self.link))
#        print("----------")

# INFO: Modify the channel definition for range filtering
for channel in channels:
    print("{}:".format(channel["name"]))
    print("++++++++++")
    c = Channel(channel["name"], channel["url"], 1, "week")
    c.getVideos()
    c.outString()