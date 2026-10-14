# Anatomy Education Assistant — Extended RAG Prototype

This repository extends the anatomy-focused retrieval-augmented generation (RAG) assistant with text retrieval, image and table lookup, chapter exercise support, PDF output and flowchart generation. The interface is built with Streamlit, retrieval uses local ChromaDB collections, and generated responses use Google's Gemini model.

## Features
- Natural-language questions over a local anatomy knowledge collection.
- Retrieval of related anatomy images and tables from metadata-backed collections.
- Chapter/back-of-book exercise retrieval with generated answers.
- PDF export of generated exercise content.
- Experimental flowchart generation from text descriptions.

## Key files
- `st_app.py` — main Streamlit interface and retrieval/generation functions.
- `requirements.txt` — Python package dependencies.
- `image_filenames.csv`, `csv_filenames.csv` — metadata mapping image/table descriptions to assets.
- `imageExtract.py`, `img_fetch.py`, `tab_fetch.py`, `bookBack.py` — supporting extraction or ingestion scripts.
- `collection/` — expected ChromaDB persistent store with text, image, table and book-back collections.
- `anatomy_vol_3_edited_final.pdf`, `anatomy_vol_3_book_back.pdf` — source materials used by the project.

## Setup
```bash
git clone https://github.com/Saikabilane/RAG-final.git
cd RAG-final
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

Prepare the local ChromaDB collections and image/table assets using the helper scripts and ensure the expected CSV files and directories are available. Then launch:
```bash
streamlit run st_app.py
```

## API key security — important
Configure Gemini credentials using environment variables or a local, untracked configuration file. **Do not commit API keys to source control.** This repository's application source has contained hard-coded credential strings; revoke/rotate any real keys that were committed, remove them from the code, and load replacement keys from the environment. Deleting a key from the latest version alone does not remove it from Git history.

## Limitations
This is an educational prototype. Generated answers can be inaccurate; verify material against authoritative sources. It is not a substitute for professional medical advice.

## License
No license file is currently included; contact the repository owner for reuse permission.
