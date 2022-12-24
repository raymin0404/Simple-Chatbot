from transitions.extensions import GraphMachine
from utils import send_text_message
from linebot.models import MessageAction,URIAction,MessageTemplateAction,CarouselColumn,MessageEvent, TextMessage, TextSendMessage,URIAction,MessageAction
from utils import send_button_message, send_carousel_message, send_image_message, send_text_message,send_text_multiple_message,send_video_message
import random
from utils import LUCK
from utils import BMI
from utils import RPC

main_url = 'https://862a-111-254-3-40.jp.ngrok.io'
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.weight = -1
        self.height = -1
        self.choice = ''
        self.machine = GraphMachine(model=self, **machine_configs)
    def is_going_to_luck(self, event):
        return event.message.text == '今日運勢'
    def is_going_to_BMI_Input_weight(self, event):
        return event.message.text == '計算BMI'
    def is_going_to_BMI_Input_height(self, event):
        text = event.message.text
        try:
            w = int(text)
        except ValueError:
            return False
        self.weight = w
        return True 
    def is_going_to_BMI_result(self, event):
        text = event.message.text
        try:
            w = int(text)
        except ValueError:
            return False
        self.height = w
        return True   
    def back(self, event):
        text = event.message.text
        return text == '返回主選單'
    def is_going_to_RPC_choice(self, event):
        return event.message.text == '玩猜拳'    
    def is_going_to_RPC_result(self, event):
        text = event.message.text

        self.choice = text
        a = ['剪刀', '石頭', '布']
        return self.choice in a
    def on_enter_LUCK(self, event):
        print('state == luck')
        res = LUCK()
        title = '今日運勢為'
        text = f'{res}'
        btn = [
            MessageTemplateAction(
                label = '返回主選單',
                text ='返回主選單'
            ),
        ]
        url = f'{main_url}/meme'
        send_button_message(event.reply_token, title, text, btn, url)
    def on_enter_BMI_Input_weight(self, event):
        reply = event.reply_token
        text = event.message.text
        send_text_message(reply, '請輸入體重(單位: 公斤)')
    def on_enter_BMI_Input_height(self, event):
        reply = event.reply_token
        text = event.message.text
        send_text_message(reply, '請輸入身高(單位: 公分)')
    def on_enter_BMI_result(self, event):
        res = BMI(self.height, self.weight)
        title = '結果'
        text = f'BMI:{res[0]}, {res[1]}'
        btn = [
            MessageTemplateAction(
                label = '返回主選單',
                text ='返回主選單'
            ),
        ]
        url = f'{main_url}/meme'
        send_button_message(event.reply_token, title, text, btn, url)
    def on_enter_RPC_choice(self, event):
        title = '請選擇您要出的拳'
        text = f'請以下任選一種'
        btn = [
            MessageTemplateAction(
                label = '剪刀',
                text ='剪刀'
            ),MessageTemplateAction(
                label = '石頭',
                text ='石頭'
            ),MessageTemplateAction(
                label = '布',
                text ='布'
            ),
        ]
        url = f'{main_url}/meme'
        send_button_message(event.reply_token, title, text, btn, url)
    def on_enter_RPC_result(self, event):
        print('full')
        res = RPC(self.choice)
        title = f'您出的拳是 {self.choice}'
        text = f'對方出的拳是:{res[1]}, 結果: {res[2]}'
        btn = [
            MessageTemplateAction(
                label = '返回主選單',
                text ='返回主選單'
            ),
        ]
        url = f'{main_url}/meme'
        send_button_message(event.reply_token, title, text, btn, url)
    def on_enter_user(self, event):
        self.weight = -1
        self.height = -1
        self.choice = ''
        print('還在user')
        title = '請選擇想要的功能'
        text = '功能如下'
        btn = [
            MessageTemplateAction(
                label = '計算BMI',
                text ='計算BMI'
            ),
            MessageTemplateAction(
                label = '今日運勢',
                text = '今日運勢'
            ),
            MessageTemplateAction(
                label = '玩猜拳',
                text = '玩猜拳'
            ),
            MessageTemplateAction(
                label = 'fsm圖',
                text = 'fsm圖'
            )
        ]
        url = f'{main_url}/meme'
        send_button_message(event.reply_token, title, text, btn, url) 
   



