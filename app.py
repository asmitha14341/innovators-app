import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Innovators",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
    .header {
        background: linear-gradient(135deg, #0d1117, #1a1a2e);
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #00ff88;
        text-align: center;
        margin-bottom: 2rem;
    }
    .header h1 { color: #00ff88; font-size: 2.5rem; }
    .header p  { color: #aaa; }
</style>
<div class="header">
    <h1>🛡️ Innovators Team</h1>
    <p>Cybersecurity · AI · Cloud Projects</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Projects Built", "12", "+3")
col2.metric("Threats Detected", "847", "+12%")
col3.metric("Cloud Uptime", "99.9%", "Stable")

st.divider()
st.subheader("📊 Project Activity")

data = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Cybersecurity": [3,5,4,7,6,9],
    "AI": [2,3,5,4,8,7],
    "Cloud": [1,2,3,5,4,6]
})

fig = px.line(data, x="Month",
              y=["Cybersecurity","AI","Cloud"],
              color_discrete_sequence=["#00ff88","#6C63FF","#3EC6E0"])
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("🤖 AI Tools")
prompt = st.text_area("Ask anything about Cybersecurity or AI:")
if st.button("✨ Get Answer", type="primary"):
    with st.spinner("Thinking..."):
        import time
        time.sleep(1)
        st.success("💡 Insight: Always use multi-factor authentication and encrypt sensitive data at rest and in transit.")
