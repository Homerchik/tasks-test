## Descripion
This is just simple repo, showing basic autotests to test simple todo application, provided as docker image, with API

#### Endpoints
The only entity here is TODO  represented by a structure with the following three fields:
* `id` — an unsigned 64-bit identifier
* `text` - description of TODO
* `completed` - whether the todo is completed or not

##### `GET /todos`

Get a JSON list of TODOs.

Available query parameters:
* `offset` — how many TODOs should be skipped
* `limit` - the maximum number of TODOs to be returned

##### `POST /todos`

Create a new TODO. This endpoint expects the whole `TODO` structure as the request body.

##### `PUT /todos/:id`

Update an existing TODO with the provided one.

##### `DELETE /todos/:id`

Delete an existing TODO.

## Functional Tests
Tests could be run simply by running `run.sh` and `pytest` afterwards
`run.sh` runs docker image with todo-app in it

## Load scripts
`run_load.sh` runs todo-app and yandex-tank images and start shooting.
Ammo for tank can be generated using `load.ammo` python script. Additional config can be performed 
using `configs/tank.yaml`. Right now yandex-tank pushes all metrics to `overload.yandex.net`
service for building graphs.

## Tests configuration
Tests can be configurated using `configs/config.yaml`, but normally you 
it shouldn't be necessary for you to change anything there.

