<div align="center">
[English](README.md) | [简体中文](README.zh-CN.md)
<div/>

# Content Analysis  

https://plpuigit-250420.streamlit.app/

This is an interactive user interface based on Streamlit that provides customized analysis results display for content creators and businesses. The application allows users to browse and analyze video comments, sentiment and topic data to gain valuable insights.

## Features

### Content Creator Module

- **Video Level Analysis**: Displays the number of comments and topics for each video, and uses color gradients to visually highlight videos with high interactions and topics

- **Creator Summary**: Displays the overall sentiment percentage and total number of comments for each creator

- **Positive Sentiment Topic Analysis**: Sorts topics by positive sentiment percentage and displays the sentiment distribution of each topic

- **Entity Sentiment Analysis**: Displays entities appearing in comments and their sentiment scores

### Commercial Use Module

- **Creator Comparison Overview**: Compares key metrics of multiple creators

- **Sentiment Analysis Method Selection**: Displays the results of different sentiment analysis methods

- **Theme/Aspect-Based Analysis**: Displays sentiment analysis of different themes/aspects for each creator

- **Time Series Trend**: Displays the trend of sentiment changes over time

## Project Structure

```
plp_ui/
├── app.py                    # 主程序入口
├── app/
│   ├── pages/                # 页面模块
│   │   ├── home.py           # 主页
│   │   ├── creator.py        # 内容创作者页面
│   │   └── business.py       # 商业用户页面
│   ├── components/           # 组件模块
│   │   ├── video_analysis.py # 视频分析组件
│   │   ├── creator_summary.py# 创作者汇总组件
│   │   ├── topic_analysis.py # 主题分析组件
│   │   ├── entity_analysis.py# 实体分析组件
│   │   ├── creator_comparison.py # 创作者比较组件
│   │   ├── sentiment_methods.py  # 情感分析方法组件
│   │   ├── aspect_analysis.py    # 方面分析组件
│   │   └── time_series.py        # 时间序列组件
│   ├── utils/                # 工具函数
│   └── data/                 # 数据处理模块
├── requirements.txt          # 项目依赖
└── README.md                 # 项目说明
```

## Installation and Running

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
streamlit run app.py
```

## System Requirements

- Python 3.8+
- Install all packages listed in requirements.txt
