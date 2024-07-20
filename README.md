# English to Spanish Translator with Streamlit

This project demonstrates how to build an interactive English-to-Spanish translation app using a fine-tuned MarianMT model and the Streamlit framework.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Evaluation](#evaluation)
- [Future Work](#future-work)
- [License](#license)

## Description

This Streamlit app provides a simple yet effective interface for translating English text into Spanish. It leverages a state-of-the-art MarianMT model fine-tuned on a large parallel corpus of English-Spanish text. The app features a progress bar to indicate translation progress and handles potential errors gracefully.

## Features

- **Real-time Translation:** Translate English text to Spanish instantly.
- **Progress Bar:** Visual feedback during translation.
- **Error Handling:** Gracefully handles errors during translation.
- **User-friendly Interface:** Easy-to-use Streamlit interface.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/WizKnight/English-to-Spanish-Translation-APP.git](https://github.com/WizKnight/English-to-Spanish-Translation-APP.git)

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

## Usage

1. **Run the App:**
   ```bash
   streamlit run main.py

2. **Enter Text:** Type or paste your English text into the text area.
3. **Click Translate:** Press the "Translate" button to initiate translation.
4. **View Translation:** The translated Spanish text will appear below.

## Model Details

* **Architecture:** MarianMT (Helsinki-NLP/opus-mt-en-es)
* **Fine-tuning:** The model has been fine-tuned on a large parallel corpus of English-Spanish text from the Hugging Face Datasets library.
* **Framework:** PyTorch and Transformers (Hugging Face)

## Evaluation

* The model was evaluated using the **BLEU** (Bilingual Evaluation Understudy) score, achieving a score of **22.96** on a test dataset.
* Additional human evaluation was conducted to assess translation fluency and adequacy.

## Future Work

* Add support for batch translation.
* Integrate a download option for translated text.
* Explore other model architectures like T5.
* Incorporate user feedback for continuous improvement.

## Liscense

This project is licensed under the Apache 2.0 License.