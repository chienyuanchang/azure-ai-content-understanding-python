# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various types of media content—such as **documents, images, audio, and video**—transforming them into structured, organized, and searchable data.

- The samples in this repository default to the latest preview API version: **2025-05-01-preview**.
- This repository will soon provide more samples for new functionalities in Preview.2 **2025-05-01-preview**.
- As of May 2025, the **2025-05-01-preview** API version is available only in the regions documented in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).
- To access sample code for version **2024-12-01-preview**, please check out the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started

You can run the samples either in GitHub Codespaces or your local environment. For a smoother and hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

Run this repository virtually using GitHub Codespaces, which opens a web-based VS Code environment in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

After clicking the link above, follow these steps to set up the Codespace:

1. Create a new Codespace by selecting the `main` branch, your preferred region, and the 2-core machine type, as shown in the screenshot below.  
   ![Create Codespace](/docs/create-codespace/1-Create%20Codespace.png)
2. Once the Codespace is ready, open the terminal and follow the instructions in the **Configure Azure AI service resource** section to set up a valid Content Understanding resource.

### Local Environment

1. Ensure the following tools are installed:

    - [Azure Developer CLI (azd)](https://aka.ms/install-azd)
    - [Python 3.11+](https://www.python.org/downloads/)
    - [Git LFS](https://git-lfs.com/)

2. Create a new directory named `azure-ai-content-understanding-python` and clone this repository into it using the `azd` CLI:

    ```bash
    azd init -t azure-ai-content-understanding-python
    ```

    Alternatively, you can clone the repository with Git:

    ```bash
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```

    - **Important:** If you use `git clone`, make sure to install Git LFS and run `git lfs pull` to download sample files stored in the `data` directory:

      ```bash
      git lfs install
      git lfs pull
      ```

3. Set Up Dev Container Environment

    - Install the necessary tools to support dev containers:

      - **Visual Studio Code**  
        Download and install [Visual Studio Code](https://code.visualstudio.com/).

      - **Dev Containers Extension**  
        In the VS Code Extension Marketplace, install the extension named **Dev Containers**.  
        *(This extension was previously called "Remote - Containers" but has since been renamed and integrated into Dev Containers.)*

      - **Docker**  
        Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (available for Windows, macOS, and Linux).  
        Docker is required to manage and run the container environment.  
        - Start Docker and ensure it is running in the background.

    - Open the project and start the Dev Container:

      - Open the project folder in VS Code.
      - Press `F1` or `Ctrl+Shift+P`, then type and select:

        ```
        Dev Containers: Reopen in Container
        ```

        Alternatively, click the green icon in the lower-left corner of VS Code and select **Reopen in Container**.
      - VS Code will automatically detect the `.devcontainer` folder, build the development container, and install all necessary dependencies.  
      - ![How to set dev container environment](./docs/dev-container-setup.gif "Dev Container Setup")

## Configure Azure AI Service Resource

### (Option 1) Use `azd` commands to automatically create temporary resources to run samples

1. Ensure you have permission to assign roles within your Azure subscription.
2. Log in to Azure:

    ```bash
    azd auth login
    ```

    If the above does not work, try the alternate login method and follow the on-screen instructions:

    ```bash
    azd auth login --use-device-code
    ```

3. Set up the environment by following the prompts and selecting a location:

    ```bash
    azd up
    ```

### (Option 2) Manually create resources and set environment variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).
2. In your resource, go to **Access Control (IAM)** and grant yourself the **Cognitive Services User** role.  
   - This step is necessary even if you are the owner of the resource.
3. Copy `notebooks/.env.sample` to `notebooks/.env`.
4. Fill in **AZURE_AI_ENDPOINT** with the endpoint URL from your Azure AI Services instance in the Azure portal.
5. Log in to Azure:

    ```bash
    azd auth login
    ```

## Open a Jupyter Notebook and Follow Step-by-Step Guidance

Navigate to the `notebooks` directory and open the sample notebook you want to explore. Since the Dev Container (in Codespaces or your local environment) is pre-configured with the required environment, you can execute each step directly in the notebook.

Steps to get started:

1. Select a notebook of interest in the `notebooks/` directory. We recommend starting with **content_extraction.ipynb** to understand the basic concepts.  
   ![Select *.ipynb](/docs/create-codespace/2-Select%20file.ipynb.png)
2. Select the Kernel.  
   ![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)
3. Choose the Python Environment.  
   ![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)
4. Run the notebook cells.  
   ![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) designed to process and ingest content of any type—including documents, images, audio, and video—into user-defined output formats. Content Understanding offers a streamlined process for reasoning over large volumes of unstructured data, accelerating time-to-value by producing outputs that can be integrated into automation and analytical workflows.

## Samples

| File                                     | Description                                                                                                                                                                  |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [content_extraction.ipynb](notebooks/content_extraction.ipynb)               | Demonstrates how the Content Understanding API extracts semantic information from files, including OCR with tables in documents, audio transcription, and face analysis in video.      |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb)                   | Shows how to create an analyzer to extract fields from your files, such as invoice amounts in documents, people counts in images, names mentioned in audio, or summaries of videos. You can customize fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates how to efficiently evaluate conversational audio data previously transcribed with Content Understanding or Azure AI Speech. Enables cost-efficient re-analysis. This sample builds on [field_extraction.ipynb](notebooks/field_extraction.ipynb). |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb)                 | Shows how to further boost field extraction performance by training the analyzer with a few labeled samples. Note: This feature is currently available only for document scenarios.                          |
| [management.ipynb](notebooks/management.ipynb)                               | Demonstrates how to create a minimal analyzer, list all analyzers in your resource, and delete unused analyzers.                                                                                  |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb)       | Demonstrates how to enroll people’s faces from images and build a Person Directory.                                                                                                        |

## Additional Samples Using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** — This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos must comply with [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Use of third-party trademarks or logos is subject to those third parties’ policies.

* **Data Collection** — This software may collect information about you and your usage of the software and send it to Microsoft. Microsoft may use this information to provide services and improve its products. You can disable telemetry as described in this repository. Some features may enable data collection from users of your applications; if you use these features, you must comply with applicable laws, including providing appropriate notices and sharing Microsoft’s privacy statement with your users. The privacy statement is available at https://go.microsoft.com/fwlink/?LinkID=824704. More information about data collection and usage can be found in the help documentation and privacy statement. Use of this software constitutes consent to these practices.