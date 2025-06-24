# Application Architecture Document

This document outlines the high-level architecture of our dummy application.

---

## Components

-   **Web Server:** Nginx (frontend reverse proxy)
-   **Application Server:** Python Flask (backend logic)
-   **Database:** PostgreSQL

## Configuration Notes

For **development environments**, sensitive values are loaded from `.env` files.
For **production environments**, secrets are managed via Kubernetes Secrets or AWS Secrets Manager.

### Example Database Connection String (FOR DOCUMENTATION PURPOSES ONLY - DO NOT USE IN CODE)
