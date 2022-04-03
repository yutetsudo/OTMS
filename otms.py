import argparse, sys
import secrets

from commands import DevicesCommands
from database.otms_data import OtmsDatabase



OtmsDB = OtmsDatabase()
Devices = DevicesCommands()

class OtmsCli(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Open Train Management System (OTMS) CLI',
            usage='''otms <command> \r\n
init        Generate server token
info        Get OTMS info
            ''')

        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def init(self):
        parser = argparse.ArgumentParser(
            description='Generate server token')
        parser.parse_args(sys.argv[2:])

        print("Generating server token ...")
        token = secrets.token_urlsafe(16)
        OtmsDB.set_token(token)
        print(f"Server token : {token}")

    def info(self):
        parser = argparse.ArgumentParser(
            description='Get OTMS info')
        parser.parse_args(sys.argv[2:])

        info = OtmsDB.get_info()

        print(f"Server Type    : {info['type']}")
        print(f"Server Version : {info['version']}")
        print(f"Server Token   : {info['token']}")

   
if __name__ == '__main__':
    OtmsCli()
