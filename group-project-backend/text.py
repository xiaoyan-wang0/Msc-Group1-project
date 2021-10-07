from jsonpath import jsonpath

result = {
    "header": {
        "code": "1",
        "date":"2"
    },
    "body": {
            "isTmpUser": 6,
            "lastActiveTime": {
                "date": 30,
                "timezoneOffset": -480,
            },
        },
        "code": 1
    }
print(result['body']['lastActiveTime']['date'])
result_data = jsonpath(result,'$..date')
print(result_data)