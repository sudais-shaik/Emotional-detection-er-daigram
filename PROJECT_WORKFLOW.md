# Project Workflow

## Emotion Detection and Learning Support Engine

This document describes the complete development workflow of the Emotion Detection and Learning Support Engine. The project is divided into six major epics covering environment setup, model training, emotion detection, AI-powered learning guidance, user interface development, testing, and deployment readiness.

## Epic 1: Environment Setup and Dependency Configuration

The first phase focuses on preparing the development environment and installing all required tools and dependencies.

### Story 1: Obtain Gemini API Key

Create and configure a Gemini API key for generating AI-powered empathetic learning support responses.

### Story 2: Install Python and Create Virtual Environment

Install Python 3.9 or above and create a dedicated virtual environment for clean dependency management.

### Story 3: Install Project Dependencies

Install all required Python libraries and packages needed for machine learning, NLP, AI integration, data processing, and Streamlit development.

### Story 4: Create the Environment Configuration File

Create a `.env` file for securely managing environment variables such as the Gemini API key.

### Story 5: Verify Model and Data Directories

Ensure that the required BiLSTM and BERT model directories and dataset directories are correctly created and configured.

### Story 6: Prepare Project Folder Structure

Create an organized project folder structure for source code, models, datasets, configuration files, analytics, and other project components.

---

## Epic 2: Kaggle Model Training and Integration

This phase focuses on training, fine-tuning, evaluating, and integrating the machine learning models used for emotion detection.

### Story 1: Kaggle Setup, GPU, Dependencies, and Data Loading

Configure the Kaggle environment, enable GPU acceleration, install dependencies, and load the required emotion detection dataset.

### Story 2: Data Preprocessing and Tokenization

Clean and preprocess the text dataset and perform tokenization to prepare the data for model training.

### Story 3: BiLSTM Model Training

Develop and train a Bidirectional Long Short-Term Memory model for classifying learner emotions.

### Story 4: Domain-Adaptive Fine-Tuning

Fine-tune the emotion detection model using education-related text data to improve its performance in learning environments.

### Story 5: BERT Model Fine-Tuning

Fine-tune the BERT transformer model for accurate learner emotion classification.

### Story 6: Model Export and Local Integration

Export the trained models and integrate them into the local Emotion Detection and Learning Support Engine application.

---

## Epic 3: Core Emotion Detection Pipeline Development

This phase focuses on developing the main emotion analysis and prediction system.

### Story 1: Text Preprocessing and Keyword Enhancement

Clean learner input text and enhance emotion detection using emotion-related keywords.

### Story 2: BiLSTM Classifier

Implement the BiLSTM emotion classifier using a five-class Softmax output.

The supported emotions are:

- Bored
- Confident
- Confused
- Curious
- Frustrated

### Story 3: BERT Classifier with Class Weighting and Keyword Adjustments

Implement the BERT classifier and improve predictions using class weighting and keyword-based adjustments.

### Story 4: Mixed Emotion Detection

Detect a secondary emotion when its prediction score meets the required threshold.

This allows the application to identify mixed emotions experienced by learners.

### Story 5: Unified Prediction Schema

Create a common prediction format for both BiLSTM and BERT models to simplify model comparison and application integration.

### Story 6: CSV Persistence and Cached Model Loading

Store emotion analysis results in CSV files for analytics and reporting.

Implement cached model loading to improve application performance and avoid repeatedly loading models.

---

## Epic 4: AI-Powered Guidance and Regeneration Engine

This phase integrates Generative AI with the emotion detection system to provide personalized learning support.

### Story 1: Capture Field and Problem Context for Prompt Generation

Collect the learner's selected academic field and problem description to create meaningful prompts for AI response generation.

### Story 2: Generate Empathetic and Context-Aware AI Responses

Use Gemini AI to generate personalized, supportive, and context-aware learning responses based on the learner's detected emotions and academic difficulties.

### Story 3: Response Regeneration and Synchronization Mechanism

Allow learners to regenerate AI responses while maintaining synchronization between the emotion analysis and generated learning support.

### Story 4: Session History Management and CSV Logging

Maintain user interaction history and store relevant emotion analysis and AI response information for analytics and reporting.

---

## Epic 5: Streamlit UI Implementation

This phase focuses on creating the interactive web-based user interface of the application.

### Story 1: Responsive Layout and Session State Management

Develop a responsive Streamlit interface and use session state management to maintain application data during user interactions.

### Story 2: Emotion Analysis, Model Comparison, and Visualization Components

Create user interface components for:

- Emotion detection
- Confidence score display
- BiLSTM and BERT model comparison
- Emotion score visualization
- AI-generated learning responses

### Story 3: Form Controls, Validation, and Error Handling

Implement input forms, data validation, exception handling, and meaningful error messages.

### Story 4: Analytics Dashboard and Interactive Charts

Develop an analytics dashboard to display emotion trends, prediction statistics, model performance, and other useful educational insights.

---

## Epic 6: User Interaction

The final phase focuses on testing the complete application and preparing it for deployment.

### Story 1: Validate UI Flow End-to-End

Test the complete user journey, including:

- User input
- Emotion detection
- Model prediction
- Mixed emotion analysis
- AI response generation
- Session history
- Analytics

### Story 2: Optimization and Deployment Readiness

Optimize application performance, verify dependencies, test model loading, improve error handling, and prepare the application for cloud deployment.

---

## Complete Project Flow

The overall project development flow is:

1. Configure the development environment.
2. Install all required dependencies.
3. Configure the Gemini API.
4. Prepare datasets and model directories.
5. Train the BiLSTM model.
6. Fine-tune the BERT model.
7. Export and integrate the trained models.
8. Develop the core emotion detection pipeline.
9. Implement mixed-emotion detection.
10. Integrate Gemini AI for personalized learning support.
11. Implement session history and CSV logging.
12. Develop the Streamlit user interface.
13. Create the analytics dashboard.
14. Perform end-to-end testing.
15. Optimize the application.
16. Prepare the project for deployment.

## Conclusion

The Emotion Detection and Learning Support Engine follows a structured six-epic development workflow. Each phase contributes to building a complete AI-powered educational application capable of detecting learner emotions and providing personalized, empathetic, and context-aware learning assistance.

The structured workflow ensures proper development, model integration, testing, analytics, user interaction, and deployment readiness.
