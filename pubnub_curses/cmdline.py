import sys, pubnub_curses.client

try:
  import argparse

  parser = argparse.ArgumentParser(description='PubNub Console')
  parser.add_argument('-p', '--pubkey', default='demo')
  parser.add_argument('-s', '--subkey', default='demo')
  parser.add_argument('-c', '--channel', default='my_channel')
  parser.add_argument('-o', '--origin', default='pubsub.pubnub.com')
  args = parser.parse_args()

  sys.exit(pubnub.client.main(args.origin, args.pubkey, args.subkey, args.channel))
except KeyboardInterrupt:
  sys.exit(1)