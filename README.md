# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various media content, such as **documents, images, audio, and video**, transforming it into structured, organized, and searchable data.

- The samples in this repository default to the latest preview API version: **2025-05-01-preview**.
- More samples demonstrating new functionalities in Preview.2 **2025-05-01-preview** will be added soon.
- As of May 2025, the 2025-05-01-preview API version is only available in the regions documented in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).
- To access sample code for version 2024-12-01-preview, please check out the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started

You can run the samples either in GitHub Codespaces or in your local environment. For a smoother, hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

You can run this repository virtually using GitHub Codespaces, which opens a web-based VS Code interface in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

Once you click the link above, follow these steps to set up the Codespace:

1. Create a new Codespace by selecting the **main** branch, your preferred region for the Codespace, and the **2-core machine type**, as shown in the screenshot below.  
   ![Create Codespace](/docs/create-codespace/1-Create%20Codespace.png)
2. Once the Codespace is ready, open the terminal and follow the instructions in the **Configure Azure AI service resource** section below to set up a valid Content Understanding resource.

### Local Environment

1. Ensure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)  
    * [Python 3.11+](https://www.python.org/downloads/)  
    * [Git LFS](https://git-lfs.com/)

2. Create a new directory named `azure-ai-content-understanding-python` and clone this repository into it:

   Using `azd` CLI:

   ```shell
   azd init -t azure-ai-content-understanding-python
   ```

   Alternatively, you can use Git:

   ```shell
   git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
   cd azure-ai-content-understanding-python
   ```

   - **Important:** If you clone with Git, make sure to install Git LFS and run the following commands to download sample files in the `data` directory:

     ```shell
     git lfs install
     git lfs pull
     ```

3. Set up the Dev Container environment:

   - Install the following tools to support Dev Containers:

     - **Visual Studio Code**  
       Download and install [Visual Studio Code](https://code.visualstudio.com/).

     - **Dev Containers Extension**  
       Install the extension named **Dev Containers** from the VS Code extension marketplace.  
       *(Previously called "Remote - Containers", it has been renamed and integrated as Dev Containers.)*

     - **Docker**  
       Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (available for Windows, macOS, and Linux).  
       Docker is used to manage and run the container environment.  
       - Start Docker and ensure it is running in the background.

   - Open the project and start the Dev Container:

     - Open the project folder with VS Code.
     - Press `F1` or `Ctrl+Shift+P`, then type and select:

       ```
       Dev Containers: Reopen in Container
       ```
       Alternatively, click the green corner icon in VS Code (bottom-left) and select **Reopen in Container**.
     - VS Code will detect the `.devcontainer` folder, build the development container, and install all necessary dependencies.
     - ![Dev container setup](./docs/dev-container-setup.gif "Dev container setup")

## Configure Azure AI Service Resource

### Option 1: Use `azd` commands to automatically create temporary resources to run the samples

1. Ensure you have permission to grant roles within your Azure subscription.
2. Log in to Azure:

   ```shell
   azd auth login
   ```

   If the above command doesn't work, try:

   ```shell
   azd auth login --use-device-code
   ```

3. Set up the environment; follow the prompts to choose the Azure location:

   ```shell
   azd up
   ```

### Option 2: Manually create resources and set environment variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).
2. In the Azure portal, go to **Access Control (IAM)** for your resource and assign yourself the role **Cognitive Services User**.  
   *(This is necessary even if you are the resource owner.)*
3. Copy `notebooks/.env.sample` to `notebooks/.env`.
4. Fill in **AZURE_AI_ENDPOINT** in `notebooks/.env` with the endpoint URL from your Azure AI Services resource in the Azure portal.
5. Log in to Azure:

   ```shell
   azd auth login
   ```

## Open a Jupyter Notebook and Follow Step-by-Step Guidance

Navigate to the `notebooks` directory and choose the sample notebook you want to run. The Dev Container environment (in Codespaces or your local setup) is pre-configured with all necessary dependencies, so you can directly run the notebooks.

To get started:

1. Select a notebook of interest in the `notebooks/` directory. We recommend starting with **content_extraction.ipynb** to understand the basic concepts.  
   ![Select notebook file](/docs/create-codespace/2-Select%20file.ipynb.png)
2. Select the Kernel.  
   ![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)
3. Select the Python Environment.  
   ![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)
4. Run the notebook cells step-by-step.  
   ![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) designed to process and ingest content of any type—documents, images, audio, and video—into a user-defined output format. Content Understanding offers a streamlined process to analyze large volumes of unstructured data, accelerating time-to-value by generating outputs that can be integrated into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how the Content Understanding API extracts semantic information from files, such as OCR with tables in documents, audio transcription, and face analysis in videos. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract specific fields from your files, e.g., invoice amounts in documents, counting people in images, names mentioned in audio, or summaries of videos. You can customize the fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates how to efficiently evaluate conversational audio data previously transcribed with Content Understanding or Azure AI Speech, optimizing processing quality and enabling cost-efficient re-analysis. This sample builds on [field_extraction.ipynb](notebooks/field_extraction.ipynb). |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to improve field extraction accuracy by training the API with a few labeled samples. Note: This feature is currently available for document scenarios only. |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates how to create a minimal analyzer, list all analyzers in your resource, and delete any analyzer you no longer need. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Demonstrates how to enroll people’s faces from images and build a Person Directory. |

## More Samples using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

- **Trademarks**  
  This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must comply with [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos is subject to those third parties’ policies.

- **Data Collection**  
  The software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve its products. You may disable telemetry as described in this repository. Some features may enable data collection from users of your applications; if you use these features, you must comply with applicable laws, including providing notices to users along with Microsoft’s privacy statement, available at https://go.microsoft.com/fwlink/?LinkID=824704. By using this software, you consent to these practices.

