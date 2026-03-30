# cirfgdps

a geometry dash private server implementation w/ FastAPI && Vue.js. with &lt;3 by lemo &amp;&amp; yux ^^

[![CI](https://github.com/cirhalfstudio/cirfgdps/actions/workflows/ci.yml/badge.svg?branch=dev)](https://github.com/cirhalfstudio/cirfgdps/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/cirhalfstudio/cirfgdps/branch/dev/graph/badge.svg?token=R3DW8NESTH)](https://codecov.io/github/cirhalfstudio/cirfgdps)

- note: this is the beta version branch (unstable).

## features

- //@TODO

## requirements

- the only requirement to build is docker.

## setup

1. copy `.env.example` to `.env` && edit the secrets with yours
2. build for development: `docker compose -f docker-compose.dev.yml up`
3. for production: `docker compose -f docker-compose.prod.yml up`

- the client will be accessible at `http://localhost:5173` in dev mode or at `http://localhost` in prod mode
- the server will be accessible at `http://localhost:8000`

## credits

- [@svlemogames](https://github.com/svlemogames) for the frontend
- [@Wyliemaster](https://github.com/Wyliemaster) and his [GDDocs](https://wyliemaster.github.io/gddocs) for geometry dash api reference
- [@lander1x](https://github.com/lander1x) for some of the backend utils code
- [@GrujicFilipRS](https://github.com/GrujicFilipRS) for some help too
