# Adobe Document Intelligence Challenge – PDF Processor via Docker

##  Overview

This repository contains a PDF processing solution designed to extract structured data from documents. It includes:

- `Heading Extractor`: Parses a PDF and extracts clean title/subheading hierarchy while avoiding table data.
- `Persona Document Reader`: Reads specific persona-style documents and extracts structured fields like name, date of birth, address, etc.

Both utilities are containerized using Docker for reproducibility and portability.

---

##  Approach

### 1. Heading Extractor

- **Goal**: Extract hierarchical headings from scanned or digitally-created PDFs while avoiding noise like table headers, footers, and filler text.
- **Library**:PymuPDF
- **Logic**:
- Heading extraction
1.bold
2.Centered
3.underlined 
4.larger font size  than others
5.font styles
6.Capitalized
7. Whitesapces + positions 
8.colored 

-sub heading extraction
1.colon
2.numbers
3.boldded but lesser than title
4.Capitalized
5.underlined
6.bulleted ,asteriks
7.postion+whitespace

Outline List:
Heading (H1)
 |
 |
 v
Sub heading 1(H2)

....

Json format



### 2. Persona Document Reader

- **Goal**: Extract identity and attribute fields from semi-structured persona documents.
- **Logic**:
  - Used Bag of words like dictionary for collecting revelant words of text from the extracted pdf
  - When rate accuracy the words matched>90% and Take and collect that alone
  - Then give td-idf for identifying the rank related to the accuracy given
  - Then return the rank+relevant heading extracted for that ranking from the list.

---

##  Project Structure

adobe_heading_extractor/
├── app/
│ ├── extract_outline.py 
│ ├── utils.py # Any helper functions
├── input/ # Input PDFs
├── output/ # Output JSONs
├── main.py # Entry point
├── requirements.txt # All Python dependencies
├── Dockerfile # Container build file


##  How to Build and Run the Solution

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/adobe-heading-extractor.git
cd adobe-heading-extractor

##Build Docker Image
##Run Docker Container
task-1
docker build -t adobe-heading-extractor .
docker run --rm -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" adobe-heading-extractor
docker run -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" adobe-heading-extractor



task-2
docker build -t persona-doc-reader .
docker run --rm -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" persona-doc-reader
docker run -d -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" --name persona-container persona-doc-reader




###Output Format

##task-1
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Section 1",
      "page": 1
    },
    ...
  ]
}

##task-2
{
  "name": "John Doe",
  "dob": "01 Jan 2000",
  "gender": "Male",
  "address": "123 Street, City"
}
