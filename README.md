# OCR_APP

OCR_APP is a simple Flask-based web application that converts unsearchable PDF files into searchable PDF files using OCR (Optical Character Recognition) technology. The app leverages the `ocrmypdf` library to perform the OCR processing.

## Features

- Upload a PDF file through a web interface
- Convert unsearchable PDF files to searchable PDF files
- Download the processed, searchable PDF file

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Sahilkumar19/OCR_APP.git
    cd OCR_APP
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    > Note: Ensure you have `ocrmypdf` and its dependencies installed. You can install `ocrmypdf` using pip:
    >
    > ```bash
    > pip install ocrmypdf
    > ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Navigate to the application in your web browser.
2. Upload a PDF file by clicking the "Choose File" button and selecting the file from your computer.
3. Click the "Upload and Process" button to start the OCR process.
4. Once the OCR processing is complete, a link will be provided to download the processed, searchable PDF file.

## Project Structure

OCR_APP/
├── app.py
├── templates/
│ └── index.html
├── static/
│ └── processed_pdfs/
├── requirements.txt
└── README.md


- **app.py**: The main Flask application file that contains routes and the OCR processing logic.
- **templates/**: Directory containing HTML templates for the web interface.
- **static/processed_pdfs/**: Directory where processed PDFs are saved.
- **requirements.txt**: File containing the list of Python dependencies.

## File Descriptions

### app.py

This file contains the main Flask application code. Key components include:

- **Configuration**: Sets the upload folder for storing processed PDFs.
- **OCR Function**: Utilizes `ocrmypdf` to convert unsearchable PDFs to searchable PDFs.
- **Routes**:
  - `/`: Handles file uploads and triggers the OCR processing.
  - `/uploads/<filename>`: Serves the processed, searchable PDF file for download.

### index.html

The HTML template provides a simple interface for users to upload PDF files. Key elements include:

- File upload form with `POST` method and `multipart/form-data` encoding type.
- Conditional message displaying a download link for the processed file after successful upload and processing.

## Dependencies

- Flask
- ocrmypdf

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a pull request or open an issue in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- The `ocrmypdf` library for providing the OCR functionality.
- Flask, for making web development simple and intuitive.


