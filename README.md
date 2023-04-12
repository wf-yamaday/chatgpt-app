# chatgpt-app

[![CI - Lint](https://github.com/wf-yamaday/chatgpt-app/actions/workflows/ci.yml/badge.svg)](https://github.com/wf-yamaday/chatgpt-app/actions/workflows/ci.yml)
[![CI - Docker Image Build](https://github.com/wf-yamaday/chatgpt-app/actions/workflows/ci-build.yml/badge.svg)](https://github.com/wf-yamaday/chatgpt-app/actions/workflows/ci-build.yml)

This is a simple web application that wraps OpenAI's Chat API.

The application is designed to be simple and can be used as a starting point for customization.
For example, this application can be used to create your original web application.

## Usage

### 1. Get an API key

Get an API key from the OpenAI website. Refer to OpenAI's documentation for instructions on obtaining an API key.

> https://platform.openai.com/account/api-keys

### 2. Pull Docker Image

Pull the Docker image with the following command.

```sh
docker pull ghcr.io/wf-yamaday/gpt-app:latest
```

### 3. Start the application locally

Run the following commands to start the application locally:

```sh
docker run --name gptapp -p 8000:8000 -e OPENAI_API_KEY=<YOUR_OPENAI_API_KEY> ghcr.io/wf-yamaday/gpt-app:latest
```

You can use the application by accessing the following URL:

> http://localhost:8000

## License

This project is [Apache License 2.0](https://github.com/wf-yamaday/chatgpt-app/blob/main/LICENSE) licensed.
