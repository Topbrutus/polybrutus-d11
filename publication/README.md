# Polybrutus D11 - release protocol

A mathematical preprint with its PDF and editable source, a complete 120-pair JSON certificate, and a fixed Git-tag source ZIP.

1. Verify all symbolic and independent rational tests.
2. Prepare a private GitHub repository, CI and SHA256SUMS blob index.
3. Freeze a successful CI commit as tag v0.1.0.
4. Make a Git archive directly from that tag; record SHA-256 and size.
5. Create a unique controlled Zenodo REST draft and verify the author, license, explicit AI disclosure and three binary file checksums.
6. Make GitHub public, verify the tag against public API, publish the existing Zenodo draft, verify Zenodo DOI and all three public files.
7. Add DOI back to README, CITATION.cff, manifest and the X72 Memoria series index. Do not move the frozen science tag.

Avoid enabling automatic Zenodo harvesting of GitHub releases in parallel with direct REST deposit (would create duplicate records). No secrets, tokens or private chats in the public archive.
