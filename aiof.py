import argparse
import asyncio
import aiofiles
from aiocsv import AsyncDictReader
import csv
import sys


async def read_file(fileName,columnName):
    async with aiofiles.open(sys.argv[1],mode='r') as file:
         async for row in file:
            print(list(map(lambda x:x[:-1] if x[-1]=='\n' else x,row.split(','))))

async def dict_reader(fileName,columnName):
   async with aiofiles.open(sys.argv[1],mode='r') as file:
         async for row in AsyncDictReader(file,delimiter=','):
            print(row[columnName])
   

async def main(fileName,columnName):
   await read_file(fileName,columnName)
   await dict_reader(fileName,columnName)

if __name__=="__main__":
   parse=argparse.ArgumentParser(description="Processing Files:")
   parse.add_argument('file_name',type=str)
   parse.add_argument('column_name',type=str)
   args=parse.parse_args()
   asyncio.run(main(args.file_name,args.column_name))
   

