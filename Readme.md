Why This Exists

In Retrieval-Augmented Generation (RAG) systems, garbage in = garbage out. The real bottleneck isn’t model performance—it’s unstructured, noisy, bloated content that chokes your vector store and pollutes semantic search.

KenCompressor is built to fix that.

It's a modular, zero-bloat content-to-markdown compression engine. Think of it as a universal translator that strips away nonsense and gives LLMs exactly what they need: structured, readable, searchable knowledge. No fluff, no formatting hell, no broken transcripts or orphaned headers.

You can throw almost anything at it—PDFs, DOCX, HTML, images, audio, video—and it will compress and convert it into clean, token-efficient markdown with embedded metadata headers, structural cues, and optional scene descriptions or speaker labels.


---

Core Philosophy

Execution over elegance – It’s built to work, not impress.

Structural fidelity – Retain meaningful structure (titles, headings, paragraphs, tables).

Token awareness – Compress intelligently, keep only what matters.

Plug-and-play – Easily integrates into RAG pipelines, chunkers, or memory stores.

Future-proofing – Vision-language model support, OCR, STT, and metadata tagging already built-in.



---

How It Works

1. Input Detection

KenCompressor identifies the input file type via extension:

pdf, docx, pptx, html

jpg/png/gif/bmp

mp3/wav/m4a

mp4/avi/mov


Each format has its own extractor with optional enhancements (scene descriptions, OCR, etc).


---

2. File Processing

Depending on the file type, it routes to a dedicated method:

Each method:

Extracts the content

Applies structural markdown formatting

Prepends a metadata block (filename, type, word/token est.)

Returns markdown as string or file output



---

3. Optional Enhancements

Segmented Transcription – Audio/video is chunked into 30s blocks with speaker tags.

Scene Descriptions – Vision model support via BLIP placeholder (custom VLMs pluggable).

Tables – Auto-extracted from HTML and converted to markdown format using pandas.

Fallbacks – If OCR/STT fails, KenCompressor still returns usable output with logging.



---

Integration Use Case

RAG Pipelines – Pre-process documents before chunking/indexing.

Semantic Search – Compress large corpora without semantic loss.

Knowledge Graphs – Tag and convert into markdown snapshots for vector enrichment.

AI Video Tools – Extract scripts and metadata from assets.



---

TODOs

Add deep speaker diarization

Plug real VLM integration (BLIP, CLIP)

Improve PPTX slide parsing

Expand metadata for search tags



---

Closing Note

KenCompressor is designed for builders who hate inefficiency.
It’s not just about compression—it’s about clarity for machines.

If you feed your LLM trash, don’t be surprised when it spits out confusion.
This tool ensures your input is signal, not noise.
