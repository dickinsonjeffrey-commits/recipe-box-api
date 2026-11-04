# Security baseline

- 2026-11-04: Anonymous **GET /recipes** → 200 OK, returns full list of recipes (no authentication, any requester can read all recipes).
- 2026-11-04: Anonymous **GET /recipes/1** → 200 OK, returns full details of recipe 1 (no authentication, any requester can read this recipe).
- 2026-11-04: Anonymous **DELETE /recipes/1** → 204 NO CONTENT, recipe 1 is removed (no authentication, any requester can delete this recipe).