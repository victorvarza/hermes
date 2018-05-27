from datetime import datetime

class Logs(object):

    @staticmethod
    def Print(msg):
        try:
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(date_now + '\t\t' + msg)
        except Exception as e:
            print("Exception: %s" % e)