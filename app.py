import os
import sys
from flask import Flask,send_from_directory, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageTemplateAction,CarouselColumn,MessageEvent, TextMessage, TextSendMessage,URIAction,MessageAction
from utils import send_button_message, send_carousel_message, send_image_message, send_text_message,send_text_multiple_message,send_video_message
from fsm import TocMachine
from utils import send_text_message
os.environ['PATH'] +=os.pathsep +r'./windows_10_msbuild_Release_graphviz-7.0.5-win32/Graphviz/bin'

load_dotenv()
hash_map = dict()

main_url = 'https://simple-chatbot.onrender.com'
# main_url = 'https://d029-111-254-3-40.jp.ngrok.io'
app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/meme", methods=["GET"])
def meme():
    filename = '1671863442214.png'
    return send_from_directory('img',filename, as_attachment=True)
@app.route("/callback", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    import json

    data = json.loads(body)

    userId = data['events'][0]['source']['userId']

    machine = hash_map.setdefault(userId,TocMachine(
        states=["user", "LUCK", "BMI_Input_weight","BMI_Input_height","BMI_result","RPC_choice","RPC_result"],
        transitions=[
            #Intialize
            {
                "trigger": "advance",
                "source": "user",
                "dest": "LUCK",
                "conditions": "is_going_to_luck",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "BMI_Input_weight",
                "conditions": "is_going_to_BMI_Input_weight",
            },
            {
                "trigger": "advance",
                "source": "BMI_Input_weight",
                "dest": "BMI_Input_height",
                "conditions": "is_going_to_BMI_Input_height",
            },
            {
                "trigger": "advance",
                "source": "BMI_Input_height",
                "dest": "BMI_result",
                "conditions": "is_going_to_BMI_result",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "RPC_choice",
                "conditions": "is_going_to_RPC_choice",
            },
            {
                "trigger": "advance",
                "source": "RPC_choice",
                "dest": "RPC_result",
                "conditions": "is_going_to_RPC_result",
            },
            {
                "trigger": "advance", 
                "source": ["LUCK", "BMI_Input_weight","BMI_Input_height","BMI_result","RPC_choice","RPC_result"], 
                "dest": "user",
                "conditions": "back",
            }
        ],
        initial = "user",
        auto_transitions = False,
        show_conditions = True,
    ))

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            # send_text_message(event.reply_token, "Not Entering any State")
            if event.message.text == 'fsm???':
                send_image_message(event.reply_token, f'{main_url}/show-fsm')
            else:
                print('??????user')
                title = '????????????????????????'
                text = '????????????'
                btn = [
                    MessageTemplateAction(
                        label = '??????BMI',
                        text ='??????BMI'
                    ),
                    MessageTemplateAction(
                        label = '????????????',
                        text = '????????????'
                    ),
                    MessageTemplateAction(
                        label = '?????????',
                        text = '?????????'
                    ),
                    MessageTemplateAction(
                        label = 'fsm???',
                        text = 'fsm???'
                    )
                ]
                url = f'{main_url}/meme'
                send_button_message(event.reply_token, title, text, btn, url)

    return "OK"


@app.route('/show-fsm', methods=["GET"])
def show_fsm():
    # machine = hash_map.get(userID)
    # machine.get_graph().draw(f"img/{userID}.png", prog="dot", format="png")
    return send_from_directory('img',f'default.png', as_attachment=True)




if __name__ == "__main__":
    from gevent import pywsgi  
    port = os.environ.get("PORT", 8000)

    server = pywsgi.WSGIServer(('0.0.0.0',int(port)),app)

    server.serve_forever()
    # app.run(host="0.0.0.0", port=port, debug=True)