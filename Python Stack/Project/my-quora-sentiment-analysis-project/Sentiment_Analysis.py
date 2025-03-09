import time
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Quora review links
quora_links = [
    "https://www.quora.com/What-is-your-review-of-Rungta-College-of-Engineering-and-Technology-Bhilai",
    "https://www.quora.com/Whats-your-review-about-the-Rungta-College-of-Engineering-and-Technology-Bhilai",
    "https://www.quora.com/What-are-the-benefits-of-studying-at-RSR-Rungta-College-of-Information-Technology-in-Bhilai"
]

# Set up Selenium WebDriver
def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

# Function to scrape Quora reviews
def scrape_quora_reviews():
    driver = setup_driver()
    all_reviews = []
    seen_reviews = set()  # To track and remove duplicates

    for url in quora_links:
        print(f"Scraping: {url}")
        driver.get(url)
        time.sleep(5)  # Allow page to load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        answers = soup.find_all("div", class_="q-text")  # Adjust class if needed

        for ans in answers:
            review_text = ans.get_text(strip=True)
            if len(review_text) > 50 and review_text not in seen_reviews:  # Avoid short/irrelevant text and duplicates
                sentiment = analyze_sentiment_vader(review_text)
                all_reviews.append({"Review": review_text, "Sentiment": sentiment})
                seen_reviews.add(review_text)  # Add the review to the set

    driver.quit()
    return all_reviews[:50]  # Limit to 50 responses

# Function to analyze sentiment using VADER
def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)["compound"]
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

# Function to create the Tkinter UI
def create_ui(reviews, sentiment_percentages):
    window = tk.Tk()
    window.title("Sentiment Analysis of Reviews")
    window.geometry("1024x720")  # Set the window size to 1024x720

    # Sentiment Summary Section
    sentiment_frame = tk.Frame(window)
    sentiment_frame.pack(pady=20)

    sentiment_label = tk.Label(sentiment_frame, text="Sentiment Analysis Summary", font=("Arial", 18))
    sentiment_label.grid(row=0, column=0, pady=5)

    sentiment_text = f"Positive: {sentiment_percentages['Positive']:.2f}%\n"
    sentiment_text += f"Negative: {sentiment_percentages['Negative']:.2f}%\n"
    sentiment_text += f"Neutral: {sentiment_percentages['Neutral']:.2f}%"

    sentiment_display = tk.Label(sentiment_frame, text=sentiment_text, font=("Arial", 16))
    sentiment_display.grid(row=1, column=0, pady=5)

    # Reviews Section (Tabular View)
    reviews_frame = tk.Frame(window)
    reviews_frame.pack(pady=20)

    reviews_label = tk.Label(reviews_frame, text="Reviews", font=("Arial", 18))
    reviews_label.grid(row=0, column=0, pady=5)

    # Set up the Treeview for displaying reviews in a tabular form
    tree = ttk.Treeview(reviews_frame, columns=("Review", "Sentiment"), show="headings", height=15)
    tree.grid(row=1, column=0, pady=5, padx=20)

    # Define columns headers
    tree.heading("Review", text="Review")
    tree.heading("Sentiment", text="Sentiment")

    # Set column widths
    tree.column("Review", width=650)
    tree.column("Sentiment", width=150)

    # Insert reviews into the Treeview
    for review in reviews:
        sentiment = review["Sentiment"]
        # Add color coding based on sentiment
        if sentiment == "Positive":
            tree.insert("", "end", values=(review["Review"][:200] + "...", sentiment), tags=("positive",))
        elif sentiment == "Negative":
            tree.insert("", "end", values=(review["Review"][:200] + "...", sentiment), tags=("negative",))
        else:
            tree.insert("", "end", values=(review["Review"][:200] + "...", sentiment), tags=("neutral",))

    # Define styles for color coding
    style = ttk.Style()
    style.configure("positive", background="lightgreen")
    style.configure("negative", background="lightcoral")
    style.configure("neutral", background="lightgray")

    # Start the Tkinter main loop
    window.mainloop()

# Function to start the scraping and UI creation
def start_scraping_and_ui():
    reviews = scrape_quora_reviews()

    # Count sentiment occurrences
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for review in reviews:
        sentiment_counts[review["Sentiment"]] += 1

    total_reviews = len(reviews)
    print(f"Total Reviews Analyzed: {total_reviews}\n")

    # Calculate sentiment percentages
    sentiment_percentages = {}
    for sentiment, count in sentiment_counts.items():
        percentage = (count / total_reviews) * 100 if total_reviews > 0 else 0
        sentiment_percentages[sentiment] = percentage

    # Print sentiment summary
    print("Sentiment Analysis Summary:")
    for sentiment, percentage in sentiment_percentages.items():
        print(f"{sentiment}: {percentage:.2f}%")
    print("\n")

    # Create the Tkinter UI with reviews
    create_ui(reviews, sentiment_percentages)

# Main execution
if __name__ == "__main__":
    # Create initial window with button
    window = tk.Tk()
    window.title("Sentiment Analysis - Quora Reviews")
    window.geometry("1024x720")  # Set the window size to 1024x720

    # Create "Quora" button to start scraping
    quora_button = tk.Button(window, text="Start Quora Review Scraping", command=start_scraping_and_ui, font=("Arial", 18), bg="blue", fg="white")
    quora_button.pack(pady=40)

    # Run the Tkinter main loop
    window.mainloop()
