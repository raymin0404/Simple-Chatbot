# 前言
這是我第一次做Line-Bot，因此我就做了一些簡單的功能:
1.計算BMI
2.今日運勢
3.玩猜拳
4.fsm圖

# 構想
1.BMI是藉由輸入自身的身高，體重然後來計算BMI值是否為正常值。
2.今日的運勢是由某一款遊戲的啟發來看看今天的運勢好不好，每天起床都可以看看今天的運氣如何。
3.猜拳遊戲就是跟電腦猜拳(電腦會隨機出)，剩下的規則就跟猜拳一樣。

# 使用說明
輸入隨便的英文字母就可以開啟選單
* 計算BMI
* 今日運勢
* 玩猜拳
* fsm圖

# 架構圖
按下計算BMI的按鈕後
1. 輸入體重 -> 輸入自己的體重(以公斤為單位)
2. 輸入身高 -> 輸入自己的身高(以公分為單位)
3. Line-Bot自動回傳您的BMI值
4. 按下回到主選單 -> 回到主選單

按下今日運勢
1. 隨機抽取今日的運勢
2. Line-Bot會回傳給您今天的運勢結果
3. 按下回到主選單 -> 回到主選單

按下玩猜拳的按鈕後
1. 跳出選單 -> 選擇剪刀石頭或布
2. Line-Bot回傳您輸贏的結果
3. 按下回到主選單 -> 回到主選單


# FSM圖片架構
![](https://i.imgur.com/5VRDDuf.png)
# State說明
* User: 隨便輸入字母來跳出選單。
* Luck: 隨機抽取一個運勢看看今天的運氣如何。
* BMI_Input_weight: 輸入體重。
* BMI_Input_height: 輸入身高。
* BMI_reult: 計算BMI後的結果。
* RPC_choice: 跳出分別有剪刀，石頭，布，的選單，電腦會隨機出。
* RPC_result: 看看有沒有猜贏電腦。

# 使用示範
![](https://i.imgur.com/YxHh2JJ.jpg)
![](https://i.imgur.com/yg8aoyF.jpg)
![](https://i.imgur.com/o7JkeLV.jpg)
![](https://i.imgur.com/mHevrUa.jpg)
![](https://i.imgur.com/qb6UNn4.jpg)
![](https://i.imgur.com/imJaE0T.jpg)
![](https://i.imgur.com/bYPrKvU.jpg)




