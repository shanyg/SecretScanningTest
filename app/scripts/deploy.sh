#!/bin/bash

echo "Starting dummy deployment script..."

# --- Environment variables passed during deployment (dummy) ---
export DOCKER_HUB_PASSWORD="DUMMY_DockerHub_Password_123!"
export KUBERNETES_API_TOKEN="k8s_DUMMY_API_TOKEN_FOR_CLUSTER_ACCESS_XYZABC123"

# --- Credentials embedded directly (bad practice, good for testing) ---
SSH_USER="deploy_user"
# Dummy SSH password (low entropy)
SSH_PASSWORD="deploy_pass"

# Dummy Azure CLI Service Principal Password
AZURE_SP_PASSWORD="DUMMY_Azure_Service_Principal_Password_Highly_Complex!@#$123"

# Attempting to echo a dummy private key (simulating accidental leakage)
echo "---BEGIN DUMMY RSA PRIVATE KEY---"
echo "MIIEpgIBAAKCAQEA0e9hR1DUMMYRSAPrivateKeyForTestingPurposesONLYp2yJ"
echo "---END DUMMY RSA PRIVATE KEY---"

# Dummy webhook URL
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/T00000000/B00000000/DUMMYSlackWebhookToken1234567890"

echo "Dummy deployment script finished."
