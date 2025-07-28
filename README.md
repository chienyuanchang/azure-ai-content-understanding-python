# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various media content, including **documents, images, audio, and video**, transforming it into structured, organized, and searchable data.

- The samples in this repository default to the latest preview API version: **2025-05-01-preview**.
- We will provide additional samples for new functionalities in Preview.2 **2025-05-01-preview** soon.
- As of May 2025, the 2025-05-01-preview API version is available only in the regions documented in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).
- To access sample code for version 2024-12-01-preview, please check out the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started

You can run the samples in GitHub Codespaces or your local environment. For a smoother, hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

You can run this repository virtually using GitHub Codespaces, which opens a web-based VS Code environment in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

After clicking the link above, follow these steps to set up your Codespace:

1. Create a new Codespace by selecting the `main` branch, your preferred region for the Codespace, and the 2-core machine type, as shown in the screenshot below. \
![Create Codespace](/docs/create-codespace/1-Create%20Codespace.png)

2. Once the Codespace is ready, open the terminal and follow the instructions in the **Configure Azure AI service resource** section to set up a valid Content Understanding resource.

### Local Environment

1. Ensure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)
    * [Python 3.11+](https://www.python.org/downloads/)
    * [Git LFS](https://git-lfs.com/)

2. Create a new directory named `azure-ai-content-understanding-python` and clone this repository using the `azd` CLI:

    ```
    azd init -t azure-ai-content-understanding-python
    ```

    Alternatively, you can use Git to clone the repository:

    ```
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```

    - **Important:** If you use `git clone`, make sure to install Git LFS and run the following commands to download sample files in the `data` directory:

      ```shell
      git lfs install
      git lfs pull
      ```

3. Set up the Dev Container environment:

    - Install the required tools to support dev containers:

        - **Visual Studio Code**  
          Download and install [Visual Studio Code](https://code.visualstudio.com/).

        - **Dev Containers Extension**  
          In the VS Code extension marketplace, install the extension named **Dev Containers**.  
          (This extension was previously called "Remote - Containers" but has since been renamed and integrated into Dev Containers.)

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

        - Alternatively, click the green icon in the lower-left corner of VS Code and select **Reopen in Container**.
        - VS Code will automatically detect the `.devcontainer` folder, build the development container, and install the necessary dependencies.  
        - ![Dev container setup](./docs/dev-container-setup.gif "Dev Container Setup")

## Configure Azure AI Service Resource

### (Option 1) Use `azd` commands to automatically create temporary resources and run the sample

1. Ensure you have permission to assign roles under your subscription.

2. Log in to Azure:

    ```shell
    azd auth login
    ```

    If the above command doesn’t work, try:

    ```shell
    azd auth login --use-device-code
    ```

    Then follow the on-screen instructions.

3. Set up the environment by following the prompts to select a location:

    ```shell
    azd up
    ```

### (Option 2) Manually create resources and set environment variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).

2. In the Azure portal, go to `Access Control (IAM)` for your resource and assign yourself the **Cognitive Services User** role.  
   - This is necessary even if you are the resource owner.

3. Copy `notebooks/.env.sample` to `notebooks/.env`.

4. Fill in **AZURE_AI_ENDPOINT** with the endpoint URL from your Azure AI Services resource.

5. Log in to Azure:

    ```shell
    azd auth login
    ```

## Open a Jupyter Notebook and Follow the Step-by-Step Guidance

Navigate to the `notebooks` directory and open the sample notebook of your choice. Since the Dev Container (in Codespaces or your local environment) is pre-configured with the necessary environment, you can directly run the cells in the notebook.

1. Select one of the notebooks in the `notebooks/` directory. We recommend starting with **content_extraction.ipynb** to understand the basic concepts.  
   ![Select *.ipynb](/docs/create-codespace/2-Select%20file.ipynb.png)

2. Select the Kernel:  
   ![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)

3. Select the Python Environment:  
   ![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)

4. Run the notebook:  
   ![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) designed to process and ingest content of any type—documents, images, audio, and video—into user-defined output formats. Content Understanding offers a streamlined process to analyze large volumes of unstructured data, accelerating time-to-value by generating outputs that can be integrated into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how the Content Understanding API can extract semantic information from your files. Examples include OCR with tables in documents, audio transcription, and face analysis in video. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract specific fields from your files, such as the invoice amount in a document, the number of people in an image, names mentioned in audio, or a summary of a video. You can customize fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates how to efficiently evaluate conversational audio data previously transcribed with Content Understanding or Azure AI Speech. This enables optimized processing quality and cost-effective re-analysis. This sample builds on [field_extraction.ipynb](notebooks/field_extraction.ipynb). |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to improve field extraction performance by training the analyzer with a few labeled samples. Note: This feature is currently available for document scenarios only. |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates how to create a minimal analyzer, list all analyzers in your resource, and delete unwanted analyzers. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Shows how to enroll people's faces from images and build a Person Directory. |

## More Samples Using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)

- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** – This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos is subject to those third parties’ policies.

* **Data Collection** – The software may collect information about you and your usage of the software and send it to Microsoft. Microsoft may use this information to provide services and improve products. You may disable telemetry as described in this repository. Some features may enable both you and Microsoft to collect data from end users of your applications. If you use these features, you must comply with applicable laws, including providing appropriate notices to users of your applications along with a copy of Microsoft’s privacy statement, available at https://go.microsoft.com/fwlink/?LinkID=824704. Your use of the software constitutes your consent to these practices.