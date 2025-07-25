# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various media content, such as **documents, images, audio, and video**, transforming it into structured, organized, and searchable data.

- The samples in this repository use the latest preview API version by default: **2025-05-01-preview**.
- More samples demonstrating new functionalities in Preview.2 **2025-05-01-preview** will be added soon.
- As of May 2025, the 2025-05-01-preview version is available only in the regions listed in the [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support) documentation.
- To access sample code for version 2024-12-01-preview, please check out the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started

You can run the samples in GitHub Codespaces or in your local environment. For a smoother, hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

Run this repository virtually by using GitHub Codespaces, which opens a web-based VS Code instance in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

After clicking the link above, follow these steps to set up your Codespace:

1. Create a new Codespace by selecting the **main** branch, your preferred region, and the 2-core machine type as shown below.  
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
    Alternatively, you can clone directly using git:
    ```
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```
    - **Important:** If you use `git clone`, ensure Git LFS is installed and run the following to download sample files in the `data` directory:
      ```shell
      git lfs install
      git lfs pull
      ```

3. Set up the Dev Container Environment:
  - Install tools that support dev containers:

    - **Visual Studio Code**  
      Download and install [Visual Studio Code](https://code.visualstudio.com/).

    - **Dev Containers Extension**  
      In the VS Code extension marketplace, install the "Dev Containers" extension.  
      (Previously called "Remote - Containers," it has been renamed and integrated into Dev Containers.)

    - **Docker**  
      Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (available for Windows, macOS, and Linux).  
      Docker manages and runs the container environment.  
      - Start Docker and ensure it is running in the background.

  - Open the project and start the Dev Container:
    - Open the project folder in VS Code.
    - Press `F1` or `Ctrl+Shift+P`, type, and select:  
      ```
      Dev Containers: Reopen in Container
      ```
      Or click the green icon in the lower-left corner of VS Code and select **Reopen in Container**.
    - VS Code will detect the `.devcontainer` folder, build the development container, and install necessary dependencies.  
    - ![Dev container setup](./docs/dev-container-setup.gif "Dev container setup")

## Configure Azure AI Service Resource

### (Option 1) Use `azd` commands to automatically create temporary resources for running the sample

1. Ensure you have permission to assign roles under your Azure subscription.
2. Log in to Azure:
    ```shell
    azd auth login
    ```
    If this command doesn’t work, try:
    ```
    azd auth login --use-device-code
    ```
    and follow the on-screen instructions.
3. Set up the environment by following prompts to select your location:
    ```shell
    azd up
    ```

### (Option 2) Manually create resources and set environment variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).
2. In the Azure portal, navigate to **Access Control (IAM)** on your resource and assign yourself the **Cognitive Services User** role.  
   - Note: This is required even if you are the owner of the resource.
3. Copy `notebooks/.env.sample` to `notebooks/.env`.
4. Fill in **AZURE_AI_ENDPOINT** with your Azure AI Services endpoint found in the portal.
5. Log in to Azure:
   ```shell
   azd auth login
   ```

## Open a Jupyter Notebook and Follow the Step-by-Step Guidance

Navigate to the `notebooks` directory and open a sample notebook of your choice. The Dev Container (in Codespaces or your local environment) is pre-configured with the required environment, enabling you to run each step directly.

1. Select a notebook from the `notebooks/` directory. We recommend starting with `content_extraction.ipynb` to understand the basic concepts.  
   ![Select *.ipynb](/docs/create-codespace/2-Select%20file.ipynb.png)

2. Select the kernel.  
   ![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)

3. Select the Python environment.  
   ![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)

4. Run the notebook cells.  
   ![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview), designed to ingest and process content of any kind (documents, images, audio, and video) into user-defined output formats. Content Understanding simplifies reasoning over large amounts of unstructured data, accelerating time-to-value by generating outputs that can be integrated into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how Content Understanding API extracts semantic information from files, e.g., OCR with tables in documents, audio transcription, and face analysis in video. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract fields from files—for example, invoice amounts in documents, number of people in images, names mentioned in audio, or video summaries. You can customize fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates efficient evaluation of conversational audio data previously transcribed with Content Understanding or Azure AI Speech. It enables re-analysis in a cost-effective manner. This sample builds on [field_extraction.ipynb](notebooks/field_extraction.ipynb). |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to boost field extraction performance by training the analyzer using a few labeled samples. Note: This feature currently supports document scenarios only. |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates creating a minimal analyzer, listing all analyzers in your resource, and deleting unneeded analyzers. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Shows how to enroll people’s faces from images and build a Person Directory. |

## More Samples Using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** — This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos must comply with [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Use of third-party trademarks or logos is governed by those third parties’ policies.

* **Data Collection** — This software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve products. You may disable telemetry as described in this repository. Some features may enable you or Microsoft to collect data from your application’s users. Use of such features requires compliance with applicable laws, including providing appropriate notices to your users along with a copy of Microsoft’s privacy statement located at https://go.microsoft.com/fwlink/?LinkID=824704. Your use of the software constitutes consent to these data collection practices.