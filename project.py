import streamlit as st
import time
import re
from collections import Counter


def get_word_count(text):
    words = text.split()
    return len(words)


def get_vowel_count(text):
    vowels = re.findall(r'[aeiouAEIOU]', text)
    return len(vowels)


def get_reversed_text(text):
    return text[::-1]


def get_repeated_letters(text):
    letter_counts = Counter(text)
    repeated = {char: count for char, count in letter_counts.items() if count > 1 and char.isalpha()}
    return repeated


st.title("📝 String Analyzer App")

text = st.text_area("Enter a string for analysis:")

if st.button("Start"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        start_time = time.time()


        word_count = get_word_count(text)
        vowel_count = get_vowel_count(text)
        reversed_text = get_reversed_text(text)
        repeated_letters = get_repeated_letters(text)

        end_time = time.time()
        execution_time = end_time - start_time

        
        st.subheader("📊 Analysis Result:")
        st.write(f"**Word Count**: {word_count}")
        st.write(f"**Vowel Count**: {vowel_count}")
        st.write(f"**Reversed String**: `{reversed_text}`")
        st.write(f"**Repeated Letters**: {repeated_letters}")
        st.write(f"**Analyzer Execution Time**: {execution_time:.6f} seconds")
