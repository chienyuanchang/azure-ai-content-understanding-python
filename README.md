# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various media content, such as **documents, images, audio, and video**, transforming it into structured, organized, and searchable data.

- The samples in this repository default to the latest preview API version: **2025-05-01-preview**.
- More samples demonstrating new functionalities in Preview.2 **2025-05-01-preview** will be added soon.
- As of May 2025, the 2025-05-01-preview version is available only in the regions listed in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).
- To access sample code for version 2024-12-01-preview, please check out the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started

You can run the samples in GitHub Codespaces or in your local environment. For a smoother, hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

Run this repository virtually using GitHub Codespaces, which opens a web-based VS Code in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

Once you click the link above, follow these steps to set up the Codespace:

1. Create a new Codespace by selecting the main branch, your preferred region, and the 2-core machine type, as shown in the screenshot below.  
![Create CodeSpace](/docs/create-codespace/1-Create%20Codespace.png)

2. When the Codespace is ready, open the terminal and follow the instructions in the "Configure Azure AI service resource" section to set up a valid Content Understanding resource.

### Local Environment

1. Ensure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)  
    * [Python 3.11+](https://www.python.org/downloads/)  
    * [Git LFS](https://git-lfs.com/)

2. Create a new directory named `azure-ai-content-understanding-python` and clone this template using the `azd` CLI:  
    ```shell
    azd init -t azure-ai-content-understanding-python
    ```  
    Alternatively, you can clone the repository using git:  
    ```shell
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```  
    - **Important:** If you clone with git, make sure to install Git LFS and run `git lfs pull` to download sample files located in the `data` directory:  
      ```shell
      git lfs install
      git lfs pull
      ```

3. Set up the development container environment:

  - Install the necessary tools:

    - **Visual Studio Code**  
        Download and install [Visual Studio Code](https://code.visualstudio.com/).

    - **Dev Containers Extension**  
      Install the "Dev Containers" extension from the VS Code marketplace.  
      (Previously called "Remote - Containers", now renamed and integrated as Dev Containers.)

    - **Docker**  
      Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (available for Windows, macOS, and Linux).  
      Docker manages and runs the container environment.  
      - Start Docker and ensure it is running.

  - Open the project and start the Dev Container:

    - Open the project folder with VS Code.  
    - Press `F1` or `Ctrl+Shift+P`, type, and select:  
      ```
      Dev Containers: Reopen in Container
      ```  
      Or click the green icon at the bottom-left corner of VS Code and select "Reopen in Container".  
    - VS Code will detect the `.devcontainer` folder, build the development container, and install required dependencies automatically.  
    - ![How to set dev container environment](./docs/dev-container-setup.gif "Dev container setup")

## Configure Azure AI Service Resource

### (Option 1) Use `azd` commands to automatically create temporary resources and run the sample

1. Ensure you have appropriate permissions to assign roles under your Azure subscription.
2. Log in to Azure:  
    ```shell
    azd auth login
    ```  
    If the above does not work, use device code authentication:  
    ```shell
    azd auth login --use-device-code
    ```
3. Set up the environment by following prompts to select location:  
    ```shell
    azd up
    ```

### (Option 2) Manually create resources and configure environment variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).
2. In your resource, go to **Access Control (IAM)** and assign yourself the role **Cognitive Services User**.  
    - This step is necessary even if you are the resource owner.
3. Copy `notebooks/.env.sample` to `notebooks/.env`.
4. Fill in **AZURE_AI_ENDPOINT** with the endpoint from your Azure AI Services instance found in the Azure portal.
5. Log in to Azure:  
    ```shell
    azd auth login
    ```

## Open a Jupyter Notebook and Follow the Step-by-Step Guide

Navigate to the `notebooks` directory and open the sample notebook you want to explore. Since the Dev Container (in Codespaces or your local environment) is pre-configured with the necessary environment, you can directly execute each step.

1. Select a notebook of interest from the `notebooks/` directory. We recommend starting with `content_extraction.ipynb` to understand the basic concepts.  
![Select *.ipynb](/docs/create-codespace/2-Select%20file.ipynb.png)

2. Select the Kernel.  
![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)

3. Select the Python environment.  
![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)

4. Run the notebook cells.  
![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) designed to process and ingest content of any type—documents, images, audio, and video—into a user-defined output format. Content Understanding offers a streamlined approach to reasoning over large volumes of unstructured data, accelerating time-to-value by generating outputs that can be integrated into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how Content Understanding APIs extract semantic information from files. For example, OCR with tables in documents, audio transcription, and face analysis in video. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract fields from your files. Examples include extracting invoice amounts from documents, counting people in images, identifying names mentioned in audio, or summarizing videos. You can customize fields by creating your own analyzer templates. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates evaluating conversational audio data previously transcribed with Content Understanding or Azure AI Speech. This helps optimize processing quality efficiently and allows cost-effective re-analysis. This sample builds upon [field_extraction.ipynb](notebooks/field_extraction.ipynb). |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to boost field extraction performance by training the analyzer using a few labeled samples. *Note: This feature is currently available for document scenarios only.* |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates creating a minimal analyzer, listing all analyzers in your resource, and deleting undesired analyzers. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Demonstrates how to enroll people’s faces from images and build a Person Directory. |

## Additional Samples Using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** — This project may contain trademarks or logos for products, services, or projects. Authorized use of Microsoft trademarks or logos is subject to [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos is subject to those third parties’ policies.

* **Data Collection** — The software may collect information about you and your use of the software and send it to Microsoft to provide services and improve our products. You may disable telemetry as described in this repository. Some features may enable you and Microsoft to collect data from users of your applications. Use of these features requires compliance with applicable laws, including providing appropriate user notices along with Microsoft’s privacy statement, available at https://go.microsoft.com/fwlink/?LinkID=824704. More information on data collection and use can be found in the documentation and privacy statement. Your use of this software constitutes consent to these practices.

