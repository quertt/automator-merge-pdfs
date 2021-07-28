# automator-merge-pdfs

## About 

Automator workflow (Mac) for merging scanned PDFs (odd and even side) of double-sided documents. This workflow is based on a python script which reverses the PDF containing even pages and subsequently merges them with the odd pages.

## Getting Started

To get the Automator workflow up and running follow these simple steps.

### Prerequisites

Things you need to have installed:
* Python 3 (e.g. see https://docs.python-guide.org/starting/install3/osx/)

### Installation

1. Install PyPDF2: Open Terminal and execute:
  ```sh
  pip install PyPDF2 
  ```
2. Download merge.py and move file to /usr/local/bin/
3. Make merge.py executable: Open Terminal and execute:
  ```sh
  chmod +x /usr/local/bin/merge.py
  ```
4. Get Python3 path:
  ```sh
  which python3
  ```
5. Create Quick Action in Automator
5.1. Open Automator, select "Quick Action" and set workflow to receive PDF-files.
5.2. Add a "Run Shell Script"-block, set "Pass input" to "as arguments" and paste:
  ```sh
  export PATH=/usr/local/bin/:$PATH
  PASTE_FROM_STEP_4 /usr/local/bin/merge.py "$@"
  ```
  Remember to replace 'PASTE_FROM_STEP_4' with the output from step 4.
6. Save Quick Action, e.g. as 'Combine scanned PDFs'


## Usage

In Finder select two PDFs to be combined, right-click and select Quick Action/'Combine scanned PDFs'


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!--## License-->
