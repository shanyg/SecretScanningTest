import os

# --- API Keys & Tokens ---
# Dummy GitHub Token (should trigger detection)
GITHUB_TOKEN = "ghp_DUMMYGitHubTokenForTesting1234567890abcdef"

# Dummy AWS Access Key ID and Secret Access Key
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Dummy Google Cloud API Key
GOOGLE_API_KEY = "AIzaSyA_DUMMYGoogleCloudAPIKeyForTesting123456"

# Dummy Stripe API Key (live mode prefix)
STRIPE_SECRET_KEY = "sk_live_DUMMYStripeSecretKey1234567890abcde"

# Dummy Twilio Auth Token
TWILIO_AUTH_TOKEN = "your_dummy_twilio_auth_token_here_1234567890"

# --- Database Credentials ---
# Dummy PostgreSQL connection string with password
DB_CONNECTION_STRING = "postgresql://user:DUMMYDBPassword@localhost:5432/mydb"

# --- Generic Passwords ---
# Low entropy password
ADMIN_PASSWORD_LOW_ENTROPY = "password123"
# High entropy (dummy) password
APP_SECRET_PASSWORD = "MyS3cr3tDummY!P@ssw0rd_aBcDeF"

# Barb token
barbslack = "xoxb-1234567890-DUMMYSlackBotToken1234567890abc"

def get_config():
    """Retrieves application configuration."""
    config = {
        "github_token": GITHUB_TOKEN,
        "aws_key": AWS_ACCESS_KEY_ID,
        "aws_secret": AWS_SECRET_ACCESS_KEY,
        "db_conn": DB_CONNECTION_STRING,
        "admin_pass": ADMIN_PASSWORD_LOW_ENTROPY
    }
    return config

if __name__ == "__main__":
    print("Application started.")
    # Example of accessing a "secret"
    print(f"Loaded GitHub Token (dummy): {os.getenv('GITHUB_TOKEN_ENV', 'Not set in env')}")
    print(f"Hardcoded Stripe Key (dummy): {STRIPE_SECRET_KEY}")
