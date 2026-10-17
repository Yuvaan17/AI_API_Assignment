import json
from google import genai


def main():
    # Read the input from the text file
    with open("text.txt", "r") as file:
        user_prompt = file.read()

    # Initialize the client and make the API call
    # Replace the text inside the quotes below with your actual API key
    client = genai.Client(api_key="AQ.Ab8RN6KjPUy-zbFOLwZpseIcXKrhzeGN-_yOb7q5PS7JGhPVKQ")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=user_prompt,
    )

    # Structure the data and save it as a JSON file
    output_data = {
        "prompt": user_prompt,
        "response": response.text
    }

    with open("llm_response.json", "w") as json_file:
        json.dump(output_data, json_file, indent=4)

    print("Success! Check the llm_response.json file in your project panel.")


if __name__ == "__main__":
    main()