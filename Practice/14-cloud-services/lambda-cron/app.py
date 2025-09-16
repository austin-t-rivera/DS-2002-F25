from datetime import datetime
from chalice import Chalice

app = Chalice(app_name='lambda-cron')
app.debug = True

@app.schedule('cron(* * ? * * *)')
def cron_tab(event):
    # 1. fetch remote file from S3 / file share / API
    # 2. transform data 
    # 3. write it into DB
    print(f"{datetime.now()}: I'm running!")
