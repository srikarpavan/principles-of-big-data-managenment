# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "1098697660947726338-IIpMm8ydh6xvmUR0DWxlcQsvmKsiAC"
access_token_secret = "aPhq1SGWf5iDUeUdYQYkMudGaVCTVs6PDvzSGDV3fsdtd"
consumer_key = "dLgz2JAk4t9NSuMg2FeVPSr4S"
consumer_secret = "Jvxw63EMTp8aUrkPXdILMT2fdbg0S4ZDOEJWcH50Yl4do2yHxm"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        saveFile = open(r'IPLTweetData.json', 'a')
        saveFile.write(data)
        saveFile.write('\n')
        saveFile.close()

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['RCB','SRH','#RCBvsSRH','Kohli','Umesh','imVkohli','SHetmyer','gurkeeratmann22','#playBold','#SRHvsRCB','VIVOIPL2019','IPL2019','CSK','KKR',
                         '#IPL','#Playoffs','#SRH','#KKR','#KXIP','#PlayMSL','#MSLexpert','#CSKvKXIP','#MIvsKKR','#CSK','#KKRvsMI','#IPL 2019','#contest','#iplcontest',
                         '#SundayMorning' ,'#SundayMotivation' ,'#MI' ,'#FantasyCricket','#cricketinsider','DelhiCapitals','CSK','#IPL12','IPL WINNERS'
                         '#CSKvDC','#Dhoni','#CSK','#WhistlePodu','Yellove','#CSKvMI','#Watson','@ChennaiIPL','@IPL','IndianPremierLeague','Royal Challengers','@RCBTweets','#PlayBold',
                         '@SHetmyer','#12thManTV','@mipaltan','@lionsdenkxip','Kings XI Punjab','#SaddaPunjab','#KXIP','#VIVOIPL',
                         'SunRisers Hyderabad','@SunRisers','#OrangeArmy','#RiseWithUs','#RCBvsSRH'])