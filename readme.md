# Event Management API Documentation
The Event Management API is a Django-based web service that allows users to manage events, book tickets, and view event details. It provides endpoints for both admin and regular users to perform various operations related to events and tickets.

# Base URL
The base URL for accessing the API is: http://localhost:8000. This is not yet live hosted so try the localhost version

# API Endpoints

## Events
GET /api/events: Retrieve a list of all events.
POST /api/events: Create a new event.
GET /api/events/{event_id}: Retrieve details of a specific event.
PUT /api/events/{event_id}: Update details of a specific event.
DELETE /api/events/{event_id}: Delete a specific event.

## Tickets
GET /api/tickets: Retrieve a list of all tickets.
POST /api/tickets: Create a new ticket for an event.
GET /api/tickets/{ticket_id}: Retrieve details of a specific ticket.
PUT /api/tickets/{ticket_id}: Update details of a specific ticket.
DELETE /api/tickets/{ticket_id}: Delete a specific ticket.
## User Authentication
POST /api/auth/register: Register a new user.
POST /api/auth/login: Log in with user credentials and obtain an access token.
POST /api/auth/logout: Log out the authenticated user.
## Admin Operations
POST /api/admin/events: Create a new event (admin only).
PUT /api/admin/events/{event_id}: Update details of a specific event (admin only).
GET /api/admin/events/{event_id}/summary: Retrieve a summary of a specific event (admin only).
## Authentication and Authorization
User registration is required to access certain endpoints.
User authentication is performed using JWT (JSON Web Tokens) for secure API access.
Admin privileges are required for admin-specific operations.
Request and Response Formats
Request data should be sent in JSON format.
Response data is returned in JSON format.
