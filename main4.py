import csv
import json
import time
import traceback
import requests

# curl 'http://vdts.ivdc.org.cn:8081/cx/api/cxsj/gnsybqsms/list'     -H 'Content-Type: application/json'   -H 'Cookie: JSESSIONID=26ec412b-fd5d-4f46-8137-04b648f71df0; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1'   -H 'Origin: http://vdts.ivdc.org.cn:8081'   -H 'Proxy-Connection: keep-alive'      -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'  --data-raw '{"page":1,"rows":25,"conditionItems":[{"field":"xgxxlx","type":"STRING","operator":"EQUAL","value":"国内兽药说明书数据"}]}'


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
        "authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ6aG91Ym9kaSIsImV4cCI6MTcyMTI3OTA4MX0.YOIgU-HAXfQRYlhjwHz84tYiZhN_Es_qyRU60E0g6haJNGGvI1ck717ePWP7utXJZ6fkHAWFUQaTb3p1o-H0bA",
        "Origin":"https://sync.hangeshenzhou.com",
        "Referer":"https://sync.hangeshenzhou.com/",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    pageNum = 1
    while True:
        url = "https://newtest.hangeshenzhou.com/prod-api/api/dfhMemberUser?size=100&sort=id,desc&page="+str(pageNum)
        print(url)
        r = requests.get(url,headers=headers)
        pageNum = pageNum + 1
        try:
            if pageNum > 3:
                break
            respJson = r.json()
            if len(respJson["content"]) == 0:
                print("###1")
                break
            for vo in respJson["content"]:
                line = [
                    getData(vo,"createTime"),
                    getData(vo, "updateTime"),
                    getData(vo, "id"),
                    getData(vo, "userAlias"),
                    getData(vo, "username"),
                    getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                    # getData(vo, "realName"),
                ]
                dataList.append(line)
                print(line)
        except:
            traceback.print_exc()
            print("###2")
            time.sleep(1)

    with open("abc.csv",mode="w",encoding="utf-8-sig",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headerList)
        writer.writerows(dataList)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
