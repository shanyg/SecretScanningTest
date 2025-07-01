// This file contains dummy configuration with fake secrets for testing.

const config = {
  api: {
    // Dummy JWT-like Bearer Token
    bearerToken: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DUMMYJWTSIGNATUREForTestingOnly1234567890abcdef",
    // Dummy JWT-like Bearer Token 2
    bearerToken2: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DUMMYJWTSIGNATUREForTestingOnly1234567890abcdef",
    // Dummy Slack Bot Token
    slackBotToken: "xoxb-1234567890-DUMMYSlackBotToken1234567890abc",
  },
  database: {
    host: "db.example.com",
    user: "app_user",
    // Dummy MySQL Password
    password: "DUMMYMySQLPasswordSecure123!",
    dbName: "production_db",
  },
  thirdParty: {
    // Another dummy Google Cloud API Key (repeated intentionally)
    googleMapsApiKey: "AIzaSyA_AnotherDUMMYGoogleKeyForMaps_1234567",
    // Dummy Firebase Web API Key
    firebaseApiKey: "AIzaSyB_DUMMYFirebaseWebAppKey_1234567890",
  },
  internal: {
    // Dummy generic internal secret key
    internalSecretKey: "DUMMY_INTERNAL_APP_SECRET_KEY_987654321_XYZ",
  },
};

export default config;
