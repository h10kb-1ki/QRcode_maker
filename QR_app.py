import streamlit as st 
import qrcode
from PIL import Image

st.title('QRコード自動生成アプリ')

txt = st.text_input('QRコード化したいテキストを入力してください:')

if st.button('QRコード生成'):
    _img = qrcode.make(txt)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
