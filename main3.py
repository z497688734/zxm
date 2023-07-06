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
    headers = {
        "Cookie":"PHPSESSID=jtnuoi1a346i7i60o80fepqnv6; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1",
        "Host":"www.jiumeifu.cc",
        "Proxy-Connection":"keep-alive",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    pageNum = 1
    while True:
        url = "http://www.jiumeifu.cc/admin.php/member/index?search_type=&keyword=&state=0&level_id=0&page="+str(pageNum)
        r = requests.post(url,headers=headers)
        try:
            with open("file/"+str(pageNum)+".html", 'w',encoding='utf-8') as f:
                f.write(r.text)
                f.close()
            if pageNum > 844:
                break
        except:
            traceback.print_exc()
            print("###2")
            break
        pageNum = pageNum + 1




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
