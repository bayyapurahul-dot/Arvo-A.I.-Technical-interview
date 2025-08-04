import re
from dotenv import set_key
import os

# Supported keywords
APP_TYPES = ['flask', 'django', 'node.js', 'nodejs', 'express']
CLOUD_PROVIDERS = ['aws', 'azure', 'gcp', 'google cloud']

def parse_deployment_request(text):
    text = text.lower()

    app_type = next((app for app in APP_TYPES if app in text), 'unknown')
    cloud = next((c for c in CLOUD_PROVIDERS if c in text), 'unknown')

    return {
        'app_type': app_type,
        'cloud_provider': cloud
    }

def write_to_env(parsed_data, env_path=".env"):
    # Create or update .env
    with open(env_path, 'w') as f:
        f.write(f'APP_TYPE={parsed_data["app_type"]}\n')
        f.write(f'CLOUD_PROVIDER={parsed_data["cloud_provider"]}\n')

if __name__ == "__main__":
    user_input = input("Enter deployment instruction (e.g., Deploy my flask app on AWS):\n> ")
    result = parse_deployment_request(user_input)
    write_to_env(result)
    print(f"Parsed and saved to .env: {result}")
