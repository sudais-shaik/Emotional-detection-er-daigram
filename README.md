# Emotional-detection-er-daigram
# 🎓 Emotion Detection & Learning Support Engine

## 📌 Project Overview

The Emotion Detection & Learning Support Engine is an AI-based educational application designed to identify students' emotions from text-based learning problems and provide personalized learning guidance.

Students often experience different emotions while learning, such as boredom, confidence, confusion, curiosity, and frustration. Detecting these emotions can help create a more supportive and personalized learning experience.

This project provides an interactive system where a student selects an academic field, describes a learning problem, and receives emotion analysis, confidence scores, mixed-emotion detection, and personalized learning guidance.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Detect student emotions from text input.
- Classify emotions into five categories.
- Identify mixed emotions.
- Display confidence scores for detected emotions.
- Compare emotion detection approaches.
- Generate personalized learning guidance.
- Maintain session history.
- Store interaction data for future analysis.
- Provide analytics and visualizations.
- Develop an interactive Streamlit-based user interface.

---

## 😊 Supported Emotions

The system supports five emotion categories:

- Bored
- Confident
- Confused
- Curious
- Frustrated

---

# 📚 Project Development

The project was developed through six major Epics.

---

## 🚀 Epic 1: Environment Setup and Project Configuration

The first Epic focused on preparing the development environment and organizing the project structure.

### Tasks Completed

- Python environment setup.
- Required dependency configuration.
- GitHub repository creation.
- Project folder structure preparation.
- Requirements file creation.
- Environment configuration.
- Development workflow preparation.

### Important Files

- `README.md`
- `requirements.txt`
- `.gitignore`
- `.env.example`
- `PREREQUISITES.md`
- `PROJECT_WORKFLOW.md`
- `PYTHON_SETUP.md`

---

## 🧠 Epic 2: Emotion Model Development and Training

Epic 2 focused on preparing the emotion detection workflow and training classification models.

### Tasks Completed

- GPU environment configuration.
- Dataset creation and loading.
- Text preprocessing.
- Text cleaning.
- Tokenization.
- Vocabulary creation.
- Sequence padding.
- Emotion label encoding.
- BiLSTM model implementation.
- BiLSTM model training.
- Domain-adaptive fine-tuning workflow.
- Transformer-style emotion classifier implementation.
- Model export and integration preparation.

### Emotion Classes

The models classify student text into:

1. Bored
2. Confident
3. Confused
4. Curious
5. Frustrated

### Generated Model Artifacts

- BiLSTM emotion model.
- Student-adaptive model.
- Transformer-style emotion classifier.
- Model configuration files.
- Preprocessed emotion datasets.

---

## 🔍 Epic 3: Core Emotion Detection Pipeline

Epic 3 focused on developing the main emotion prediction pipeline.

### Tasks Completed

- Text preprocessing.
- Keyword-based emotion enhancement.
- Five-class softmax classification workflow.
- Model comparison structure.
- Class weighting.
- Keyword score adjustments.
- Mixed-emotion detection.
- Secondary emotion threshold detection.
- Unified prediction schema.
- CSV persistence.
- Cached model loading structure.

### Mixed Emotion Detection

The application can identify multiple emotions when secondary emotion scores cross the configured threshold.

Example:

`Confused + Curious`

This allows the system to represent complex student emotions instead of returning only one emotion.

---

## 🤖 Epic 4: AI-Powered Guidance Engine

Epic 4 focused on generating supportive and personalized educational guidance based on detected emotions.

### Tasks Completed

- Academic field selection.
- Student learning problem input.
- Emotion and confidence integration.
- Guidance prompt construction.
- Emotion-aware response generation.
- Field-aware learning guidance.
- Fallback response templates.
- Response regeneration workflow.
- Session history.
- CSV interaction logging.

### Example

Student Input:

`I cannot understand neural networks and I feel confused.`

Detected Emotion:

`Confused`

Generated Guidance:

`This topic may feel difficult. Break the concept into smaller parts and start with a simple example.`

---

## 🖥️ Epic 5: Streamlit User Interface Implementation

Epic 5 focused on developing the interactive user interface.

The final application was created using Streamlit.

### Application Features

- Responsive application layout.
- Sidebar dashboard.
- Model status display.
- Total interaction tracking.
- Academic field selection.
- Learning problem input.
- Emotion analysis button.
- Clear history functionality.
- Primary emotion display.
- Confidence score display.
- Mixed-emotion detection.
- Emotion confidence progress bars.
- Personalized learning guidance.
- Session history.
- Analytics dashboard.
- Emotion distribution visualization.
- Confidence timeline.
- Input validation.
- Error handling.

---

## ✅ Epic 6: User Interaction Validation and Deployment Readiness

Epic 6 focused on validating the complete application workflow.

### Validation Tasks

- Application startup validation.
- Model loading workflow verification.
- Input validation.
- Emotion prediction verification.
- Mixed-emotion detection testing.
- Confidence score verification.
- Guidance generation validation.
- Session history verification.
- CSV logging validation.
- Analytics dashboard validation.
- Performance checks.
- Caching workflow verification.
- Deployment readiness checks.

The final workflow was tested from user input to emotion analysis, personalized guidance, history tracking, and analytics display.

---

# ⚙️ System Workflow

The application follows this workflow:

1. The user opens the application.
2. The user selects an academic field.
3. The user describes their learning problem.
4. The text is cleaned and processed.
5. Emotion-related keywords are analyzed.
6. Emotion confidence scores are generated.
7. The primary emotion is identified.
8. Mixed emotions are detected.
9. Personalized learning guidance is generated.
10. The interaction is stored in session history.
11. Analytics are updated.

---

# 🏗️ Project Architecture

The overall system architecture is:

Student Input

↓

Text Preprocessing

↓

Emotion Analysis

↓

Emotion Classification

↓

Mixed Emotion Detection

↓

Confidence Score Generation

↓

Personalized Learning Guidance

↓

Session History

↓

Analytics Dashboard

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Machine Learning and Data Processing

- PyTorch
- NumPy
- Pandas
- Scikit-learn

## Natural Language Processing

- Text preprocessing
- Tokenization
- Keyword-based emotion enhancement
- BiLSTM workflow
- Transformer-style classification workflow

## User Interface

- Streamlit

## Data Visualization

- Streamlit Charts
- Plotly

## Development Platforms

- Google Colab
- GitHub

## Additional Tools

- ngrok
- pyngrok

---

# 📂 Project Structure

```text
Emotion-Detection-Learning-Support-Engine/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── PREREQUISITES.md
├── PROJECT_WORKFLOW.md
├── PYTHON_SETUP.md
│
├── Epic_2_Model_Training.ipynb
├── Epic_3_Core_Emotion_Detection_Pipeline.ipynb
├── Epic_4_AI_Powered_Guidance_Engine.ipynb
├── Epic_5_Streamlit_UI_Implementation.ipynb
├── Epic_6_User_Interaction_Validation.ipynb
│
├── models/
│
├── notebooks/
│
└── data/
application link 
https://lend-simplify-unsorted.ngrok-free.dev/
