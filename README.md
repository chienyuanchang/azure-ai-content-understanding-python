# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various media content—such as **documents, images, audio, and video**—and transforms it into structured, organized, and searchable data.

- The samples in this repository default to the latest preview API version: **2025-05-01-preview**.
- This repository will soon include more samples showcasing new functionalities introduced in Preview.2 **2025-05-01-preview**.
- As of May 2025, the 2025-05-01-preview API is available only in the regions documented in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).
- To access sample code for version 2024-12-01-preview, please checkout the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started
You can run the samples either in GitHub Codespaces or in your local environment. For a smoother, hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces
Run this repository virtually using GitHub Codespaces, which opens a web-based VS Code in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

After clicking the link above, follow these steps to set up the Codespace:

1. Create a new Codespace by selecting the main branch, your preferred region, and the 2-core machine type, as shown in the screenshot below.  
![Create Codespace](/docs/create-codespace/1-Create%20Codespace.png)  
2. Once the Codespace is ready, open the terminal and follow the instructions in the "Configure Azure AI service resource" section to set up a valid Content Understanding resource.

### Local Environment
1. Ensure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)
    * [Python 3.11+](https://www.python.org/downloads/)
    * [Git LFS](https://git-lfs.com/)

2. Create a new directory called `azure-ai-content-understanding-python` and clone this repository using the `azd` CLI:
    ```
    azd init -t azure-ai-content-understanding-python
    ```
    Alternatively, you can clone the repository using Git:
    ```
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```
    - **Important:** If you clone the repository with Git, install Git LFS and pull the large files in the `data` folder:

      ```shell
      git lfs install
      git lfs pull
      ```
3. Set up the Dev Container environment:
  - Install the following tools:
    - **Visual Studio Code**  
      Download and install [Visual Studio Code](https://code.visualstudio.com/).

    - **Dev Containers Extension**  
      In the VS Code extension marketplace, install the "Dev Containers" extension.  
      (Previously called "Remote - Containers", it has been renamed and integrated into Dev Containers.)

    - **Docker**  
      Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Windows, macOS, or Linux.  
      Docker manages and runs the container environment.  
      - Start Docker and ensure it is running in the background.

  - Open the project and start the Dev Container:
    - Open the project folder in VS Code.
    - Press `F1` or `Ctrl+Shift+P`, type and select:
      ```
      Dev Containers: Reopen in Container
      ```
      Or click the green icon in the lower-left corner of VS Code and select "Reopen in Container".
    - VS Code will detect the `.devcontainer` folder, build the development container, and install required dependencies automatically.
    - ![Dev Container Setup](./docs/dev-container-setup.gif "Dev container setup")

## Configure Azure AI Service Resource

### Option 1: Use `azd` Commands to Automatically Create Temporary Resources to Run Samples
1. Ensure you have permission to grant roles within your Azure subscription.
2. Log in to Azure:
    ```shell
    azd auth login
    ```
    If the command above fails, try:
    ```
    azd auth login --use-device-code
    ```
    and follow the on-screen instructions.
3. Set up the environment, following the prompts to select the desired location:
    ```shell
    azd up
    ```

### Option 2: Manually Create Resources and Set Environment Variables
1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).
2. In the resource, go to `Access Control (IAM)` and assign yourself the role **Cognitive Services User**.  
   - This step is required even if you are the owner of the resource.
3. Copy `notebooks/.env.sample` to `notebooks/.env`.
4. Fill in **AZURE_AI_ENDPOINT** with the endpoint URL from your Azure AI Services resource in the Azure portal.
5. Log in to Azure:
   ```shell
   azd auth login
   ```

## Open a Jupyter Notebook and Follow Step-by-Step Guidance

Navigate to the `notebooks` directory and select the sample notebook that interests you. Since the Dev Container (whether in Codespaces or your local environment) is pre-configured with the necessary runtime and dependencies, you can run each step in the notebook directly.

1. Choose a notebook in the `notebooks/` directory. We recommend starting with `content_extraction.ipynb` to understand the basic concepts.  
![Select Notebook](/docs/create-codespace/2-Select%20file.ipynb.png)  
2. Select the Kernel:  
![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)  
3. Select the Python Environment:  
![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)  
4. Run the notebook:  
![Run Notebook](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) designed to process and ingest all content types (documents, images, audio, and video) into user-defined output formats. It streamlines reasoning over large volumes of unstructured data, accelerating time-to-value by generating outputs that can be seamlessly integrated into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how the Content Understanding API extracts semantic information from files—for example, OCR with tables in documents, audio transcription, and face analysis in videos. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract fields from your files—for example, extracting invoice amounts from documents, counting people in images, identifying names mentioned in audio, or generating video summaries. You can customize fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates evaluating conversational audio data previously transcribed using Content Understanding or Azure AI Speech, optimizing processing quality, and enabling cost-efficient re-analysis. This sample builds on the [field_extraction.ipynb](notebooks/field_extraction.ipynb) sample. |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to boost field extraction performance by training the model with a few labeled samples. Note: This feature is currently available only for document scenarios. |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates how to create a minimal analyzer, list all analyzers in your resource, and delete unnecessary analyzers. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Demonstrates how to enroll people’s faces from images and build a Person Directory. |

## More Samples Using Azure Content Understanding
- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** – This project may include trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks and logos must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Use of third-party trademarks or logos is subject to those third parties' policies.

* **Data Collection** – This software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve our products. You may disable telemetry as described in this repository. Some features may enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable laws, including providing appropriate notices to your application users together with a copy of Microsoft's privacy statement. Our privacy statement is at https://go.microsoft.com/fwlink/?LinkID=824704. Your use of this software indicates your consent to these practices.