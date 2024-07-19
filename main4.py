import csv
import json
import time
import traceback
import requests


def getData(dict,key):
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
                "createTime",
                "updateTime",
                "id",
                "userAlias",
                "username",
                "realName",
                "status",
                "statusDesc",
                "branch",
                "branchName",
                "introducerId",
                "introducerAlias",
                "introducerName",
                "parentId",
                "parentAlias",
                "parentName",
                "userType",
                "userTypeDesc",
                "userStage",
                "userStageDesc",
                "addres",
                "teamId",
                "teamUserId",
                "teamUserAlias",
                "teamUserName",
                "uniqueMobile",
                "idCard",
                "familyAddress",
                "familyDetailedAddress",
                "contactAreaAddress",
                "password",
                "passwordSecret",
                "passwordBase",
                "passwordSecretBase",
                "cTypeDesc",
                 ]
    dataList = []
    headers = {
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ6aG91Ym9kaSIsImV4cCI6MTcyMTM0MDI5NH0.H_F8f5VMKjMNpOTbQxf7t56Q98_bG_GQDf5bfvS3RVCS6IHxkrFJKUlsK0MtX2yNL2Tgj6bZ6p8yJ4nKtVRd8w",
        "Origin":"https://sync.hangeshenzhou.com",
        "Referer":"https://sync.hangeshenzhou.com/",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    pageNum = 915
    maxPageNum = 5135
    fileName = "huiyuan.csv"
    while True:
        try:
            url = "https://newtest.hangeshenzhou.com/prod-api/api/dfhMemberUser?size=100&sort=id,desc&page=" + str(pageNum)
            r = requests.get(url, headers=headers)
            if pageNum == 3515:
                break
            respJson = r.json()
            content = respJson.get('content')
            if content is  None:
                print("###content nil",respJson)
                break
            print(url,len(respJson["content"]))
            if pageNum > maxPageNum:
                print("hit maxPageNUm")
                break
            for vo in respJson["content"]:
                line = [
                    getData(vo,"createTime"),
                    getData(vo, "updateTime"),
                    getData(vo, "id"),
                    getData(vo, "userAlias"),
                    getData(vo, "username"),
                    getData(vo, "realName"),
                    getData(vo, "status"),
                     getData(vo, "statusDesc"),
                    getData(vo, "branch"),
                     getData(vo, "branchName"),
                     getData(vo, "introducerId"),
                     getData(vo, "introducerAlias"),
                     getData(vo, "introducerName"),
                     getData(vo, "parentId"),
                     getData(vo, "parentAlias"),
                     getData(vo, "parentName"),
                     getData(vo, "userType"),
                     getData(vo, "userTypeDesc"),
                     getData(vo, "userStage"),
                     getData(vo, "userStageDesc"),
                     getData(vo, "addres"),
                     getData(vo, "teamId"),
                     getData(vo, "teamUserId"),
                     getData(vo, "teamUserAlias"),
                     getData(vo, "teamUserName"),
                     getData(vo, "uniqueMobile"),
                     getData(vo, "idCard"),
                     getData(vo, "familyAddress"),
                     getData(vo, "familyDetailedAddress"),
                     getData(vo, "contactAreaAddress"),
                     getData(vo, "password"),
                     getData(vo, "passwordSecret"),
                     getData(vo, "passwordBase"),
                     getData(vo, "passwordSecretBase"),
                     getData(vo, "cTypeDesc"),
                ]
                dataList.append(line)
            pageNum = pageNum + 1
        except:
            traceback.print_exc()
            print("except",pageNum)
            time.sleep(1)
            saveFile("huiyuan.csv",dataList)

    saveFile("huiyuan.csv", dataList)