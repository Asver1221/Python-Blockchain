import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-663ba8fc-918e-11ec-82a0-02d5075437d9'
pnconfig.publish_key = 'pub-c-9e78d581-4dc1-4d4a-ba15-8aa9736cdcf9'

TEST_CHANNEL = 'TEST_CHANNEL'


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')


class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

def main():
    pubsub = PubSub()
    
    # In some cases publishing can be executed before subscribing to the TEST_CHANNEL, sleep(1) prevent from publishing before subscribing
    time.sleep(1)
    pubsub.publish(TEST_CHANNEL, { 'foo': 'bar'})
    

if __name__ == '__main__':
    main()
