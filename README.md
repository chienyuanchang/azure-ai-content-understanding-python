# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various types of media content—including **documents, images, audio, and video**—and transforms it into structured, organized, and searchable data.

- The samples in this repository use the latest preview API version by default: **2025-05-01-preview**.
- This repository will soon provide more samples for new functionalities introduced in Preview.2 **2025-05-01-preview**.
- As of May 2025, the 2025-05-01-preview API is only available in the regions listed in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).
- To access sample code for version 2024-12-01-preview, please check out the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started

You can run the samples in GitHub Codespaces or your local environment. For a smoother and hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

Run this repository virtually using GitHub Codespaces, which opens a web-based VS Code instance in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

After clicking the link above, follow these steps to set up the Codespace:

1. Create a new Codespace by selecting the **main** branch, your preferred region for the Codespace, and the 2-core machine type, as shown in the screenshot below.  
![Create Codespace](/docs/create-codespace/1-Create%20Codespace.png)

2. Once the Codespace is ready, open the terminal and follow the instructions in the **Configure Azure AI service resource** section to set up a valid Content Understanding resource.

### Local Environment

1. Ensure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)
    * [Python 3.11 or higher](https://www.python.org/downloads/)
    * [Git LFS](https://git-lfs.com/)

2. Create a new directory named `azure-ai-content-understanding-python` and clone this repository into it using the `azd` CLI:

    ```
    azd init -t azure-ai-content-understanding-python
    ```

    Alternatively, you can clone the repository using Git:

    ```
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```

    - **Important:** If you use `git clone`, ensure Git LFS is installed and run `git lfs pull` to download the sample files located in the `data` directory:

      ```shell
      git lfs install
      git lfs pull
      ```

3. Set up the Development Container environment:

   - Install tools that support Dev Containers:

     - **Visual Studio Code**  
       Download and install [Visual Studio Code](https://code.visualstudio.com/).

     - **Dev Containers Extension**  
       In the VS Code Extensions Marketplace, install the extension named **Dev Containers**.  
       (Previously called "Remote - Containers," it has been renamed and integrated into Dev Containers.)

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

       Alternatively, click the green icon in the lower-left corner of VS Code and select **Reopen in Container**.

     - VS Code will automatically detect the `.devcontainer` folder, build the development container, and install the necessary dependencies.  
     - ![Dev container setup](./docs/dev-container-setup.gif)

## Configure Azure AI Service Resource

### Option 1: Use `azd` Commands to Automatically Create Temporary Resources to Run the Sample

1. Ensure you have permissions to grant roles under your subscription.

2. Log in to Azure:

    ```shell
    azd auth login
    ```

    If that command fails, try:

    ```
    azd auth login --use-device-code
    ```

    Follow the on-screen instructions.

3. Set up the environment and follow prompts to choose the location:

    ```shell
    azd up
    ```

### Option 2: Manually Create Resources and Set Environment Variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).

2. In the Azure portal, navigate to **Access Control (IAM)** on your resource and assign yourself the **Cognitive Services User** role.  
   - This step is necessary even if you are the owner of the resource.

3. Copy `notebooks/.env.sample` to `notebooks/.env`.

4. Fill in **AZURE_AI_ENDPOINT** in the `.env` file with the endpoint URL from your Azure AI Services instance.

5. Log in to Azure:

   ```shell
   azd auth login
   ```

## Open a Jupyter Notebook and Follow the Step-by-Step Guidance

Navigate to the `notebooks` directory and open the sample notebook you want to explore. Since the Dev Container (in Codespaces or your local environment) is pre-configured with the necessary environment, you can directly execute each cell in the notebook.

1. Select one of the notebooks in the `notebooks/` directory. We recommend starting with **content_extraction.ipynb** to understand the basic concepts.  
![Select *.ipynb](/docs/create-codespace/2-Select%20file.ipynb.png)

2. Select the Kernel:  
![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)

3. Choose the Python Environment:  
![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)

4. Run the notebook:  
![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) designed to process and ingest content of any type—including documents, images, audio, and video—into user-defined output formats. Content Understanding offers a streamlined way to analyze vast amounts of unstructured data, accelerating time-to-value by generating outputs ready for integration with automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how the Content Understanding API extracts semantic information from your files, including OCR with tables in documents, audio transcription, and face analysis in videos. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract fields from your files, such as invoice amounts from documents, people counts from images, names mentioned in audio, or video summaries. You can customize fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates how to efficiently evaluate conversational audio data previously transcribed with Content Understanding or Azure AI Speech. This approach optimizes processing quality and cost. This sample builds on the [field_extraction.ipynb](notebooks/field_extraction.ipynb) sample. |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to improve field extraction performance by training the analyzer using a few labeled samples. Note: This feature currently supports document scenarios only. |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates how to create a minimal analyzer, list all analyzers in your resource, and delete analyzers you no longer need. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Demonstrates how to enroll people’s faces from images and build a Person Directory. |

## More Samples Using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks**  
  This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must comply with [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Use of third-party trademarks or logos is subject to those third parties' policies.

* **Data Collection**  
  The software may collect information about you and your usage and send it to Microsoft. Microsoft uses this information to provide and improve its services and products. You may disable telemetry as described in this repository. Some features may allow you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable laws, including providing appropriate notices to your users along with a copy of Microsoft's privacy statement, located at https://go.microsoft.com/fwlink/?LinkID=824704. Use of this software indicates your consent to these practices.