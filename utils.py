import random
import os
from linebot import LineBotApi, WebhookParser
from linebot.models import VideoSendMessage,MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ImageCarouselColumn,CarouselTemplate, ImageCarouselTemplate, URITemplateAction, ButtonsTemplate, MessageTemplateAction, ImageSendMessage
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
def send_text_multiple_message(reply_token, textList):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, textList)
    return "OK"

def send_video_message(reply_token, videoUrl, preUrl):
    line_bot_api = LineBotApi(channel_access_token)
    message = VideoSendMessage(
        original_content_url = videoUrl,
        preview_image_url = preUrl
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"

def send_carousel_message(reply_token, col):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = '*選單*',
        template = CarouselTemplate(columns = col)
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_button_message(reply_token, title, text, btn, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='button template',
        template = ButtonsTemplate(
            title = title,
            text = text,
            thumbnail_image_url = url,
            actions = btn
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url = url,
        preview_image_url = url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"
def BMI(height , weight):
    res = []
    BMI = weight / ((height/100)**2)
    res.append(BMI)
    if BMI < 18.5:
        res.append('您的體重過輕')
    elif BMI >= 18.5 and BMI < 24:
        res.append('您的體重正常')
    elif BMI >= 24 and BMI < 27:
        res.append('您過重了')
    elif BMI >= 27 and BMI < 30:
        res.append('您為輕度肥胖了')
    elif BMI >= 30 and BMI < 35:
        res.append('您為中度肥胖了')
    else:
        res.append('您為重度肥胖了') 
    return res

def LUCK():
    r = random.randint(1 , 10)
    if r > 8:
        return('大吉')
    elif r <= 8 and r > 6:
        return('中吉')
    elif r <= 6 and r > 3:
        return('小吉')
    else:
        return('末吉')
    
def RPC(choice):
    res = []
    a = ['剪刀', '石頭', '布']
    r = random.sample(a, 1)
    res.append(choice)
    res.append(r[0])
    if choice == r[0]:
        res.append('平手')
    elif (choice == a[0] and r[0] == a[1]) or (choice == a[1] and r[0] == a[2]) or (choice == a[2] and r[0] == a[0]):
        res.append('你輸了')
    else:
        res.append('你贏了')
    return res

if __name__ == '__main__':
    print(BMI(175, 60))
    print(LUCK())
    print(RPC('剪刀'))
    print(RPC('石頭'))
    print(RPC('布'))