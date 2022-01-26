# import sys
# sys.path.append(r"C:\\\\Users\\\\HoMinhSang\\\\Documents\\\\DynamicCS\\\\DynamicCS\\\\bin\\\\Release\\\\netstandard2.0")
 
# import clr
# clr.AddReference(r"C:\\\\Users\\\\HoMinhSang\\\\Documents\\\\DynamicCS\\\\DynamicCS\\\\bin\\\\Release\\\\netstandard2.0\\\\DynamicCS.dll")
 
# from DynamicCS import DynamicCalc
 
# calc=DynamicCalc()
 
# print(calc.__class__.__name__)
# # display the name of the class: 'DynamicCalc' 
 
# a=7.5
# b=2.5
 
# res = calc.add(a, b)
# print(a, '+', b, '=', res)
 
# res = calc.sub(a, b)
# print(a, '-', b, '=', res)
 
# raw_input('Press any key to finish...')

import clr #pythonnet
import asyncio
clr.FindAssembly('C:\\Users\\HoMinhSang\\Desktop\\IdteckLibrary\\IdteckLibrary\\bin\\Release\\netstandard2.0\\IdteckLibrary.dll')

clr.AddReference('C:\\Users\\HoMinhSang\\Desktop\\IdteckLibrary\\IdteckLibrary\\bin\\Release\\netstandard2.0\\IdteckLibrary.dll')

from IdteckLibrary import *

async def say_after(delay, what):
    await asyncio.sleep(delay)
    # await Class1.run()
    print(what)

async def main():
    # print('python call K8Cscan c# dll')
    # # x = await Class1.run()
    # # print(x)
    # # print(x.Result)
    # await say_after(2, 'hello')
    await Class1.run()

asyncio.run(main())

# clr.FindAssembly('C:\\Users\\HoMinhSang\\Desktop\\ClassLibrary1\\ClassLibrary1\\bin\\Release\\netstandard2.0\\ClassLibrary1.dll')

# clr.AddReference('C:\\Users\\HoMinhSang\\Desktop\\ClassLibrary1\\ClassLibrary1\\bin\\Release\\netstandard2.0\\ClassLibrary1.dll')

# from ClassLibrary1 import *

# print(Class1.run('192.168.1.1'))


