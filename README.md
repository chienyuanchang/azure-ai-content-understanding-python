# Azure AI Content Understanding Samples (Python)

Welcome! Content Understanding is a solution that analyzes and comprehends various media content—such as **documents, images, audio, and video**—transforming it into structured, organized, and searchable data.

- The samples in this repository default to the latest preview API version: **2025-05-01-preview**.
- This repository will soon provide more samples for new functionalities in Preview.2 **2025-05-01-preview**.
- As of May 2025, the 2025-05-01-preview API is available only in the regions documented in [Content Understanding region and language support](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/language-region-support).
- To access the sample code for version 2024-12-01-preview, please check out the corresponding Git tag `2024-12-01-preview` or download it directly from the [release page](https://github.com/Azure-Samples/azure-ai-content-understanding-python/releases/tag/2024-12-01-preview).

## Getting Started

You can run the samples either in GitHub Codespaces or in your local environment. For a smoother, hassle-free experience, we recommend starting with Codespaces.

### GitHub Codespaces

You can run this repository virtually using GitHub Codespaces, which opens a web-based VS Code instance in your browser.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=899687170&ref=main&geo=UsEast&devcontainer_path=.devcontainer%2Fdevcontainer.json)

After clicking the link above, please follow the steps below to set up your Codespace.

1. Create a new Codespace by selecting the main branch, your preferred Codespace region, and the 2-core machine type, as shown in the screenshot below.  
![Create CodeSpace](/docs/create-codespace/1-Create%20Codespace.png)

2. Once the Codespace is ready, open the terminal and follow the instructions in the "Configure Azure AI service resource" section to set up a valid Content Understanding resource.

### Local Environment

1. Ensure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)
    * [Python 3.11+](https://www.python.org/downloads/)
    * [Git LFS](https://git-lfs.com/)

2. Create a new directory named `azure-ai-content-understanding-python` and clone this repository into it using the `azd` CLI:

    azd init -t azure-ai-content-understanding-python

    Alternatively, you can clone the repository using Git:

    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git  
    cd azure-ai-content-understanding-python

    - **Important:** If you choose to use `git clone`, make sure to install Git LFS and run `git lfs pull` to download sample files in the `data` directory:

      git lfs install  
      git lfs pull

3. Set up the Dev Container Environment:

  - Install tools required to support dev containers:

    - **Visual Studio Code**  
      Download and install [Visual Studio Code](https://code.visualstudio.com/).

    - **Dev Containers Extension**  
      In the VS Code extension marketplace, install the extension named "Dev Containers".  
      (This extension was previously called "Remote - Containers" but has since been renamed and integrated into Dev Containers.)

    - **Docker**  
      Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (available for Windows, macOS, and Linux).  
      Docker is used to manage and run the container environment.  
      - Start Docker and ensure it is running in the background.

  - Open the project and start the Dev Container:

    - Open the project folder in VS Code.  
    - Press `F1` or `Ctrl+Shift+P`, then type and select:  
      `Dev Containers: Reopen in Container`  
      Alternatively, click the green icon in the lower-left corner of VS Code and select "Reopen in Container".  
    - VS Code will automatically detect the `.devcontainer` folder, build the development container, and install the necessary dependencies.  
    - ![How to set dev container environment](./docs/dev-container-setup.gif "Dev container setup")

## Configure Azure AI Service Resource

### (Option 1) Use `azd` Commands to Automatically Create Temporary Resources for Running Samples

1. Ensure you have the necessary permissions to grant roles under your Azure subscription.

2. Login to Azure:

    azd auth login

    If the above command doesn't work, try the following and follow the on-screen instructions:

    azd auth login --use-device-code

3. Set up the environment by following the prompts to choose location:

    azd up

### (Option 2) Manually Create Resources and Set Environment Variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).

2. In your Azure portal, go to `Access Control (IAM)` for the resource and grant yourself the `Cognitive Services User` role:  
   - This step is required even if you are the owner of the resource.

3. Copy `notebooks/.env.sample` to `notebooks/.env`.

4. Fill in the **AZURE_AI_ENDPOINT** variable with the endpoint from your Azure AI Services instance in the Azure portal.

5. Login to Azure:

    azd auth login

## Open a Jupyter Notebook and Follow Step-by-Step Guidance

Navigate to the `notebooks` directory and select the sample notebook you are interested in. Since the Dev Container (in Codespaces or your local environment) is pre-configured with the necessary environment, you can execute each step in the notebook directly.

1. Select a notebook of interest from the `notebooks/` directory. We recommend starting with `content_extraction.ipynb` to understand the basic concepts.  
   ![Select *.ipynb](/docs/create-codespace/2-Select%20file.ipynb.png)

2. Select the Kernel.  
   ![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)

3. Select the Python environment.  
   ![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)

4. Run the notebook.  
   ![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new Generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview), designed to process and ingest content of any type (documents, images, audio, and video) into a user-defined output format. Content Understanding streamlines reasoning over large volumes of unstructured data, accelerating time-to-value by generating outputs that can be integrated into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how the Content Understanding API helps extract semantic information from files. Examples include OCR with tables in documents, audio transcription, and face analysis in video. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract fields from your files, such as invoice amounts in documents, counts of people in images, names mentioned in audio, or summaries of videos. You can customize fields by creating your own analyzer template. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates evaluating conversational audio data that has been transcribed with Content Understanding or Azure AI Speech to optimize processing quality and enable cost-efficient re-analysis. This sample builds upon [field_extraction.ipynb](notebooks/field_extraction.ipynb). |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to improve field extraction performance by training with a few labeled samples. Note: This feature is currently available only for document scenarios. |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates how to create a minimal analyzer, list all analyzers in your resource, and delete unnecessary analyzers. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Demonstrates how to enroll people's faces from images and build a Person Directory. |

## More Samples Using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)  
- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** - This project may contain trademarks or logos for various projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos is subject to those third parties’ policies.

* **Data Collection** - The software may collect information about you and your use of the software and send it to Microsoft. Microsoft may use this information to provide services and improve products and services. You may turn off telemetry as described in the repository. Some features in the software may enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable laws, including providing appropriate notices to users of your applications along with a copy of Microsoft’s privacy statement, located at https://go.microsoft.com/fwlink/?LinkID=824704. Your use of the software constitutes consent to these practices.