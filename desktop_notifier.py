import plyer
import time
import datetime

def show_notification(title, message, scheduled_time, timeout):
    current_time = datetime.datetime.now()
    if current_time >= scheduled_time:
        plyer.notification.notify(
            title=title,
            message=message,
            app_name='Desktop Notifier',
            timeout=timeout
        )

def snooze(interval):
    print(f"Snoozing for {interval} minutes.")
    time.sleep(interval * 60)

if __name__ == '__main__':
    notifications = []
    while True:
        option = input("Enter 'add' to add a notification, 'show' to show notifications, 'exit' to exit: ")
        if option == 'add':
            title = input("Enter the title of the notification: ")
            message = input("Enter the message of the notification: ")
            year = int(input("Enter the year for the notification: "))
            month = int(input("Enter the month (1-12) for the notification: "))
            day = int(input("Enter the day for the notification: "))
            hour = int(input("Enter the hour (0-23) for the notification: "))
            minute = int(input("Enter the minute (0-59) for the notification: "))
            scheduled_time = datetime.datetime(year, month, day, hour, minute)
            timeout = int(input("Enter the timeout (in seconds) for the notification: "))
            notifications.append((title, message, scheduled_time, timeout))
        elif option == 'show':
            for notification in notifications:
                show_notification(*notification)
                response = input("Enter 'snooze' to snooze the notifications for a specific duration, 'off' to turn off the notifications for a specific duration, 'next' to show the next notification: ")
                if response == 'snooze':
                    interval = int(input("Enter the snooze interval (in minutes): "))
                    snooze(interval)
                elif response == 'off':
                    interval = int(input("Enter the duration (in minutes) for which notifications should be turned off: "))
                    snooze(interval)
                elif response == 'next':
                    continue
                else:
                    print("Invalid option. Terminating the program.")
                    break
        elif option == 'exit':
            break
        else:
            print("Invalid option. Please try again.")
    print("Goodbye!")