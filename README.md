# datalens-patch
ui customize for datalens

- Клонировать datalens-patch
- Перейти в datalens-patch
- Клоинровать остальные сервисы datalens в datalens-patch
- Построить образы docker
- - Build datalens-backend
  - - ./docker_build/run-project-bake dl_control_api --set "dl_control_api.tags=datalens-control-api:local"
  - - ./docker_build/run-project-bake dl_data_api --set "dl_data_api.tags=datalens-data-api:local"
- - Build datalens-ui + datalens-ui-api
  - - docker build .
- - Build datalens-us
  - - docker build -t tpz_datalens-us .
- - Build datalens-auth
  - - docker build -t tpz_datalens-auth .
- - Build datalens-meta-manager
  - - docker build -t tpz_datalens-meta-manager .


## 01. Override assets, logo and styles

### Prerequisites

Docker

- [macOS](https://docs.docker.com/desktop/install/mac-install/)
- [Linux](https://docs.docker.com/engine/install/)
- [Windows](https://docs.docker.com/desktop/install/windows-install/)

Git Version Control System

- [Git](https://git-scm.com/downloads)

\* Bash compatible shell for Windows
- [Git Bash](https://git-scm.com/downloads)

### 1. Clone additional repos

- Main DataLens repo with docker-compose.yaml file

`git clone git@github.com:datalens-tech/datalens.git`

- UI repo with sources of client side DataLens part

`git clone git@github.com:datalens-tech/datalens-ui.git`

### 2. Check assets for override

Folder `./patch` contains the same directory and files structure as UI project with custom overrides

### 3. Check new Dockerfile 

New `Dockerfile` contains copy of default sources from `datalens-ui` folder with replaced copies `./path` folder assets

### 4. Extend main docker-compose.yaml file

All services from main compose file except `datalens-ui` were extended

Service `datalens-ui` for ui is build from new `Dockerfile` with resource overriding

### 5. Build new datalens-ui container

`docker build datalens-ui`

### 6. Pull US and backend docker images

`docker compose pull`

### 7. Up all compose stack

`docker compose up --build -d`

### 8. Open DataLens

Open your custom DataLens by path: [http://localhost:8080](http://localhost:8080)
