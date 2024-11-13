                      #asyncronus function with async keyword 
import asyncio
import time

async def m():
    print("this is ")
    await asyncio.sleep(3)
    print("asyncronous programming")
    await asyncio.sleep(3)
    print("course")

asyncio.run(m())

                     #asyncio.gather function #
async def m1():
    print("sun1 started ..")
    await asyncio.sleep(1)
    print("fun1 ended...")
    
async def m2():
    print("fun2 started..")
    await asyncio.sleep(1)
    print("fun2 ended...")
    
async def m3():
    print("fun3 started ")
    await asyncio.sleep(1)
    print("fun3 ended ...")

async def main():
    L=await asyncio.gather(
        m1(),
        m2(),
        m3(),
    )
    print("main ended ..")
asyncio.run(main())
