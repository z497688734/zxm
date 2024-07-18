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
        "orderId"
        "userId"
        "shareId"
        "storageId"
        "realName"
        "userPhone"
        "ticketId"
        "userAddress"
        "userTypeDesc"
        "userStageDesc"
        "userStage"
        "userType"
        "userXxdz"
        "province"
        "cartId"
        "cateName"
        "totalNum"
        "totalAmount"
        "actualAmount"
        "totalPostage"
        "postCode"
        "payAmount"
        "voucherPrice"
        "payExchangeVoucher"
        "exchangeVoucher"
        "payStatus"
        "payTime"
        "payType"
        "payTypeName"
        "payChannel"
        "regionId"
        "createTime"
        "updateTime"
        "finishTime"
        "updateName"
        "isExchange"
        "status"
        "statusOld"
        "isPavilionOwner"
        "statusName"
        "refundReasonWapImg"
        "refundReasonWapExplain"
        "refundReasonTime"
        "refundReasonWap"
        "refundReason"
        "refundPrice"
        "refundPv"
        "deliverySn"
        "deliveryName"
        "deliveryType"
        "deliveryId"
        "deliveryAddressId"
        "mark"
        "isDel"
        "remark"
        "cost"
        "shippingType"
        "isChannel"
        "isRemind"
        "isSystemDel"
        "isTeamCluster"
        "totalPv"
        "ppv"
        "source"
        "payPv"
        "company"
        "companyName"
        "companyRemark"
        "buyType"
        "isRefund"
        "buyUser"
        "personType"
        "firstOrder"
        "invoice"
        "adminMark"
        "mergeId"
        "isMerge"
        "orderType"
        "isTear"
        "isTeam"
        "repayPpv"
        "repayVoucher"
        "repayPv"
        "buyUserRank"
        "buyUserStage"
        "buyUserNum"
        "buyUserReal"
        "isStop"
        "isPromo"
        "storageCode"
        "storageName"
        "isSupplementGift"
        "isTianxuan"
        "isContainGift"
        "isRebate"
        "saleDate"
        "isVoucher"
        "successTime"
        "isRepay"
        "needPayVoucher"
        "giftsPrice"
        "lotteryNum"
        "lotteryNumPv"
        "surplusLotteryNum"
        "activityId"
        "ticketsMax"
        "userAlias"
        "buyUserAlias"
        "buyRealName"
        "buyUserTypeDesc"
        "buyUserStageDesc"
        "createName"
        "specialOrderType"

    ]
    dataList = []
    headers = {
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ6aG91Ym9kaSIsImV4cCI6MTcyMTM0MDI5NH0.H_F8f5VMKjMNpOTbQxf7t56Q98_bG_GQDf5bfvS3RVCS6IHxkrFJKUlsK0MtX2yNL2Tgj6bZ6p8yJ4nKtVRd8w",
        "Origin": "https://sync.hangeshenzhou.com",
        "Referer": "https://sync.hangeshenzhou.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }
    pageNum = 1840
    maxPageNum = 1846
    fileName = "order.csv"
    while True:
        try:
            url = "https://newtest.hangeshenzhou.com/prod-api/api/productOrder?orderStatus=&createTimes=2024-01-01 00:00:00&createTimes=2024-07-19 23:59:59&size=100&sort=id,desc&page=" + str(pageNum)
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
                    getData(vo, "orderId"),
                    getData(vo, "userId"),
                    getData(vo, "shareId"),
                    getData(vo, "storageId"),
                    getData(vo, "realName"),
                    getData(vo, "userPhone"),
                    getData(vo, "ticketId"),
                    getData(vo, "userAddress"),
                    getData(vo, "userTypeDesc"),
                    getData(vo, "userStageDesc"),
                    getData(vo, "userStage"),
                    getData(vo, "userType"),
                    getData(vo, "userXxdz"),
                    getData(vo, "province"),
                    getData(vo, "cartId"),
                    getData(vo, "cateName"),
                    getData(vo, "totalNum"),
                    getData(vo, "totalAmount"),
                    getData(vo, "actualAmount"),
                    getData(vo, "totalPostage"),
                    getData(vo, "postCode"),
                    getData(vo, "payAmount"),
                    getData(vo, "voucherPrice"),
                    getData(vo, "payExchangeVoucher"),
                    getData(vo, "exchangeVoucher"),
                    getData(vo, "payStatus"),
                    getData(vo, "payTime"),
                    getData(vo, "payType"),
                    getData(vo, "payTypeName"),
                    getData(vo, "payChannel"),
                    getData(vo, "regionId"),
                    getData(vo, "createTime"),
                    getData(vo, "updateTime"),
                    getData(vo, "finishTime"),
                    getData(vo, "updateName"),
                    getData(vo, "isExchange"),
                    getData(vo, "status"),
                    getData(vo, "statusOld"),
                    getData(vo, "isPavilionOwner"),
                    getData(vo, "statusName"),
                    getData(vo, "refundReasonWapImg"),
                    getData(vo, "refundReasonWapExplain"),
                    getData(vo, "refundReasonTime"),
                    getData(vo, "refundReasonWap"),
                    getData(vo, "refundReason"),
                    getData(vo, "refundPrice"),
                    getData(vo, "refundPv"),
                    getData(vo, "deliverySn"),
                    getData(vo, "deliveryName"),
                    getData(vo, "deliveryType"),
                    getData(vo, "deliveryId"),
                    getData(vo, "deliveryAddressId"),
                    getData(vo, "mark"),
                    getData(vo, "isDel"),
                    getData(vo, "remark"),
                    getData(vo, "cost"),
                    getData(vo, "shippingType"),
                    getData(vo, "isChannel"),
                    getData(vo, "isRemind"),
                    getData(vo, "isSystemDel"),
                    getData(vo, "isTeamCluster"),
                    getData(vo, "totalPv"),
                    getData(vo, "ppv"),
                    getData(vo, "source"),
                    getData(vo, "payPv"),
                    getData(vo, "company"),
                    getData(vo, "companyName"),
                    getData(vo, "companyRemark"),
                    getData(vo, "buyType"),
                    getData(vo, "isRefund"),
                    getData(vo, "buyUser"),
                    getData(vo, "personType"),
                    getData(vo, "firstOrder"),
                    getData(vo, "invoice"),
                    getData(vo, "adminMark"),
                    getData(vo, "mergeId"),
                    getData(vo, "isMerge"),
                    getData(vo, "orderType"),
                    getData(vo, "isTear"),
                    getData(vo, "isTeam"),
                    getData(vo, "repayPpv"),
                    getData(vo, "repayVoucher"),
                    getData(vo, "repayPv"),
                    getData(vo, "buyUserRank"),
                    getData(vo, "buyUserStage"),
                    getData(vo, "buyUserNum"),
                    getData(vo, "buyUserReal"),
                    getData(vo, "isStop"),
                    getData(vo, "isPromo"),
                    getData(vo, "storageCode"),
                    getData(vo, "storageName"),
                    getData(vo, "isSupplementGift"),
                    getData(vo, "isTianxuan"),
                    getData(vo, "isContainGift"),
                    getData(vo, "isRebate"),
                    getData(vo, "saleDate"),
                    getData(vo, "isVoucher"),
                    getData(vo, "successTime"),
                    getData(vo, "isRepay"),
                    getData(vo, "needPayVoucher"),
                    getData(vo, "giftsPrice"),
                    getData(vo, "lotteryNum"),
                    getData(vo, "lotteryNumPv"),
                    getData(vo, "surplusLotteryNum"),
                    getData(vo, "activityId"),
                    getData(vo, "ticketsMax"),
                    getData(vo, "userAlias"),
                    getData(vo, "buyUserAlias"),
                    getData(vo, "buyRealName"),
                    getData(vo, "buyUserTypeDesc"),
                    getData(vo, "buyUserStageDesc"),
                    getData(vo, "createName"),
                    getData(vo, "specialOrderType"),

                ]
                dataList.append(line)
            pageNum = pageNum + 1
        except:
            traceback.print_exc()
            print("except", pageNum)
            time.sleep(1)
            saveFile(fileName, dataList)

    saveFile(fileName,dataList)