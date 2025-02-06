from flask import Flask
import asyncio

app = Flask(__name__)

@app.route("/")
def hello_world():
    asyncio.run(main())

    return "<p>Hello, World!</p>"

async def new(time,word):
    
    await asyncio.sleep(time)
    print(word)
async def main():
    async with asyncio.TaskGroup() as tg:
        task3 = tg.create_task(new(3,'3'))
        task4 = tg.create_task(new(10,'4'))

     
if __name__ == '__main__':    
    app.run()