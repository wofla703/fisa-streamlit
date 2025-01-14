import streamlit as st

#text를 입력하는 검색창 생성
#ani리스트에 있는 글자가 일부라도 들어가면
#이미지 리스트 나오게 
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

search=st.text_input("First name")

for ani in ani_list:
    if search in ani:
        img_idx = ani_list.index(search)

if title == '':
    st.write(img_list[img_idx])

