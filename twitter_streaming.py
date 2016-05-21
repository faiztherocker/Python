#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "3300074881-YhhcBtCUelm0uqiBAG7ImholaSPTPRfCvmmsDsd"
access_token_secret = "k6KJ72AQAqRZbSApfeg7iDEqFzebJ6b0txHZ8VOwapYqf"
consumer_key = "yMYHTw7vZz3mnggQUwaZ35WC0"
consumer_secret = "R9hwdp9UZpKarKIr09FJX7lbtvFAmGFSg0C51bwOSEuXEZ41Yj"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])