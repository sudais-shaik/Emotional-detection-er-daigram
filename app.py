
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="Emotion Detection & Learning Support Engine",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------
# SESSION STATE
# -------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# EMOTION PREDICTION
# -------------------------------

emotion_classes = [
    "Bored",
    "Confident",
    "Confused",
    "Curious",
    "Frustrated"
]

def predict_emotion(text):

    text = text.lower()

    scores = {
        "Bored": 0.10,
        "Confident": 0.10,
        "Confused": 0.10,
        "Curious": 0.10,
        "Frustrated": 0.10
    }

    keyword_map = {
        "Bored": [
            "bored",
            "boring",
            "uninteresting"
        ],

        "Confident": [
            "confident",
            "easy",
            "sure",
            "solve"
        ],

        "Confused": [
            "confused",
            "difficult",
            "understand",
            "confusing"
        ],

        "Curious": [
            "curious",
            "learn",
            "know",
            "how"
        ],

        "Frustrated": [
            "frustrated",
            "stuck",
            "cannot",
            "annoyed"
        ]
    }

    for emotion, keywords in keyword_map.items():

        for keyword in keywords:

            if keyword in text:
                scores[emotion] += 0.30

    total = sum(scores.values())

    scores = {
        emotion: score / total
        for emotion, score in scores.items()
    }

    primary_emotion = max(
        scores,
        key=scores.get
    )

    confidence = scores[primary_emotion]

    mixed_emotions = [
        emotion
        for emotion, score in scores.items()
        if score >= 0.15
    ]

    return (
        primary_emotion,
        confidence,
        scores,
        mixed_emotions
    )


# -------------------------------
# GUIDANCE ENGINE
# -------------------------------

def generate_guidance(field, emotion):

    responses = {

        "Bored":
        f"Try making your {field} learning more interactive. "
        "Use practical examples and short challenges.",

        "Confident":
        f"You are making good progress in {field}. "
        "Try solving a more advanced problem.",

        "Confused":
        f"This {field} topic may feel difficult. "
        "Break the concept into smaller parts and "
        "start with a simple example.",

        "Curious":
        f"Your curiosity about {field} is valuable. "
        "Explore examples and connect new concepts "
        "with what you already know.",

        "Frustrated":
        f"Learning {field} can take time. "
        "Focus on one small concept at a time "
        "and practice gradually."
    }

    return responses[emotion]


# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("📊 Dashboard")

st.sidebar.metric(
    "Model Status",
    "Ready"
)

st.sidebar.metric(
    "Total Interactions",
    len(st.session_state.history)
)

st.sidebar.success(
    "Emotion Detection Engine Active"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Supported Emotions:\n\n"
    "• Bored\n"
    "• Confident\n"
    "• Confused\n"
    "• Curious\n"
    "• Frustrated"
)


# -------------------------------
# MAIN UI
# -------------------------------

st.title(
    "🎓 Emotion Detection & Learning Support Engine"
)

st.write(
    "Detect student emotions and receive "
    "personalized learning guidance."
)

st.markdown("---")


fields = [

    "Artificial Intelligence",
    "Machine Learning",
    "Data Science",
    "Computer Science",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Engineering"
]


field = st.selectbox(
    "📚 Select Academic Field",
    fields
)


problem = st.text_area(

    "✏️ Describe Your Learning Problem",

    placeholder=(
        "Example: I am confused and frustrated "
        "because I cannot understand neural networks."
    ),

    height=150
)


col1, col2 = st.columns(2)


with col1:

    analyze = st.button(
        "🔍 Analyze Emotion",
        use_container_width=True
    )


with col2:

    clear = st.button(
        "🗑️ Clear History",
        use_container_width=True
    )


# -------------------------------
# CLEAR HISTORY
# -------------------------------

if clear:

    st.session_state.history = []

    st.success(
        "Session history cleared successfully!"
    )


# -------------------------------
# ANALYSIS
# -------------------------------

if analyze:

    if not problem.strip():

        st.error(
            "Please enter your learning problem."
        )

    else:

        with st.spinner(
            "Analyzing your emotion..."
        ):

            (
                emotion,
                confidence,
                scores,
                mixed_emotions

            ) = predict_emotion(problem)


            guidance = generate_guidance(
                field,
                emotion
            )


        st.success(
            "Analysis completed successfully!"
        )


        st.markdown("---")

        st.header("🎯 Emotion Analysis")


        metric1, metric2, metric3 = st.columns(3)


        metric1.metric(
            "Primary Emotion",
            emotion
        )


        metric2.metric(
            "Confidence",
            f"{confidence:.1%}"
        )


        metric3.metric(
            "Detected Emotions",
            len(mixed_emotions)
        )


        st.subheader(
            "🔀 Mixed Emotions"
        )


        st.write(
            " + ".join(mixed_emotions)
        )


        st.subheader(
            "📊 Emotion Confidence Scores"
        )


        for emotion_name, score in scores.items():

            st.write(
                f"**{emotion_name}: "
                f"{score:.1%}**"
            )

            st.progress(
                min(float(score), 1.0)
            )


        st.markdown("---")


        st.header(
            "🤖 Personalized Learning Guidance"
        )


        st.info(guidance)


        interaction = {

            "Time":
            datetime.now().strftime(
                "%H:%M:%S"
            ),

            "Field":
            field,

            "Problem":
            problem,

            "Emotion":
            emotion,

            "Confidence":
            round(confidence, 4)
        }


        st.session_state.history.append(
            interaction
        )


# -------------------------------
# HISTORY & ANALYTICS
# -------------------------------

if st.session_state.history:

    st.markdown("---")

    st.header(
        "📈 Session History & Analytics"
    )


    history_df = pd.DataFrame(
        st.session_state.history
    )


    tab1, tab2 = st.tabs(
        [
            "📋 History",
            "📊 Analytics"
        ]
    )


    with tab1:

        st.dataframe(
            history_df,
            use_container_width=True
        )


    with tab2:

        emotion_counts = (
            history_df["Emotion"]
            .value_counts()
        )

        st.subheader(
            "Emotion Distribution"
        )

        st.bar_chart(
            emotion_counts
        )


        st.subheader(
            "Confidence Timeline"
        )

        st.line_chart(
            history_df["Confidence"]
        )


st.markdown("---")

st.caption(
    "Emotion Detection & Learning Support Engine"
)
