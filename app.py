import streamlit as st

# పేజ్ టైటిల్ మరియు డిజైన్
st.set_page_config(page_title="Detector Pro", page_icon="🛡️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🛡️ DETECTOR PRO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Online Fraud & Scam Identifier</h3>", unsafe_allow_html=True)
st.write("---")

# యూజర్ నుండి ఇన్పుట్ తీసుకోవడం
user_input = st.text_area("అనుమానాస్పద మెసేజ్, లింక్ లేదా ఫోన్ నంబర్‌ను ఇక్కడ నమోదు చేయండి:", placeholder="ఉదాహరణకు: You won lottery click here...")

if st.button("CHECK FOR FRAUD", use_container_width=True):
    if not user_input.strip():
        st.warning("దయచేసి ఏదെങ്കിലും టెక్స్ట్ లేదా లింక్ ఎంటర్ చేయండి!")
    else:
        # ఫ్రాడ్ కీవర్డ్స్ చెకింగ్ లాజిక్
        text = user_input.lower()
        fraud_keywords = ['lottery', 'win', 'prize', 'kyc', 'blocked', 'click', 'http', 'free', 'reward', 'job offer', 'task', 'telegram money']
        
        is_fraud = any(keyword in text for keyword in fraud_keywords)
        
        if is_fraud:
            st.error("⚠️ హెచ్చరిక (WARNING): ఇది ఫేక్ లేదా ఆన్‌లైన్ మోసపూరిత లింక్/మెసేజ్ అయ్యే అవకాశం ఉంది!")
        else:
            st.success("✅ సురక్షితం (Safe): ఇందులో ఎలాంటి స్పష్టమైన మోసపూరిత లక్షణాలు కనుగొనబడలేదు.")

st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>Powered by Detector Pro Engine</p>", unsafe_allow_html=True)
