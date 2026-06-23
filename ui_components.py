import streamlit as st
import pandas as pd

def initialize_dashboard(title: str, subtitle: str, icon: str = "🤖"):
    """Configures the premium page layout and applies a structured warm light-mode header matrix."""
    
    # Premium Executive Light Cream Theme Injection
    st.markdown("""
        <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            /* Main Global Canvas - Soft Light Cream/Alabaster */
            .stApp, [data-testid="stAppViewContainer"] {
                background-color: #fdfbf7 !important;
                animation: fadeIn 0.15s ease-in-out forwards;
            }
            
            /* Main header text overrides */
            h1, h2, h3, h4, h5, h6, .stSubheader {
                color: #2b2623 !important; /* Elegant Warm Charcoal */
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
                font-weight: 700 !important;
                letter-spacing: -0.3px;
            }
            
            /* Standard text, paragraph, and label alignment */
            .stMarkdown p, p, span, label, div[data-testid="stWidgetLabel"] p {
                color: #514b47 !important; /* Soft Coordinated Earthy Dark Gray */
                font-weight: 500 !important;
            }
            
            /* Structural Containers transformed into soft Ivory tech cards */
            div[data-testid="stContainer"], .stAlert {
                background-color: #ffffff !important;
                border: 1px solid #efebe4 !important;
                border-radius: 14px !important;
                box-shadow: 0 4px 12px rgba(139, 128, 118, 0.04) !important;
                padding: 24px !important;
            }
            
            /* Form Control Elements (Text Inputs & Text Areas) */
            .stTextArea textarea, .stTextInput input {
                background-color: #ffffff !important;
                color: #2b2623 !important;
                border: 1px solid #dcd6cd !important;
                border-radius: 10px !important;
                font-size: 15px !important;
                padding: 12px !important;
            }
            
            /* Interactive focus rings for input boxes */
            .stTextArea textarea:focus, .stTextInput input:focus {
                border-color: #8c7e74 !important; /* Premium Taupe/Warm Gray Focus */
                box-shadow: 0 0 0 3px rgba(140, 126, 116, 0.15) !important;
            }
            
            /* 🛠️ FIXED: Master Buttons colored deep dark brown with forced bold white text */
            .stButton button {
                background-color: #4a3f35 !important; /* Premium Elegant Dark Brown */
                border: none !important;
                border-radius: 10px !important;
                font-size: 16px !important;
                padding: 12px 24px !important;
                box-shadow: 0 4px 10px rgba(74, 63, 53, 0.15) !important;
                transition: all 0.2s ease-in-out;
            }
            
            /* Target inner button label directly to force white and bold */
            .stButton button p, .stButton button span {
                color: #ffffff !important;
                font-weight: 800 !important;
            }
            
            /* Interactive hover states */
            .stButton button:hover {
                background-color: #5c4f43 !important; /* Slightly lighter brown on hover */
                box-shadow: 0 6px 16px rgba(74, 63, 53, 0.22) !important;
                transform: translateY(-1px);
            }
            .stButton button:hover p {
                color: #ffffff !important;
            }
            
            /* Native Streamlit Metrics Styling */
            div[data-testid="stMetricValue"] {
                color: #2b2623 !important;
                font-weight: 800 !important;
                font-size: 32px !important;
            }
            div[data-testid="stMetricLabel"] p {
                color: #78706a !important;
                font-weight: 600 !important;
            }
            
            /* Native Tabs Customizations */
            button[data-baseweb="tab"] {
                color: #78706a !important;
                font-weight: 600 !important;
            }
            button[data-baseweb="tab"][aria-selected="true"] {
                color: #2b2623 !important;
                border-bottom-color: #2b2623 !important;
            }
        </style>
    """, unsafe_allow_html=True)

def render_metrics_panel(metrics_data: list):
    """Renders a premium, bordered KPI card grid panel dynamically."""
    cols = st.columns(len(metrics_data))
    for i, data in enumerate(metrics_data):
        with cols[i]:
            with st.container(border=True):
                delta_color = "inverse" if data.get("inverse") else "normal"
                st.metric(
                    label=data["label"], 
                    value=data["value"], 
                    delta=data.get("delta"),
                    delta_color=delta_color
                )

def create_workspace_layout(ratio: list = [1, 2]):
    """Creates a balanced, asymmetric side-by-side workspace split."""
    return st.columns(ratio, gap="large")

def render_content_card(title: str, content: str, is_markdown: bool = True):
    """Encloses raw output logs inside defined interactive wireframe borders."""
    st.markdown(f"#### {title}")
    with st.container(border=True):
        if is_markdown:
            st.markdown(content)
        else:
            st.text(content)

def render_history_ledger(title: str, dataframe: pd.DataFrame):
    """Outputs high-density transactional tracking metrics tables cleanly."""
    st.markdown(f"#### {title}")
    st.dataframe(dataframe, use_container_width=True, hide_index=True)