# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various media content, such as **documents, images, audio, and video**, transforming it into structured, organized, and searchable data.

- The samples in this repository default to the latest preview API version: **2025-05-01-preview**.
- This repo will soon provide more samples for new functionalities in Preview.2 **2025-05-01-preview**.
- As of May 2025, the **2025-05-01-preview** API version is only available in the regions documented in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).
- To access sample code for version **2024-12-01-preview**, please check out the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting started

You can run the samples in GitHub Codespaces or your local environment. For a smoother, hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

Run this repository virtually using GitHub Codespaces, which opens a web-based VS Code in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

After clicking the link above, follow these steps to set up the Codespace:

1. Create a new Codespace by selecting the **main** branch, your preferred Codespace region, and the **2-core** machine type, as shown below.  
   ![Create Codespace](/docs/create-codespace/1-Create%20Codespace.png)

2. Once the Codespace is ready, open the terminal and follow the instructions in the **Configure Azure AI service resource** section below to set up a valid Content Understanding resource.

### Local environment

1. Ensure the following tools are installed:

    - [Azure Developer CLI (azd)](https://aka.ms/install-azd)  
    - [Python 3.11+](https://www.python.org/downloads/)  
    - [Git LFS](https://git-lfs.com/)

2. Create a new directory named `azure-ai-content-understanding-python` and clone this repository using the `azd` CLI:

    ```bash
    azd init -t azure-ai-content-understanding-python
    ```

    Alternatively, you can clone directly using git:

    ```bash
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```

    - **Important:** If you use `git clone`, ensure Git LFS is installed and run `git lfs pull` to download the sample files in the `data` directory:

      ```bash
      git lfs install
      git lfs pull
      ```

3. Set up the Dev Container environment:

    - **Visual Studio Code**  
      Download and install [Visual Studio Code](https://code.visualstudio.com/).

    - **Dev Containers Extension**  
      Install the "Dev Containers" extension from the VS Code marketplace.  
      *(Note: This extension was previously called "Remote - Containers" but has since been renamed and integrated into Dev Containers.)*

    - **Docker**  
      Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (available for Windows, macOS, and Linux). Docker is required to manage and run the container environment.  
      - Start Docker and ensure it is running in the background.

    - Open the project folder in VS Code.

    - Press `F1` or `Ctrl+Shift+P`, type and select:

      ```
      Dev Containers: Reopen in Container
      ```

      Alternatively, click the green icon in the bottom-left corner of VS Code and select "Reopen in Container".

    - VS Code will detect the `.devcontainer` folder, build the development container, and install the necessary dependencies.

    - ![How to set dev container environment](./docs/dev-container-setup.gif "Dev container setup")

## Configure Azure AI service resource

### (Option 1) Use `azd` commands to automatically create temporary resources to run samples

1. Ensure you have permission to grant roles under your Azure subscription.

2. Log in to Azure:

    ```bash
    azd auth login
    ```

    If the above command does not work, try:

    ```bash
    azd auth login --use-device-code
    ```

    and follow the on-screen instructions.

3. Set up the environment and follow the prompts to choose your location:

    ```bash
    azd up
    ```

### (Option 2) Manually create resources and set environment variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).

2. In the Azure portal, navigate to **Access Control (IAM)** for your resource and assign yourself the role `Cognitive Services User`.  
   *Note: This is necessary even if you are the owner of the resource.*

3. Copy `notebooks/.env.sample` to `notebooks/.env`.

4. Fill in the **AZURE_AI_ENDPOINT** variable in `.env` with the endpoint from your Azure AI Services instance.

5. Log in to Azure:

    ```bash
    azd auth login
    ```

## Opening a Jupyter notebook and following the step-by-step guidance

Navigate to the `notebooks` directory and select the sample notebook you want to try. Since the Dev Container (in Codespaces or your local environment) is pre-configured with all necessary dependencies, you can directly execute each step in the notebook.

1. Select a notebook of interest from the `notebooks/` directory.  
   We recommend starting with `content_extraction.ipynb` to understand the basic concepts.  
   ![Select *.ipynb](/docs/create-codespace/2-Select%20file.ipynb.png)

2. Select the Kernel.  
   ![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)

3. Select the Python environment.  
   ![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)

4. Run the notebook cells.  
   ![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) designed to process and ingest content of any type (documents, images, audio, and video) into a user-defined output format.

Content Understanding streamlines reasoning over large volumes of unstructured data, accelerating time-to-value by generating outputs that can be integrated into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how the Content Understanding API can extract semantic information from files, such as OCR with tables in documents, audio transcription, and face analysis in video. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract fields from files, such as invoice amounts in documents, number of people in images, names mentioned in audio, or video summaries. Customize fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates evaluating conversational audio data transcribed by Content Understanding or Azure AI Speech efficiently to optimize processing quality and to enable cost-efficient re-analysis. Based on the [field_extraction.ipynb](notebooks/field_extraction.ipynb) sample. |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Demonstrates how to improve field extraction performance by training with a few labeled samples provided to the API. *Note: This feature is currently available for document scenarios only.* |
| [management.ipynb](notebooks/management.ipynb) | Shows how to create a minimal analyzer, list all analyzers in your resource, and delete analyzers you no longer need. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Demonstrates how to enroll people’s faces from images and build a Person Directory. |

## More Samples using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)  
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** — This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos is subject to those third parties’ policies.

* **Data Collection** — The software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve products. You may disable telemetry as described in this repository. Additionally, some software features may enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable law, including providing appropriate notices to your users along with a copy of Microsoft’s privacy statement. The privacy statement is located at https://go.microsoft.com/fwlink/?LinkID=824704. You can learn more about data collection and use in the help documentation and privacy statement. Your use of this software constitutes your consent to these practices.