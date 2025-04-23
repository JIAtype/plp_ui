import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

def show_topic_analysis(selected_creator=None):
    col1, col2 = st.columns([2, 8])
    with col1:
        st.image("https://img.icons8.com/color/96/000000/youtube-play.png", width=80)
    with col2:
        # st.title("Content Creator Analytics")
        st.header("Positive Sentiment Topic Analysis")
        # st.markdown("<h1 class='main-header'>Video Comments Analysis</h1>", unsafe_allow_html=True)
    st.markdown("---")
    # st.header("Positive Sentiment Topic Analysis")
    topic_sentiment_df = pd.read_csv('data/topic_sentiment_summary.csv')
    
    if selected_creator:
        videos_data = pd.read_csv('data/video_sentiment_summary.csv')
        df_sentiment = videos_data[videos_data["Content Creator"] == selected_creator]
        if len(df_sentiment) == 0:
            st.warning(f"No data found for creator: {selected_creator}")
            return
        st.subheader(f"Topic Analysis for ⭐{selected_creator}⭐")
        
        # 提取所有话题并计算频率
        all_topics = []
        for topics_str in df_sentiment['Topics'].dropna():
            if isinstance(topics_str, str):
                # 假设话题是以某种方式分隔的，例如逗号
                topics = [t.strip() for t in topics_str.split(',')]
                all_topics.extend(topics)
        
        if all_topics:
            topic_counts = pd.Series(all_topics).value_counts().reset_index()
            topic_counts.columns = ['Topic', 'Count']
            
            # 显示前15个最常见话题
            top_topics = topic_counts.head(15)
            
            fig_topics = px.bar(
                top_topics, 
                x='Topic', 
                y='Count',
                title=f'Top 15 Topics for {selected_creator}',
                color='Count',
                color_continuous_scale='Blues'
            )
            
            fig_topics.update_layout(
                xaxis={'categoryorder':'total descending', 'tickangle': -45},
                yaxis_title='Frequency',
                margin=dict(l=50, r=50, t=80, b=100),
                height=500
            )
            
            st.plotly_chart(fig_topics, use_container_width=True)
        else:
            st.info("No topic data available for analysis")
    
    # 计算总提及次数和百分比
    topic_sentiment_df["Total Mentions"] = (
        topic_sentiment_df["Positive"] + 
        topic_sentiment_df["Negative"] + 
        topic_sentiment_df["Neutral"]
    )
    
    topic_sentiment_df["% Positive"] = (topic_sentiment_df["Positive"] / topic_sentiment_df["Total Mentions"] * 100).round(2)
    topic_sentiment_df["% Negative"] = (topic_sentiment_df["Negative"] / topic_sentiment_df["Total Mentions"] * 100).round(2)
    topic_sentiment_df["% Neutral"] = (topic_sentiment_df["Neutral"] / topic_sentiment_df["Total Mentions"] * 100).round(2)
    
    # 按照正面情感百分比排序
    topic_sentiment_df = topic_sentiment_df.sort_values("% Positive", ascending=False).reset_index(drop=True)
    
    # 创建两列布局
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Topic Sentiment Overview")
        # 显示前20个话题的正面情感百分比条形图
        fig = px.bar(
            topic_sentiment_df.head(20),
            x="Topic",
            y="% Positive",
            title="Top 20 Topics by Positive Sentiment (%)",
            labels={"% Positive": "Positive Sentiment (%)"},
            color="% Positive",
            color_continuous_scale="Blues",
            text="% Positive"  # 在条形上显示数值
        )
        
        fig.update_layout(
            xaxis_tickangle=-45,
            height=500,
            xaxis_title="Topic",
            yaxis_title="Positive Sentiment (%)"
        )
        
        # 添加数值标签格式
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        
        # Streamlit中正确显示plotly图表
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # 显示热门话题的数据表格
        st.subheader("Top Topics Data")
        st.dataframe(
            topic_sentiment_df.head(10)[["Topic", "Total Mentions", "% Positive", "% Negative", "% Neutral"]]
            .style.background_gradient(subset=["% Positive"], cmap="Blues")
            .format({"% Positive": "{:.2f}%", "% Negative": "{:.2f}%", "% Neutral": "{:.2f}%"})
        )
    
    st.subheader("Sentiment Breakdown per Topic")
    
    # 准备数据：融合数据框为长格式，用于分组条形图
    melted_df = topic_sentiment_df.melt(
        id_vars=["Topic", "Total Mentions"],
        value_vars=["Positive", "Negative", "Neutral"],
        var_name="Sentiment",
        value_name="Count"
    )
    
    # 过滤出按提及次数排序的前N个话题
    top_n = min(15, len(topic_sentiment_df))  # 防止数据量太小
    top_topics = topic_sentiment_df.nlargest(top_n, "Total Mentions")["Topic"].tolist()
    filtered_df = melted_df[melted_df["Topic"].isin(top_topics)]
    
    # 绘制分组条形图
    fig = px.bar(
        filtered_df,
        x="Topic",
        y="Count",
        color="Sentiment",
        barmode="group",
        title=f"Sentiment Breakdown for Top {top_n} Topics by Mentions",
        labels={"Count": "Number of Comments", "Topic": "Topic"},
        color_discrete_map={
            "Positive": "#2ca02c",  # 绿色
            "Negative": "#d62728",  # 红色
            "Neutral": "#1f77b4"    # 蓝色
        },
        hover_data=["Total Mentions"]
    )
    
    fig.update_layout(
        xaxis_tickangle=-45,
        height=500,
        legend_title="Sentiment Type",
        xaxis_title="Topic",
        yaxis_title="Number of Comments"
    )
    
    # Streamlit中正确显示plotly图表
    st.plotly_chart(fig, use_container_width=True)
    
    # 添加堆叠百分比图表
    st.subheader("Proportional Sentiment Distribution")
    
    # 准备比例图数据
    stack_data = topic_sentiment_df.head(10).copy()  # 只取前10个话题，避免拥挤
    
    fig = px.bar(
        stack_data,
        x="Topic",
        y=["% Positive", "% Negative", "% Neutral"],
        title="Sentiment Proportion for Top 10 Topics",
        labels={"value": "Percentage (%)", "variable": "Sentiment Type"},
        barmode="stack",
        color_discrete_map={
            "% Positive": "#2ca02c",
            "% Negative": "#d62728",
            "% Neutral": "#1f77b4"
        }
    )
    
    fig.update_layout(
        xaxis_tickangle=-45,
        height=500,
        legend_title="Sentiment Type",
        xaxis_title="Topic",
        yaxis_title="Percentage (%)"
    )
    
    # Streamlit中正确显示plotly图表
    st.plotly_chart(fig, use_container_width=True)
