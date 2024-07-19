import csv
import json
import time
import traceback
import requests


def getData(dict, key):
    if key in dict:
        return dict[key]
    return ""

def saveFile(fileName,dataList):
    with open(fileName, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headerList)
        writer.writerows(dataList)

if __name__ == '__main__':

    headerList = [
           "id"
            "joinCycle"
            "userStatus"
            "levels"
            "certificationTime"
            "directPush"
            "createTime"
            "createName"
            "updateTime"
            "updateName"
            "indirectPush"
            "branchNumber"
            "branchName"
            "specialApprovalTime"
            "specialApprovalUsername"
            "certificationAnewTime"
            "certificationInfo"
            "userId"
            "userAlias"
            "name"
            "realName"
            "nation"
            "gender"
            "bom"
            "idExpire"
            "idCard"
            "address"
            "faceImage"
            "backImage"
            "status"
            "createUserId"
            "updateUserId"
            "requestId"
            "ctype"


    ]
    dataList = []
    headers = {
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ6aG91Ym9kaSIsImV4cCI6MTcyMTM2Njc1Mn0.5p0nAFDlZOk5T6hPx6F9EXrYzO4DfC_Pe2T3uWVd5iVWpFhNbFPAKWl8bx088HbiJL-_ajm-eyu0DMOSjnwzYA",
        "Origin": "https://sync.hangeshenzhou.com",
        "Referer": "https://sync.hangeshenzhou.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    pageNum = 0
    maxPageNum = 2280
    fileName = "dz.csv"
    while True:
        try:
            url = "https://newtest.hangeshenzhou.com/prod-api/api/dfhUserAuthentication?&size=100&sort=id%2Cdesc&page=" + str(pageNum)
            r = requests.get(url, headers=headers)
            respJson = r.json()
            content = respJson.get('content')
            if content is  None:
                print("###content nil",respJson)
                break
            print(url, len(content))
            if pageNum > maxPageNum:
                print("hit maxPageNUm")
                break
            for vo in content:
                line = [
                getData(vo, "id"),
                getData(vo,"joinCycle"),
                getData(vo,"userStatus"),
                getData(vo,"levels"),
                getData(vo,"certificationTime"),
                getData(vo,"directPush"),
                getData(vo,"createTime"),
                getData(vo,"createName"),
                getData(vo,"updateTime"),
                getData(vo,"updateName"),
                getData(vo,"indirectPush"),
                getData(vo,"branchNumber"),
                getData(vo,"branchName"),
                getData(vo,"specialApprovalTime"),
                getData(vo,"specialApprovalUsername"),
                getData(vo,"certificationAnewTime"),
                getData(vo,"certificationInfo"),
                getData(vo,"userId"),
                getData(vo,"userAlias"),
                getData(vo,"name"),
                getData(vo,"realName"),
                getData(vo,"nation"),
                getData(vo,"gender"),
                getData(vo,"bom"),
                getData(vo,"idExpire"),
                getData(vo,"idCard"),
                getData(vo,"address"),
                getData(vo,"faceImage"),
                getData(vo,"backImage"),
                getData(vo,"status"),
                getData(vo,"createUserId"),
                getData(vo,"updateUserId"),
                getData(vo,"requestId"),
                getData(vo,"ctype"),

                ]
                dataList.append(line)
            pageNum = pageNum + 1
        except:
            traceback.print_exc()
            print("except", pageNum)
            time.sleep(1)
            saveFile(fileName, dataList)

    saveFile(fileName,dataList)