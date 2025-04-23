def show_creator_comparison():
    import streamlit as st
    
    # 定义所有可用的分析类型
    analysis_types = [
        "Video Summary",
        "Sentiment Analysis",
        "Topic Analysis",
        "Entity Analysis", 
        "Topics As Aspects - VADER Sentiment Analysis",
        "Topics As Aspects - ROBERTA ABSA Sentiment Analysis",
        "TD-IDF Extracted Aspects - VADER Sentiment Analysis",
        "TD-IDF Extracted Aspects - ROBERTA ABSA Sentiment Analysis",
        "TD-IDF Extracted Aspects - BART ABSA Sentiment Analysis"
    ]
    
    # 创建两列布局
    col1, col2 = st.columns(2)
    
    # 在第一列选择第一个分析类型
    with col1:
        analysis_type_1 = st.selectbox(
            "Select First Analysis Type",
            options=analysis_types,
            index=0,
            key="analysis_1"
        )
    
    # 在第二列选择第二个分析类型
    with col2:
        analysis_type_2 = st.selectbox(
            "Select Second Analysis Type",
            options=analysis_types,
            index=1, 
            key="analysis_2"
        )
    
    # 创建两列布局来显示两个分析
    display_col1, display_col2 = st.columns(2)
    
    # 在第一列显示第一个分析
    with display_col1:
        # st.subheader(analysis_type_1)
        display_analysis(analysis_type_1)
    
    # 在第二列显示第二个分析
    with display_col2:
        # st.subheader(analysis_type_2)
        display_analysis(analysis_type_2)

# 辅助函数，用于根据分析类型显示相应的组件
def display_analysis(analysis_type):
    from app.components.video_summary import show_video_summary
    from app.components.sentiment_summary import show_sentiment_summary
    from app.components.topic_analysis import show_topic_analysis
    from app.components.entity_analysis import show_entity_analysis
    from app.components.topics_vader_sentiment_analysis import show_vader_sentiment_analysis
    from app.components.topics_roberta_sentiment_analysis import show_roberta_sentiment_analysis
    from app.components.tdidf_vader_sentiment_analysis import show_tdidf_vader_sentiment_analysis
    from app.components.tdidf_roberta_sentiment_analysis import show_tdidf_roberta_sentiment_analysis
    from app.components.tdidf_bart_sentiment_analysis import show_tdidf_bart_sentiment_analysis
    
    if analysis_type == "Video Summary":
        show_video_summary()
    elif analysis_type == "Sentiment Analysis":
        show_sentiment_summary()
    elif analysis_type == "Topic Analysis":
        show_topic_analysis()
    elif analysis_type == "Entity Analysis":
        show_entity_analysis()
    elif analysis_type == "Topics As Aspects - VADER Sentiment Analysis":
        show_vader_sentiment_analysis()
    elif analysis_type == "Topics As Aspects - ROBERTA ABSA Sentiment Analysis":
        show_roberta_sentiment_analysis()
    elif analysis_type == "TD-IDF Extracted Aspects - VADER Sentiment Analysis":
        show_tdidf_vader_sentiment_analysis()
    elif analysis_type == "TD-IDF Extracted Aspects - ROBERTA ABSA Sentiment Analysis":
        show_tdidf_roberta_sentiment_analysis()
    elif analysis_type == "TD-IDF Extracted Aspects - BART ABSA Sentiment Analysis":
        show_tdidf_bart_sentiment_analysis()
