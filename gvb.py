import asyncio
import httpx
from datetime import datetime

class GithubViewBot():
    
    def __init__(self):
        self.username               = str(input("[?] Username >> "))
        self.total                  = int(input("[?] Enter Amount Of Views >> "))
        self.amount                 = 0
        self.sucess                 = 0
        self.ratelimit              = 0
        self.client                 = httpx.AsyncClient()
        self.headers                = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}

    async def view(self):
        for x in range(self.total):
            r = await self.client.get(f"https://github{self.username}", headers=self.headers)
            if r.status_code in [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]:
                self.sucess += 1
                self.amount += 1
                _time_ = datetime.now().strftime("%H:%M:%S")
                print(f"[{_time_}] Successfully Viewed {self.username} {self.sucess} Times")

            elif r.status_code in [429]:
                self.ratelimit += 1
                self.amount += 1
                _time_ = datetime.now().strftime("%H:%M:%S")
                print(f"[{_time_}] Rate Limit Exceeded | {self.ratelimit} Times")

        if self.total == self.sucess:
                _time_ = datetime.now().strftime("%H:%M:%S")
                print(f'[{_time_}] Successfully Viewed | Sucess {self.sucess} / Total {self.total} | Errors {self.ratelimit}')
                input('any key to exit')
                exit()

            
if __name__ == "__main__":
    github = GithubViewBot()
    asyncio.run(github.view()).until_complete()
