import asyncio
import time

import clr #pythonnet
import asyncio
clr.FindAssembly('C:\\Users\\HoMinhSang\\Desktop\\IdteckLibrary\\IdteckLibrary\\bin\\Release\\netstandard2.0\\IdteckLibrary.dll')

clr.AddReference('C:\\Users\\HoMinhSang\\Desktop\\IdteckLibrary\\IdteckLibrary\\bin\\Release\\netstandard2.0\\IdteckLibrary.dll')

from IdteckLibrary import *


async def main():  
    print("-----", Class1.run().Result.error_message)

asyncio.run(main())
