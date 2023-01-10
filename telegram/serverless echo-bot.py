import requests

ur1 = "https://api.teiegram.org/bot(token)/(method)".format(
token = "5560514523:AAFeewGBovYA2JhHCQpZaS0pdPTOPvihjxE",
method = "setwebhook"
#method = "deletewebhook"
#method = "getwebhookinfo"
)

data = ("ur1": "https://functions.yandexcloud.net/d4ejbidg639o03ip1tli")

r = requests.post(ur1, data = data)
print(r.json()(
