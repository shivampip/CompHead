from variable_length_code import VLC
import comp_test 

model= VLC()

text= 'aaabbbbbccccccddddee'
#text= 'My name is shivam agrawal. I live at pipariya. currently I am working at L & T Infotech, Mumbai, India'

text= """
Samsung (Hangul: 삼성; Hanja: 三星; Korean pronunciation: [samsʌŋ]; means "tristar" in English) is a South Korean multinational conglomerate headquartered in Samsung Town, Seoul.[1] It comprises numerous affiliated businesses,[1] most of them united under the Samsung brand, and is the largest South Korean chaebol (business conglomerate).

Samsung was founded by Lee Byung-chul in 1938 as a trading company. Over the next three decades, the group diversified into areas including food processing, textiles, insurance, securities, and retail. Samsung entered the electronics industry in the late 1960s and the construction and shipbuilding industries in the mid-1970s; these areas would drive its subsequent growth. Following Lee's death in 1987, Samsung was separated into four business groups – Samsung Group, Shinsegae Group, CJ Group and Hansol Group. Since 1990, Samsung has increasingly globalised its activities and electronics; in particular, its mobile phones and semiconductors have become its most important source of income. As of 2017, Samsung has the 6th highest global brand value.[5]

Notable Samsung industrial affiliates include Samsung Electronics (the world's largest information technology company, consumer electronics maker and chipmaker measured by 2017 revenues),[6][7] Samsung Heavy Industries (the world's 2nd largest shipbuilder measured by 2010 revenues),[8] and Samsung Engineering and Samsung C&T (respectively the world's 13th and 36th largest construction companies).[9] Other notable subsidiaries include Samsung Life Insurance (the world's 14th largest life insurance company),[10] Samsung Everland (operator of Everland Resort, the oldest theme park in South Korea)[11] and Cheil Worldwide (the world's 15th largest advertising agency measured by 2012 revenues).[12][13]

Samsung has a powerful influence on South Korea's economic development, politics, media and culture and has been a major driving force behind the "Miracle on the Han River".[14][15] Its affiliate companies produce around a fifth of South Korea's total exports.[16] Samsung's revenue was equal to 17% of South Korea's $1,082 billion GDP
"""


h_eout= model.encodeHuff(text)
h_dout= model.decodeHuff(h_eout)

comp_test.test(text, h_eout, h_dout)