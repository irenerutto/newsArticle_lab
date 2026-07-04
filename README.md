# 📰 News Article Text Analysis

A simple Python application that performs basic Natural Language Processing (NLP) tasks on a news article. The program reads text from a file, analyzes its contents, and provides useful statistics about the article.

---

## 📌 Features

The application can:

* 🔍 Count the number of times a specific word appears.
* 📊 Identify the most common word in the article.
* ✏️ Calculate the average word length.
* 📄 Count the total number of paragraphs.
* 💬 Count the total number of sentences.

---

## 🛠️ Technologies Used

* Python 3
* Regular Expressions (`re`)
* `collections.Counter`
* Pytest (Unit Testing)

---

## 📁 Project Structure

```text
.
├── .gitignore
├── pythonAssessment.py      # Main application
├── newsArticle.txt          # News article to analyze
├── test_pythonAssessment.py # Unit tests
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your computer.

### Installation

Clone the repository or download the project files.

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd <project-folder>
```

### Create a Virtual Environment (Recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

---

## ▶️ Running the Program

Run the following command:

```bash
python pythonAssessment.py
```

When prompted, enter a word you would like to search for in the article.

Example:

```text
Enter a word to search for:
apple
```

---

## 📈 Example Output

```text
Word count: 16
Most common word: the
Average word length: 5.22
Sentences: 27
Paragraphs: 19
```

---

## 🧪 Running the Tests

Run the unit tests with:

```bash
pytest -v
```

This runs the unit tests for the `count_specific_word()` and `identify_most_common_word()` functions.

---

## 📖 Learning Outcomes

This project demonstrates how to:

* Read data from a text file.
* Work with Python functions.
* Use regular expressions to process text.
* Count word frequencies with `Counter`.
* Implement loops and conditional statements.
* Write clean, modular, and reusable code.
* Test Python functions using Pytest.

---

## 📜 License

This project was created for educational purposes as part of a Python programming assignment.

---

## 👩‍💻 Author

**Irene**
