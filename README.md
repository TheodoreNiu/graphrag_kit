# GraphRAG Kit

## Requirements

- Ubuntu 24
    - [Azure Virtual Machines](https://portal.azure.com/#browse/Microsoft.Compute%2FVirtualMachines)
- Docker & Docker Compose
    - [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

## Set Env

Copy and set your `env`

```bash
cp .env.example .env
```

Set up your env variables.

## Start App

```bash
bash start.sh
```

## Deploy

Before deploy apps, you need `az login`

### Deploy Test App

```bash
bash deploy_test.sh
```

### Deploy API

```bash
bash deploy_api.sh
```
