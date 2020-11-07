from datetime import datetime

def botlog(text):
    print('%s - %s'  % (str(datetime.now()), text))