import streamlit as st
from nlp.pipeline import run_pipeline
from llm.generator import generate_answer

st.set_page_config(page_title="Crime Scene Investigator", page_icon="🕵️", layout="wide")

st.markdown("""
<style>
    .main {background-color: #0a0a0a;}
    .title {color: #ff4444; font-size: 3em; font-weight: bold; text-align: center;}
    .subtitle {color: #aaaaaa; text-align: center; font-size: 1.2em;}
    .report-box {background-color: #1a1a1a; border-left: 4px solid #ff4444; 
                 padding: 20px; border-radius: 5px; margin-top: 20px;}
    .badge {background-color: #ff4444; color: white; padding: 5px 10px; 
            border-radius: 20px; font-size: 0.8em;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🕵️ Crime Scene Investigator</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Describe a crime scene and let AI analyze the clues</p>', unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("🔍 Describe the Crime Scene:", height=150, 
                               placeholder="e.g. I found a dead body in the kitchen with a knife nearby and blood on the floor...")
    
    if st.button("🔎 Investigate!", use_container_width=True):
        if user_input:
            with st.spinner("🕵️ Analyzing crime scene..."):
                pipeline_result = run_pipeline(user_input)
                response = generate_answer(
                    pipeline_result['original_query'],
                    pipeline_result['intent'],
                    pipeline_result['entities'],
                    pipeline_result['relevant_docs']
                )
            
            st.markdown("### 📋 Investigation Results")
            
            col3, col4, col5 = st.columns(3)
            with col3:
                st.metric("🎯 Intent", pipeline_result['intent'])
            with col4:
                st.metric("📚 Docs Found", len(pipeline_result['relevant_docs']))
            with col5:
                weapons = pipeline_result['entities'].get('weapons', [])
                st.metric("🔪 Weapons", len(weapons))
            
            st.markdown("### 🔍 Extracted Entities")
            entities = pipeline_result['entities']
            if entities:
                for key, values in entities.items():
                    st.write(f"**{key.upper()}:** {', '.join(values)}")
            else:
                st.write("No specific entities detected")
            
            st.markdown("### 🕵️ Investigation Report")
            st.markdown(f'<div class="report-box">{response}</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please describe the crime scene first!")

with col2:
    st.markdown("### 📌 How to Use")
    st.info("1. Describe the crime scene in detail\n2. Click Investigate!\n3. AI will analyze clues, detect intent, extract entities and generate a full investigation report")
    
    st.markdown("### 🔑 What I Detect")
    st.success("✅ Weapons\n✅ Locations\n✅ Suspects\n✅ Evidence\n✅ Motive")