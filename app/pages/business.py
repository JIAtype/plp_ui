import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from app.components.creator_comparison import show_creator_comparison
from app.components.tdidf_roberta_sentiment_analysis import show_tdidf_roberta_sentiment_analysis
from app.components.tdidf_vader_sentiment_analysis import show_tdidf_vader_sentiment_analysis
from app.components.topics_roberta_sentiment_analysis import show_roberta_sentiment_analysis
from app.components.video_summary import show_video_summary
from app.components.sentiment_summary import show_sentiment_summary
from app.components.topic_analysis import show_topic_analysis
from app.components.entity_analysis import show_entity_analysis
from app.components.topics_vader_sentiment_analysis import show_vader_sentiment_analysis
from app.components.tdidf_bart_sentiment_analysis import show_tdidf_bart_sentiment_analysis

def show_business_page():
    # 创建侧边栏过滤器
    st.sidebar.markdown("---")
    
    # 分析类型选择
    analysis_type = st.sidebar.radio(
        "Select Analysis",
        ["Video Summary","Sentiment Summary","Topic Analysis","Entity Analysis", "VADER Sentiment Analysis","ROBERTA ABSA Sentiment Analysis","TD-IDF VADER Sentiment Analysis","TD-IDF ROBERTA ABSA Sentiment Analysis","TD-IDF BART ABSA Sentiment Analysis","Analysis Comparison"]
    )
    
    # 显示选定的分析
    if analysis_type == "Analysis Comparison":
        show_creator_comparison()
    elif analysis_type == "Sentiment Summary":
        show_sentiment_summary()
    elif analysis_type == "Video Summary":
        show_video_summary()
    elif analysis_type == "Topic Analysis":
        show_topic_analysis()
    elif analysis_type == "Entity Analysis":
        show_entity_analysis()
    elif analysis_type == "VADER Sentiment Analysis":
        show_vader_sentiment_analysis()
    elif analysis_type == "ROBERTA ABSA Sentiment Analysis":
        show_roberta_sentiment_analysis()
    elif analysis_type == "TD-IDF VADER Sentiment Analysis":
        show_tdidf_vader_sentiment_analysis()
    elif analysis_type == "TD-IDF ROBERTA ABSA Sentiment Analysis":
        show_tdidf_roberta_sentiment_analysis()
    elif analysis_type == "TD-IDF BART ABSA Sentiment Analysis":
        show_tdidf_bart_sentiment_analysis()
