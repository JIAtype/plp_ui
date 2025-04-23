import streamlit as st

def show_home():

    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.info("""
    This dashboard helps analyze YouTube 
    comments sentiment and trends to gain 
    actionable insights.
    """)

    # st.title("Content Analysis Dashboard")
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://img.icons8.com/color/96/000000/youtube-play.png", width=80)
    with col2:
        st.title("INSIGHTX")
        st.write("Analyze social media comments, revealing audience sentiment, popular topics, and engagement trends to inform content strategies and influencer marketing decisions using multiple AI models.")
        # st.markdown("<h1 class='main-header'>Video Comments Analysis</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("""
    ## Welcome to the Content Analysis Platform
    
    Hello there! 👋 Welcome to **INSIGHTX**, your go-to platform for understanding what people are saying about your videos and the creators they love!
    Ever wondered what your audience *really* thinks about your latest upload? Or maybe you're a business trying to find the perfect content creator to team up with? 
                Manually sifting through comments is like searching for a needle in a haystack!

    That's where **INSIGHTX** comes in! We use clever technology – think of it as a super-smart way to read and understand comments – to bring you valuable insights.

    *   **For Content Creators**: We help you figure out which topics your viewers are buzzing about and what they love (or maybe don't love!) about your content. This means you can create even better videos that your audience will adore, leading to more engagement and a bigger reach.

    *   **For Businesses**: Finding the right influencer can be tough. We make it easier by helping you understand which creators have audiences that are saying positive things about topics related to your brand. This way, you can make smart choices and build partnerships that really work.

    So, whether you're looking to fine-tune your content strategy or find the ideal collaborator, **INSIGHTX** is here to help you make sense of the conversation. Let's dive in and see what insights we can uncover together! 🎉
                
    ---

    ### Available Features:

    **For Content Creators:**
    - **Video-level analysis of comments and sentiments**, classifying individual comments as positive, negative, or neutral and determining an overall sentiment for each video.
    - **Creator summary with overall sentiment percentages**, providing a high-level view of audience engagement and reception for each content creator.
    - **Spam detection and analysis** of comments to ensure data quality and focus on genuine feedback.
    - **Positive sentiment topic analysis**, identifying the most popular and positively received discussion themes within video comments.
    - **Entity sentiment analysis**, uncovering public sentiment towards specific named entities (e.g., brands, people, locations) mentioned in the comments through various pipelines (A, B, C, D) and Positive-Unlabelled (PU) learning.

    **For Business Users:**
    - **Creator comparison overview**, enabling the comparison of different content creators based on metrics such as total videos, comments, topics, and overall sentiment.
    - **Multi-method sentiment analysis**, utilizing VADER, BART, and a fine-tuned RoBERTa model to provide a comprehensive and nuanced understanding of sentiment in comments.
    - **Topic/aspect-based sentiment analysis**, allowing businesses to evaluate how audiences feel about specific topics or product aspects discussed in the comments, using both LLM-suggested and TF-IDF-extracted aspects, as well as topics identified through topic modelling.
    - **Time series trends and insights**, tracking how overall and aspect-specific sentiment evolves across a creator's videos over time.
    - **Identification of creators with positive sentiment towards specific aspects**, helping businesses pinpoint influencers whose audiences show favourable opinions on product features or areas relevant to their campaigns.
    - **Ability to identify high-performing videos and creators for targeted collaboration**, based on the sentiment expressed towards specific aspects in individual videos.
    
    Use the sidebar to navigate to the appropriate section based on your needs.
    """)
    
    st.info("Select your user type from the sidebar to get started!")
    
    # Sample cards to illustrate available analyses
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Content Creator Analytics")
        st.image("images/Picture1.png", use_column_width=True)
        st.markdown("Gain insights into your content performance and audience sentiment")
    
    with col2:
        st.subheader("Business Intelligence")
        st.image("images/Picture2.png", use_column_width=True)
        st.markdown("Compare creators and discover trends to inform your marketing strategy") 
