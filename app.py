import streamlit as st
import random

places = ["水がある場所","1駅先","行きたかった場所","懐かしい場所","観覧車が見える場所"]
actions = ["おしゃれな飲み物を飲む","生き物を探す","ぶれた写真を撮る","3回回る","おいしいパンを食べる","レトロな喫茶に行く"]

if st.button("ランダム単語を表示"):
    st.write(f"「{random.choice(places)}」で「{random.choice(actions)}」")
