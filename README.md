# Automated Image Processing Pipeline
### A DevOps CI/CD demonstration using Python, OpenCV, and GitHub Actions

## Introduction
This project demonstrates a complete **DevOps Continuous Integration (CI) pipeline** that automates image processing tasks. Designed for the Elective 4 Midterm, the system automatically detects new images uploaded to the directory, applies artistic filters (Vintage, Sketch, Saturation, Noise, Blur), and pushes the results back to the repository without human intervention. The goal is to simulate a workflow where code and assets are verified and processed automatically on every push.

## Pipeline Workflow
* **Trigger:** The workflow watches the `input/` directory on the `main` branch.
* **Process:** The `process_images.py` script runs, generating 5 variations for every image.
* **Validate:** The `test_script.py` ensures files are created and are valid images.
* **Deploy:** The system commits the new images as `github-actions[bot]` and pushes them back to the repo.

## Installation Instructions for Users
If you simply want to run the image processor on your local machine:

1.  **Clone the repository:**
    ```
    git clone <your-repo-url>
    ```

2.  **Prepare your Input:**
    Place your `.jpg`, `.png`, or `.jpeg` files into the `input/` folder.

3.  **Run the Processor:**
    Execute the python script to generate filtered images in the `output/` folder.
    ```
    python process_images.py
    ```

## Installation Instructions for Developers
To contribute to the code or run the full test suite, you need the development environment:

1.  **Install Dependencies:**
    Ensure you have Python 3.9+ installed, then run:
    ```
    pip install -r requirements.txt
    ```
    *Required Libraries:* `opencv-python-headless`, `numpy`, `pytest`.

2.  **Run Automated Tests:**
    Validate that the system is working correctly by running the test suite:
    ```
    python test_script.py
    ```

## Contributor Expectations
Our group simulates a real-world software development lifecycle (SDLC) using **Git Branching** and **Automated Testing**.

### Branching Strategy
We utilize a multi-branch workflow to allow parallel development:
* **`main`**: The production-ready branch (Managed by the DevOps Engineer).
* **`image-processing`**: The feature branch for Image Processing algorithms (Vintage, Pencil Sketch, Saturation, etc.).
* **`testing`**: The quality assurance branch for writing and validating automated tests.

### Development Phases & Workflow
Contributors followed a strict phased approach, as seen in our Pull Request history:
1.  **Phase 1 (Foundation):** The **Vintage Filter** was implemented first. The tester verified the output, and the DevOps Engineer merged it only after valid automated tests.
2.  **Phase 2 (Expansion):** We integrated **Pencil Sketch** and **Color Saturation**. These features were validated against file constraints before merging.
3.  **Phase 3 (Completion):** The final set of effects, **Noise Injection** and **Motion Blur**, were added in a separate PR to complete the feature set.
4.  **Phase 4 (Refinement):** We conducted a final round of bug fixes (fixing typos and main code errors) to ensure the pipeline runs smoothly.

**Communication:** All updates and merge conflicts were resolved synchronously via Discord.

## Known Issues
* **File Support:** The system strictly accepts `.jpg`, `.png`, and `.jpeg` files only. Any other file type uploaded to the input directory will be ignored to prevent errors.
* **Processing Time:** Large batch uploads (10+ high-res images) may slow down the GitHub Actions runner, though the timeout is set generously.
