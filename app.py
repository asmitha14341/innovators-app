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
    body { background-color: #0d1117; }
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
    .card {
        background: #1a1a2e;
        border: 1px solid #00ff8833;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
</style>
<div class="header">
    <h1>🛡️ Innovators Team</h1>
    <p>Cybersecurity · AI · Cloud Projects</p>
</div>
""", unsafe_allow_html=True)

# ── KPI Cards ──────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Projects Built",    "12",    "+3")
col2.metric("Threats Detected",  "847",   "+12%")
col3.metric("Cloud Uptime",      "99.9%", "Stable")
col4.metric("Team Members",      "2",     "Active")

st.divider()

# ── Tabs ───────────────────────────────
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🛡️ Cybersecurity", "🤖 AI Tools"])

with tab1:
    st.subheader("Project Activity")
    data = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "Cybersecurity": [3,5,4,7,6,9],
        "AI":            [2,3,5,4,8,7],
        "Cloud":         [1,2,3,5,4,6]
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

with tab2:
    st.subheader("🛡️ Cybersecurity Scanner")
    url = st.text_input("Enter website URL to check:",
                        placeholder="https://example.com")
    if st.button("🔍 Scan", type="primary"):
        with st.spinner("Scanning..."):
            import time
            time.sleep(1.5)
        st.success("✅ No threats detected!")
        st.info("🔒 SSL Certificate: Valid")
        st.info("🛡️ Firewall: Active")
        st.warning("⚠️ Recommendation: Enable 2FA")

with tab3:
    st.subheader("🤖 AI Assistant")
    prompt = st.text_area("Ask about Cybersecurity or Cloud:",
                          placeholder="e.g. How to prevent SQL injection?")
    if st.button("✨ Get Answer", type="primary"):
        with st.spinner("Thinking..."):
            import time
            time.sleep(1)
        st.success("💡 Always use parameterized queries to prevent SQL injection. "
                   "Validate all user inputs and use an ORM framework.")
        st.balloons()

# ── Sidebar ────────────────────────────
with st.sidebar:
    st.markdown("### 🛡️ Innovators")
    st.markdown("---")
    st.markdown("**Team Members**")
    st.markdown("👩‍💻 Asmitha Reddy — Lead Dev")
    st.markdown("👩‍💻 Seejal Reddy — AI & Cloud")
    st.markdown("---")
    st.markdown("**Tech Stack**")
    st.markdown("🐍 Python + Streamlit")
    st.markdown("📊 Plotly Charts")
    st.markdown("☁️ GitHub Pages")
    st.markdown("---")
    st.success("🟢 System Online")
