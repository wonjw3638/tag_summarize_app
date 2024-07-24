import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = 'YOUR_OPENAI_API_KEY'

st.title('OpenAI GPT-3 with Streamlit')
st.write('이 애플리케이션은 OpenAI GPT-3 모델을 사용하여 텍스트 생성을 수행합니다.')

# 사용자 입력 받기
user_input = st.text_area('Prompt를 입력하세요:', '')

if st.button('생성'):
    if user_input:
        # OpenAI API 호출
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=150
        )
        
        # 결과 출력
        st.write('GPT-3의 응답:')
        st.write(response.choices[0].text.strip())
    else:
        st.write('Prompt를 입력해주세요.')
