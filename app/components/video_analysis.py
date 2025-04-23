import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

def show_video_analysis(selected_creator):
    col1, col2 = st.columns([2, 8])
    with col1:
        st.image("https://img.icons8.com/color/96/000000/youtube-play.png", width=80)
    with col2:
        # st.title("Content Creator Analytics")
        st.header("Video-Level Sentiment Analysis")
        # st.markdown("<h1 class='main-header'>Video Comments Analysis</h1>", unsafe_allow_html=True)
    st.markdown("---")

    try:
        # 加载视频情感分析数据
        videos_data = pd.read_csv('data/video_sentiment_summary.csv')
        df_sentiment = videos_data[videos_data["Content Creator"] == selected_creator]
        
        if df_sentiment.empty:
            st.warning(f"No sentiment analysis data available for {selected_creator}")
            return

        st.subheader("Video Sentiment Summary")

        # 定义要显示的列
        columns_to_show = [
            "Content Creator", "Playlist ID", "Video ID", 
            "Overall Sentiment", "Positive %", "Negative %", "Neutral %",
            "Number of Topics", "Topics"
        ]

        # 确保所有所需列都存在
        df_summary_view = df_sentiment[columns_to_show].copy()

        # 格式化百分比列
        for col in ["Positive %", "Negative %", "Neutral %"]:
            if col in df_summary_view.columns:
                df_summary_view[col] = df_summary_view[col].apply(lambda x: f"{x:.2f}%" if pd.notna(x) else "N/A")

        # 使用pandas的styler来设置颜色渐变
        def style_dataframe(df):
            # 提取百分比值用于颜色渐变
            df_numeric = df.copy()
            for col in ["Positive %", "Negative %", "Neutral %"]:
                if col in df.columns:
                    df_numeric[col] = df[col].str.rstrip('%').astype(float)
            
            # 应用样式
            return df_numeric.style\
                .background_gradient(subset=["Positive %", "Negative %", "Neutral %"], cmap="Blues")\
                .format({"Positive %": "{:.2f}%", "Negative %": "{:.2f}%", "Neutral %": "{:.2f}%"})\
                .set_properties(**{
                    'white-space': 'pre-wrap',  # 允许文本换行
                    'text-align': 'left'
                })\
                .set_table_styles([
                    {'selector': 'td', 'props': [('max-width', '200px'), ('word-wrap', 'break-word')]},
                ])

        # 显示带样式的数据框
        styled_df = style_dataframe(df_summary_view)
        st.write(styled_df)

        # 添加自定义CSS以确保表格可以水平滚动且文本换行
        st.markdown("""
        <style>
            .stTable {
                overflow-x: auto;
            }
            .dataframe td {
                white-space: pre-wrap !important;
                max-width: 200px;
                word-wrap: break-word;
            }
            .dataframe th {
                white-space: normal !important;
            }
        </style>
        """, unsafe_allow_html=True)

        # 添加情感分布图表
        st.subheader("Sentiment Distribution Across Videos")
        
        # 为图表准备数据 - 取前10个视频进行比较
        chart_data = df_sentiment.head(10).copy()
        
        # 创建情感分布堆叠条形图
        fig_sentiment = go.Figure()
        
        fig_sentiment.add_trace(go.Bar(
            x=chart_data['Video ID'],
            y=chart_data['Positive %'],
            name='Positive',
            marker_color='rgb(26, 118, 255)'
        ))
        
        fig_sentiment.add_trace(go.Bar(
            x=chart_data['Video ID'],
            y=chart_data['Neutral %'],
            name='Neutral',
            marker_color='rgb(158, 158, 158)'
        ))
        
        fig_sentiment.add_trace(go.Bar(
            x=chart_data['Video ID'],
            y=chart_data['Negative %'],
            name='Negative',
            marker_color='rgb(255, 79, 79)'
        ))
        
        fig_sentiment.update_layout(
            title='Sentiment Distribution by Video',
            xaxis={'categoryorder':'total descending', 'tickangle': -45},
            yaxis=dict(title='Percentage'),
            barmode='stack',
            legend=dict(x=0, y=1.0),
            margin=dict(l=50, r=50, t=80, b=100),
            height=600
        )
        
        st.plotly_chart(fig_sentiment, use_container_width=True)
        
        # 添加视频按情感排序的表格
        st.subheader("Videos Ranked by Sentiment")
        
        # 创建一个排序后的视图
        df_ranked = df_sentiment.sort_values(by="Positive %", ascending=False).copy()
        columns_for_ranking = ["Video ID", "Overall Sentiment", "Positive %", "Negative %", "Neutral %"]
        df_ranked_view = df_ranked[columns_for_ranking]
        
        # 格式化百分比
        for col in ["Positive %", "Negative %", "Neutral %"]:
            if col in df_ranked_view.columns:
                df_ranked_view[col] = df_ranked_view[col].apply(lambda x: f"{x:.2f}%" if pd.notna(x) else "N/A")
        
        # 用热图样式显示排名
        fig_ranked = ff.create_table(df_ranked_view.head(10))
        st.plotly_chart(fig_ranked, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error analyzing video data: {str(e)}")
        st.exception(e)  # 显示详细错误信息，方便调试
