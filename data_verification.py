#-*- coding: utf-8 -*-

import json
import datetime

test_data = {
    "ad_network": "FOO",
    "date": "2019-06-05",
    "app_name": "LINETV",
    "unit_id": "55665201314",
    "request": "100", 
    "revenue": 0.00365325, 
    "imp": "23"
}

# 假設日期格式都遇設為YYYY-mm-dd與revenue為float

data_type = {
    "ad_network": str,
    "date": datetime.date,
    "app_name": str,
    "unit_id": str,
    "request": str, 
    "revenue": float, 
    "imp": str
}


def app_data_verification(app_data):

    # 檢查是否有遺漏值
    for key in data_type.keys():
        if key not in app_data.keys():
            # 如果是缺少欄位就標記為False
            app_data["verification"] = 0
            return app_data

    # 檢查型態是否正確與值是否為空或是有遺漏
    for key,value in app_data.items():
        if data_type[key] == datetime.date:
            # 如果日期欄位無法正確轉換 就標記為False
            try:
                date_ = datetime.datetime.strptime(value, "%Y-%m-%d")
            except:
                app_data["verification"] = 0
                return app_data
        else:
            if not isinstance(value,data_type[key]):
                app_data["verification"] = 0
                return app_data

        # 值為None或是為空值
        if value is None or value == "":
            app_data["verification"] = 0
            return app_data


    # 驗證都沒問題就標記為1
    app_data["verification"] = 1
    return app_data


if __name__ == '__main__':

    print(app_data_verification(test_data))