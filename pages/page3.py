import streamlit as st
import requests

# NASA API 키 (데모키)
API_KEY = st.secrets["DEMO_KEY"]
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

def get_apod():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("API 요청 실패")
        return None

def main():
    st.title("NASA Astronomy Picture of the Day")
    
    data = get_apod()
    if data:
        st.header(data.get("title", ""))
        st.write(data.get("date", ""))
        
        if data.get("media_type") == "image":
            st.image(data.get("url", ""), caption=data.get("title", ""))
        elif data.get("media_type") == "video":
            st.video(data.get("url", ""))
        
        st.write(data.get("explanation", ""))
        
if __name__ == "__main__":
    main()
