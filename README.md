# Event Trigger Platform

## Description
This is a backend application designed to help customers manage and trigger events based on certain conditions. The app supports the creation of two types of triggers:

1. **Scheduled Trigger:** Executes at a specific time or at a fixed interval (one-time or recurring).
2. **API Trigger:** Executes based on an API call with a predefined JSON schema and values.

Users can also test triggers manually, manage triggers (CRUD operations), and view event logs with details. Event logs are maintained in an active state for 2 hours, archived for 46 hours, and deleted after 48 hours.

---

## Features

- Create, edit, delete, and view triggers.
- Manual testing of triggers.
- Event logs with aggregation and individual views.
- Event retention and archival system.
- Containerized deployment using Docker.
- Minimal Swagger/OpenAPI UI for trigger management.
- Local caching for frequent event log queries.
- Deployed solution on a free-tier cloud platform.

---

## Assumptions

- Scheduled triggers will fire only once based on user selection.
- API triggers will execute once for testing purposes.
- Retention and archival times are fixed (active for 2 hours, archived for 46 hours).
- JSON payload for API triggers will have a flat schema.
- Authentication is minimal and implemented via a simple token.

---

## Tech Stack

- **Language:** Python
- **Framework:** Flask/FastAPI
- **Database:** PostgreSQL
- **Caching:** Redis
- **Containerization:** Docker
- **Deployment:** Render/Heroku/AWS Free Tier

---

## API Endpoints

### Trigger Management

1. **Create Trigger**
   - `POST /triggers`
   - Request:
     ```json
     {
       "type": "scheduled",
       "schedule": {
         "interval": 30,
         "unit": "minutes",
         "is_recurring": false
       }
     }
     ```
     OR
     ```json
     {
       "type": "api",
       "payload": {"key": "value"}
     }
     ```
   - Response:
     ```json
     {
       "id": "trigger-id",
       "status": "created"
     }
     ```

2. **List Triggers**
   - `GET /triggers`
   - Response:
     ```json
     [
       {
         "id": "trigger-id",
         "type": "scheduled",
         "details": { ... },
         "created_at": "timestamp"
       }
     ]
     ```

3. **Edit Trigger**
   - `PUT /triggers/{id}`

4. **Delete Trigger**
   - `DELETE /triggers/{id}`

### Manual Testing

1. **Test Trigger**
   - `POST /triggers/test`
   - Response:
     ```json
     {
       "id": "test-id",
       "status": "success"
     }
     ```

### Event Logs

1. **Get Active Logs**
   - `GET /logs?state=active`

2. **Get Archived Logs**
   - `GET /logs?state=archived`

3. **Aggregate Logs**
   - `GET /logs/aggregate`

---

## Deployment

The application is deployed on [Cloud Provider Link]. Access it here: [Deployed URL]

---

## Local Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Build and run using Docker:
   ```bash
   docker-compose up --build
   ```

3. Access Swagger UI:
   - Navigate to `http://localhost:8000/docs` (for FastAPI) or `http://localhost:5000/swagger` (for Flask).

4. Environment variables:
   - Copy `.env.example` to `.env` and set the following:
     ```
     DATABASE_URL=<database-url>
     REDIS_URL=<redis-url>
     ```

---

## Cost Analysis

- **Cloud Hosting:** Free tier of Render/Heroku/AWS
- **Database:** PostgreSQL free tier
- **Cache:** Redis free tier

Estimated monthly cost for 24x7 operations: **$0** (using free-tier services)

---

## Testing

1. Run test suite:
   ```bash
   pytest
   ```
2. Sample test cases cover:
   - Trigger creation and deletion.
   - Scheduled and API trigger execution.
   - Event log retention and archival.

---

## Credits

- OpenAI ChatGPT for initial brainstorming.
- [Redis Documentation](https://redis.io/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)

---

## Submission

- **GitHub Repository:** [Link to Repo]
- **Deployed Solution:** [Link to Deployed App]
- **Contact:** shobhit@segwise.ai

