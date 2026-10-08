from datetime import datetime, timedelta

# --- Configuration ---
# Simulate the current date for predictable output.
# Change this date to see how reminders would behave on different days.
CURRENT_SIMULATION_DATE = datetime(2023, 3, 10)

# --- Data Store (simulated bookmarks) ---
# Each 'bookmark' is a dictionary containing details about the item to remember.
# 'last_reminded_date' tracks when it was last brought to the user's attention.
# 'reminder_interval_days' defines how frequently the user should be reminded.
bookmarks = [
    {
        "id": 1,
        "title": "Python Asyncio Tutorial",
        "url": "https://example.com/asyncio",
        "added_date": datetime(2023, 1, 10),
        "last_reminded_date": datetime(2023, 3, 1), # Last reminded 9 days ago (relative to CURRENT_SIMULATION_DATE)
        "reminder_interval_days": 7 # Should be reminded every 7 days
    },
    {
        "id": 2,
        "title": "Machine Learning Basics",
        "url": "https://example.com/ml-basics",
        "added_date": datetime(2023, 1, 15),
        "last_reminded_date": datetime(2023, 2, 15), # Last reminded 23 days ago
        "reminder_interval_days": 14 # Should be reminded every 14 days
    },
    {
        "id": 3,
        "title": "CSS Flexbox Guide",
        "url": "https://example.com/flexbox",
        "added_date": datetime(2023, 2, 1),
        "last_reminded_date": datetime(2023, 3, 5), # Last reminded 5 days ago
        "reminder_interval_days": 30 # Should be reminded every 30 days
    },
    {
        "id": 4,
        "title": "New JavaScript Features",
        "url": "https://example.com/js-new",
        "added_date": datetime(2023, 3, 8),
        "last_reminded_date": datetime(2023, 3, 8), # Added recently, not due yet
        "reminder_interval_days": 7
    }
]

def check_for_reminders(current_date: datetime, bookmarks_list: list) -> None:
    """
    Checks the list of bookmarks and prints reminders for items that are due.
    Updates the 'last_reminded_date' for items that are reminded to schedule
    their next reminder.
    """
    print(f"--- Running reminder check for {current_date.strftime('%Y-%m-%d')} ---")
    reminders_found = False

    for bookmark in bookmarks_list:
        # Calculate the date when the next reminder for this item was due.
        # This is the core logic for determining if a reminder is needed.
        next_due_date = bookmark["last_reminded_date"] + timedelta(days=bookmark["reminder_interval_days"])

        # If the current simulation date is on or after the next due date,
        # then it's time to remind the user about this item.
        if current_date >= next_due_date:
            reminders_found = True
            print(f"\n🔔 REMINDER: It's time to revisit '{bookmark['title']}'!")
            print(f"   URL: {bookmark['url']}")
            print(f"   Last reminded: {bookmark['last_reminded_date'].strftime('%Y-%m-%d')}")
            print(f"   Interval: {bookmark['reminder_interval_days']} days")
            
            # Update 'last_reminded_date' to the current simulation date.
            # This simulates the bot acknowledging the reminder and resetting the timer
            # for the next reminder cycle.
            bookmark["last_reminded_date"] = current_date
            print(f"   Next reminder due: {(current_date + timedelta(days=bookmark['reminder_interval_days'])).strftime('%Y-%m-%d')}")
            print("-" * 30)

    if not reminders_found:
        print("\nNo reminders due today. Keep up the good work!")

# --- Main execution ---
if __name__ == "__main__":
    print("Simulating a Smart Reminder Bot...")
    check_for_reminders(CURRENT_SIMULATION_DATE, bookmarks)

    # Optional: Display the updated state of bookmarks after the check
    # This shows how 'last_reminded_date' would be persisted in a real application.
    print("\n--- Updated bookmark states (for demonstration) ---")
    for bookmark in bookmarks:
        print(f"ID: {bookmark['id']}, Title: '{bookmark['title']}', Last Reminded: {bookmark['last_reminded_date'].strftime('%Y-%m-%d')}")
