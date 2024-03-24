import json
from playwright.sync_api import sync_playwright

def return_response(status_code, json_body):
    response = {
        "statusCode": status_code,
        "body": json.dumps(json_body)
    }
    return response

def lambda_handler(event, context):
    try:
        with sync_playwright as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.goto('https://www.motherfuckingwebsite.com')
        return return_response(200, {
                "message": "Hello from Lambda!"
            })
    except Exception as e:
        return return_response(500, {"message": str(e)})