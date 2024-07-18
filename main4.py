import csv
import json
import time
import traceback
import requests


def getData(dict,key):
    if key in dict:
        return dict[key]
    return ""

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
        "authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ6aG91Ym9kaSIsImV4cCI6MTcyMTMyMzM3N30.OxLOd6fYPouY16M0o9-0Y2-CGA4308LeS371UfBVv6SHVywX4RpTFjBOlPgLPxpsCe01gG4ktlOVD_HzgAYQDQ",
        "Origin":"https://sync.hangeshenzhou.com",
        "Referer":"https://sync.hangeshenzhou.com/",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    pageNum = 1
    maxPageNum = 5135
    while True:
        url = "https://newtest.hangeshenzhou.com/prod-api/api/dfhMemberUser?size=100&sort=id,desc&page="+str(pageNum)
        r = requests.get(url,headers=headers)
        try:
            respJson = r.json()
            print(url,len(respJson["content"]))
            if pageNum > maxPageNum:
                print("hit maxPageNUm")
                break
            pageNum = pageNum + 1
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
        except:
            traceback.print_exc()
            print("except",pageNum)
            time.sleep(1)

    with open("abc.csv",mode="w",encoding="utf-8-sig",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headerList)
        writer.writerows(dataList)