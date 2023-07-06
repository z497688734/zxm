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

    headerList = ["bank_code",
                  "bank_card",
                  "create_time",
                  "check_state",
                  "area_code",
                  "real_name",
                  "bank_acct_type",
                  "shop_name",
                  "prov_code",
                  "identity_card",
                  "shop_id",
                  "user_id",
                  "phone",
                  "open_branch_bank",
                  "reserve_phone"
                  ]
    dataList = []
    headers = {
        "Authorization":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0YyIsImNyZWF0ZWQiOjE2ODg2NTU5NjgyODMsImV4cCI6MTY4OTk1MTk2OH0.EliUFAXQoCdQOF1RD-GQi1cNGNr6CSQdAdjlSg_YwSYRuiWvSYyaaf3h5FiI9e_kdu3kELs8iZFxlLynDTSNcg",
        "Origin":"http://gladmin.mysoule.com",
        "Referer":"http://gladmin.mysoule.com/",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    pageNum = 1
    while True:
        url = "http://glslb.sootoken.com.cn/searched-api/api/common/v1/wjs/queryMyData/queryRealUser?shop_id=&shop_name=&userReal_id=&userReal_phone=&userReal_name=&check_state=&pageSize=10&pageNum="+str(pageNum)
        print(url)
        r = requests.post(url,headers=headers)
        pageNum = pageNum + 1
        try:
            if pageNum > 405:
                break
            respJson = r.json()
            print(respJson["data"]["list"])
            print(json.dumps(respJson))
            print(len(respJson["data"]["list"]))
            if len(respJson["data"]["list"]) == 0:
                print("###1")
                break
            for vo in respJson["data"]["list"]:
                line = [
                    getData(vo,"bank_code"),
                    getData(vo,"bank_card"),
                    getData(vo,"create_time"),
                    getData(vo,"check_state"),
                    getData(vo,"area_code"),
                    getData(vo,"real_name"),
                    getData(vo,"bank_acct_type"),
                    getData(vo,"shop_name"),
                    getData(vo,"prov_code"),
                    getData(vo,"identity_card"),
                    getData(vo,"shop_id"),
                    getData(vo,"user_id"),
                    getData(vo,"phone"),
                    getData(vo,"open_branch_bank"),
                    getData(vo,"reserve_phone"),
                ]
                dataList.append(line)
                print(line)
        except:
            traceback.print_exc()
            print("###2")
            break

    with open("abc.csv",mode="w",encoding="utf-8-sig",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headerList)
        writer.writerows(dataList)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
