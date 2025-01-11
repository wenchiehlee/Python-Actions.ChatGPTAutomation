from chatgpt_automation import ChatGPTAutomation

if __name__ == "__main__":
    # Initialize the ChatGPTAutomation instance
    automation = ChatGPTAutomation()

    try:
        # Test: Send a prompt to ChatGPT
        test_prompt = "Hello, ChatGPT!"
        automation.send_prompt_to_chatgpt(test_prompt)

        # Test: Return last response
        last_response = automation.return_last_response()
        print(f"Last response from ChatGPT: {last_response}")
    finally:
        # Clean up resources
        automation.quit()
