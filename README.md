# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various media content—such as **documents, images, audio, and video**—transforming it into structured, organized, and searchable data.

- The samples in this repository default to the latest preview API version: **2025-05-01-preview**.  
- Additional samples demonstrating new functionalities in Preview.2 (**2025-05-01-preview**) will be provided soon.  
- As of May 2025, the **2025-05-01-preview** API version is available only in the regions listed in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).  
- To access sample code for version **2024-12-01-preview**, please check out the corresponding Git tag `2024-12-01-preview`, or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started

You can run the samples in GitHub Codespaces or your local environment. For a smoother, hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

You can run this repository virtually via GitHub Codespaces, which opens a web-based VS Code in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

After clicking the link above, follow the steps below to set up the Codespace:

1. Create a new Codespace by selecting the `main` branch, your preferred region, and the 2-core machine type, as shown in the screenshot below.  
   ![Create Codespace](/docs/create-codespace/1-Create%20Codespace.png)
2. Once the Codespace is ready, open the terminal and follow the instructions in the **Configure Azure AI service resource** section to set up a valid Content Understanding resource.

### Local Environment

1. Ensure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)  
    * [Python 3.11+](https://www.python.org/downloads/)  
    * [Git LFS](https://git-lfs.com/)  

2. Create a new directory called `azure-ai-content-understanding-python` and clone this template into it using the `azd` CLI:

    ```bash
    azd init -t azure-ai-content-understanding-python
    ```

    Alternatively, you can use git to clone the repository:

    ```bash
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```

    - **Important:** If you use `git clone`, ensure you have Git LFS installed and run the following commands to download sample files in the `data` directory:

      ```bash
      git lfs install
      git lfs pull
      ```

3. Set Up Dev Container Environment:

  - Install tools that support development containers:

    - **Visual Studio Code**  
      Download and install [Visual Studio Code](https://code.visualstudio.com/).

    - **Dev Containers Extension**  
      In the VS Code Extensions marketplace, install the extension named **Dev Containers**.  
      (This extension was previously called "Remote - Containers" but has been renamed and integrated into Dev Containers.)

    - **Docker**  
      Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (available for Windows, macOS, and Linux).  
      Docker manages and runs the container environment.  
      - Start Docker and ensure it is running in the background.

  - Open the project and start the Dev Container:

    - Open the project folder with VS Code.
    - Press `F1` or `Ctrl+Shift+P`, type, and select:

      ```
      Dev Containers: Reopen in Container
      ```

      Or click the green icon in the lower-left corner of VS Code and select **Reopen in Container**.
    - VS Code will automatically detect the `.devcontainer` folder, build the development container, and install the necessary dependencies.
    - ![Dev container setup](./docs/dev-container-setup.gif "Dev container setup")

## Configure Azure AI Service Resource

### (Option 1) Use `azd` commands to automatically create temporary resources to run the sample

1. Ensure you have permission to assign roles under your subscription.

2. Login to Azure:

    ```bash
    azd auth login
    ```

    If this command doesn’t work, try the following and follow the on-screen instructions:

    ```bash
    azd auth login --use-device-code
    ```

3. Set up the environment, following prompts to choose a location:

    ```bash
    azd up
    ```

### (Option 2) Manually Create Resources and Set Environment Variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).

2. In the Azure portal, go to **Access Control (IAM)** for your resource and assign yourself the role **Cognitive Services User**.  
   - This assignment is necessary even if you are the owner of the resource.

3. Copy `notebooks/.env.sample` to `notebooks/.env`.

4. Fill in **AZURE_AI_ENDPOINT** with the endpoint URL from your Azure AI Services instance in the portal.

5. Login to Azure:

    ```bash
    azd auth login
    ```

## Open a Jupyter Notebook and Follow the Step-by-Step Guidance

Navigate to the `notebooks` directory and select the sample notebook you want to explore. Since the Dev Container (in Codespaces or your local environment) is pre-configured with the necessary environment, you can directly execute each step in the notebook.

1. Select a notebook in the `notebooks/` directory. We recommend starting with **content_extraction.ipynb** to understand the basic concepts.  
   ![Select .ipynb file](/docs/create-codespace/2-Select%20file.ipynb.png)

2. Select the Kernel:  
   ![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)

3. Select the Python Environment:  
   ![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)

4. Run the notebook cells:  
   ![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) designed to process and ingest content of any type (documents, images, audio, and video) into a user-defined output format. Content Understanding offers a streamlined process to analyze large amounts of unstructured data, accelerating time-to-value by generating outputs that can be integrated into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how Content Understanding APIs extract semantic information from various file types, such as OCR with tables in documents, audio transcription, and face analysis in videos. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract specific fields from your files. Examples include invoice amounts from documents, counting people in images, extracting names mentioned in audio, or summarizing videos. You can customize fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates efficient evaluation of conversational audio data previously transcribed using Content Understanding or Azure AI Speech, enabling cost-effective re-analysis and improved processing quality. This sample builds on [field_extraction.ipynb](notebooks/field_extraction.ipynb). |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to enhance field extraction performance by training the analyzer with a few labeled samples. *Note:* This training feature currently supports only document scenarios. |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates how to create minimal analyzers, list all analyzers in your resource, and delete unnecessary analyzers. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Demonstrates how to enroll faces from images and build a Person Directory. |

## More Samples Using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)  
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** — This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos must comply with [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Use of third-party trademarks or logos is subject to those third parties’ policies.

* **Data Collection** — The software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve products. You may disable telemetry as described in this repository. Some features may enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable laws, including providing appropriate notices to your users alongside a copy of Microsoft’s privacy statement. Microsoft’s privacy statement is located at https://go.microsoft.com/fwlink/?LinkID=824704. By using this software, you consent to these data collection and use practices.