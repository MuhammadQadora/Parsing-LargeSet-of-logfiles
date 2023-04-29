#!/bin/python
import concurrent.futures
import time
import os

def getCampaignId():
    with open("TracRx_EDH_CROSSIX_Consumer_DimCampaign_Daily_FULL_20170707.txt","r") as f:
        campainId = []
        for line in f:
            line = line.strip()
            if '"Y"' in line:
                line = line.split('|')
                line = line[0]
                campainId.append(line)
    return campainId

def createDirectory(cmpId):
    i = cmpId.strip('"')
    directory = os.getcwd()
    path = os.path.join(directory,i)
    os.mkdir(path)

def createDirectories():
    cmp = getCampaignId()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(createDirectory, cmp)

def getRecord(filename,recname,cmpId):
    newsletter = []
    for file in os.listdir():
        if recname in file:
            newsletter.append(file)

    directory = os.getcwd()+ "\\" + cmpId.strip('"')
    path = os.path.join(directory,filename)
    with open(path,'w') as add:
        for file in newsletter:
            with open(file) as f:
                for line in f:
                    line = line.rstrip()
                    if cmpId in line:
                        add.write(line+"\n")

if __name__ == '__main__':
    t1 = time.perf_counter()
    createDirectories()
    cmpID = getCampaignId()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for item in cmpID:
            a = executor.submit(getRecord,'UserCenterClicks.txt','NewsletterClicksActivity_', item)
            b = executor.submit(getRecord,'UserMediaAllActivity.txt','UserMediaAllActivity_', item)
            c = executor.submit(getRecord,'UserTrafficCenterActivity.txt','UserTrafficCenterActivity_', item)
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1} seconds")