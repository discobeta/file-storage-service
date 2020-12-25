## File storage API service
###### API service for file storage with token authentication, using Python 3 FastAPI deployed on Digital Ocean using a Kubernetes deployment.

### Endpoints
The service features the two endpoints that allow saving a file as well as serving files.

#### Saving a new file
Saving a new file via `POST` request at path `/create`

#### Serving files
Serving files via `GET` request at path `/domain/path` or `/id/path`

### Configuration
Configuration can be found at `app.lib.config`. The file contains the authentication dictionary.

### Models
Models are defined in `app.models`. In addition to the expected routes, there is a health_check route that is used by Kubernetes to determine when the POD is availble. The other routes that are defined in `app.routes.storage` are responsible for saving and serving files.

### Routes
Routes are defined in `app.routes`. In addition to the expected routes, there is a health_check route that is used by Kubernetes to determine when the POD is availble. The other routes that are defined in `app.routes.storage` are responsible for saving and serving files.

### Authentication
A dictionary containing authentication data is used to verify API requests. The configuration can be found in the `app.lib.config` file. This work was stopped short of encrypting the dictionary in memory of each worker.

### Docs

http://localhost:6900/docs#/


