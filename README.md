### Local environment

1. Ensure the following tools are installed:

    * [Azure Developer CLI (azd)](https://aka.ms/install-azd)
    * [Python 3.11+](https://www.python.org/downloads/)
    * [Git LFS](https://git-lfs.com/)

2. Create a new directory named `azure-ai-content-understanding-python` and clone this template into it using the `azd` CLI:
    ```
    azd init -t azure-ai-content-understanding-python
    ```
    Alternatively, you can use Git to clone the repository:
    ```
    git clone https://github.com/Azure-Samples/azure-ai-content-understanding-python.git
    cd azure-ai-content-understanding-python
    ```
    - **Important:** If you use `git clone`, ensure Git LFS is installed and run `git lfs pull` to download sample files in the `data` directory:
      ```shell
      git lfs install
      git lfs pull
      ```

3. Set up the Development Container Environment

  - Install tools to support dev containers:

    - **Visual Studio Code**  
      Download and install [Visual Studio Code](https://code.visualstudio.com/).

    - **Dev Containers Extension**  
      In the VS Code Extensions Marketplace, install the extension named "Dev Containers".  
      (This extension was previously called "Remote - Containers" but has since been renamed and integrated into Dev Containers.)

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
      Alternatively, click the green icon in the lower-left corner of VS Code and select "Reopen in Container".
    - VS Code will automatically detect the `.devcontainer` folder, build the development container, and install the necessary dependencies.
    - ![How to set dev container environment](./docs/dev-container-setup.gif "dev container setup")

## Configure Azure AI Service Resource

### (Option 1) Use `azd` commands to auto-create temporary resources and run the sample

1. Ensure you have permissions to grant roles under your subscription.

2. Login to Azure:
    ```shell
    azd auth login
    ```
    If this command fails, try:
    ```shell
    azd auth login --use-device-code
    ```
    and follow the on-screen instructions.

3. Set up the environment by following the prompts to choose a location:
    ```shell
    azd up
    ```


### (Option 2) Manually create resources and set environment variables

1. Create an [Azure AI Services resource](docs/create_azure_ai_service.md).

2. Navigate to `Access Control (IAM)` in your resource and assign yourself the `Cognitive Services User` role.  
   - This step is required even if you are the resource owner.

3. Copy `notebooks/.env.sample` to `notebooks/.env`.

4. Update **AZURE_AI_ENDPOINT** in the `.env` file with the endpoint from your Azure AI Services resource in the Azure portal.

5. Login to Azure:
   ```shell
   azd auth login
   ```

## Open a Jupyter Notebook and Follow the Step-by-Step Guidance

Navigate to the `notebooks` directory and open the sample notebook of your choice. Since the Dev Container (in Codespaces or your local environment) is pre-configured with the necessary environment, you can execute each step directly in the notebook.

1. Select a notebook of interest from the `notebooks/` directory.  
   We recommend starting with `content_extraction.ipynb` to understand the basic concepts.  
   ![Select *.ipynb](/docs/create-codespace/2-Select%20file.ipynb.png)

2. Select the Kernel  
   ![Select Kernel](/docs/create-codespace/3-Select%20Kernel.png)

3. Select Python Environment  
   ![Select Python Environment](/docs/create-codespace/4-Select%20Python%20Environment.png)

4. Run the notebook  
   ![Run](/docs/create-codespace/5-Run.png)

## Features

Azure AI Content Understanding is a new generative AI-based [Azure AI service](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview), designed to process and ingest content of any type—including documents, images, audio, and video—into user-defined output formats. Content Understanding streamlines reasoning over large volumes of unstructured data, accelerating time-to-value by generating outputs that integrate seamlessly into automation and analytical workflows.

## Samples

| File | Description |
| --- | --- |
| [content_extraction.ipynb](notebooks/content_extraction.ipynb) | Demonstrates how the Content Understanding API extracts semantic information from your file—for example, OCR with tables in documents, audio transcription, and face analysis in videos. |
| [field_extraction.ipynb](notebooks/field_extraction.ipynb) | Shows how to create an analyzer to extract fields from your file. Examples include extracting invoice amounts from documents, counting people in images, identifying names mentioned in audio, or summarizing video content. You can customize fields by creating your own analyzer templates. |
| [conversational_field_extraction.ipynb](notebooks/conversational_field_extraction.ipynb) | Demonstrates efficient evaluation of conversational audio data previously transcribed using Content Understanding or Azure AI Speech. This enables re-analysis of data in a cost-effective way. This sample is based on [field_extraction.ipynb](notebooks/field_extraction.ipynb). |
| [analyzer_training.ipynb](notebooks/analyzer_training.ipynb) | Shows how to improve field extraction performance by training the API with a few labeled samples. *Note: This feature is currently available only for document scenarios.* |
| [management.ipynb](notebooks/management.ipynb) | Demonstrates how to create a minimal analyzer, list all analyzers in your resource, and delete unnecessary analyzers. |
| [build_person_directory.ipynb](notebooks/build_person_directory.ipynb) | Demonstrates how to enroll people’s faces from images and build a Person Directory. |

## More Samples Using Azure Content Understanding

- [Azure Search with Content Understanding](https://github.com/Azure-Samples/azure-ai-search-with-content-understanding-python)

- [Azure Content Understanding with OpenAI](https://github.com/Azure-Samples/azure-ai-content-understanding-with-azure-openai-python)

## Notes

* **Trademarks** – This project may include trademarks or logos of projects, products, or services. Authorized use of Microsoft trademarks or logos must comply with [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Modified versions of this project must not cause confusion or imply Microsoft sponsorship. Use of third-party trademarks or logos is subject to those third parties’ policies.

* **Data Collection** – This software may collect information about you and your usage patterns and send it to Microsoft. Microsoft may use this data to provide services and improve products. You can disable telemetry as described in this repository. Some features may enable you and Microsoft to collect data from your application users; if you use these features, you must comply with applicable laws, including providing appropriate notices and a copy of Microsoft’s privacy statement to your users. Microsoft’s privacy statement is available at https://go.microsoft.com/fwlink/?LinkID=824704. By using this software, you consent to these practices.