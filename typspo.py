import time

def typing_speed_calculator():
    # Step 1: Provide a sample text
    sample_text = (
        "The quick brown fox jumps over the lazy dog. "
        "Practice makes perfect when it comes to typing. "
        "Keep improving your skills and speed."
    )
    print("Type the following text as quickly and accurately as you can:\n")
    print(f"---\n{sample_text}\n---")

    # Step 2: Wait for the user to start typing
    input("Press Enter when you are ready to start typing...")
    print("\nStart typing below:\n")

    # Step 3: Record the start time
    start_time = time.time()

    # Step 4: Capture the user's input
    user_input = input()

    # Step 5: Record the end time
    end_time = time.time()

    # Step 6: Calculate the typing duration
    typing_duration = end_time - start_time  # in seconds

    # Step 7: Calculate the typing speed in WPM
    word_count = len(user_input.split())  # Count words in user input
    wpm = (word_count / typing_duration) * 60  # Convert to words per minute

    # Step 8: Calculate accuracy
    sample_words = sample_text.split()
    user_words = user_input.split()
    correct_words = sum(1 for sw, uw in zip(sample_words, user_words) if sw == uw)
    accuracy = (correct_words / len(sample_words)) * 100

    # Step 9: Provide feedback
    print("\n--- Results ---")
    print(f"Time Taken: {typing_duration:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} words per minute (WPM)")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words Typed: {word_count}")
    print(f"Correct Words: {correct_words}/{len(sample_words)}")
    print("----------------")

# Run the typing speed calculator
if __name__ == "__main__":
    typing_speed_calculator()
