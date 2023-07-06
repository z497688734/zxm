import csv
import json
import time

import requests

# curl 'http://vdts.ivdc.org.cn:8081/cx/api/cxsj/gnsybqsms/list'     -H 'Content-Type: application/json'   -H 'Cookie: JSESSIONID=26ec412b-fd5d-4f46-8137-04b648f71df0; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1'   -H 'Origin: http://vdts.ivdc.org.cn:8081'   -H 'Proxy-Connection: keep-alive'      -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'  --data-raw '{"page":1,"rows":25,"conditionItems":[{"field":"xgxxlx","type":"STRING","operator":"EQUAL","value":"国内兽药说明书数据"}]}'



if __name__ == '__main__':

    headerList = ["itemid","tym","fj"]
    dataList = []
    headers = {
        "Content-Type":"application/json",
        "Cookie":"JSESSIONID=26ec412b-fd5d-4f46-8137-04b648f71df0; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1",
        "Origin":"http://vdts.ivdc.org.cn:8081",
        "Proxy-Connection":"keep-alive",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    pageNum = 1
    while True:
        payload = {
            "page":pageNum,
            "rows":25,
            "conditionItems":[{
                "field":"xgxxlx",
                "type":"STRING",
                "operator":"EQUAL",
                "value":"国内兽药说明书数据"
            }]
        }
        print("now payload:" + json.dumps(payload))

        r = requests.post('http://vdts.ivdc.org.cn:8081/cx/api/cxsj/gnsybqsms/list',data=json.dumps(payload),headers=headers)
        pageNum = pageNum + 1
        try:
            respJson = r.json()
            if len(respJson["rows"]) == 0:
                break
            for vo in respJson["rows"]:
                line = [respJson["rows"][0]["itemid"],respJson["rows"][0]["tym"],respJson["rows"][0]["fj"]]
                dataList.append(line)
        except:
            break

    with open("abc.csv",mode="w",encoding="utf-8-sig",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headerList)
        writer.writerows(dataList)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
