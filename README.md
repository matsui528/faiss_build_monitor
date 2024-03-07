# Faiss Build Monitor
[![Build Faiss](https://github.com/matsui528/faiss_build_monitor/actions/workflows/build_faiss.yml/badge.svg)](https://github.com/matsui528/faiss_build_monitor/actions/workflows/build_faiss.yml)

Check faiss-cpu from conda works or not.

- [Workflow](.github/workflows/build_faiss.yml)
- [Result](https://github.com/matsui528/faiss_build_monitor/actions/workflows/build_faiss.yml)

## Matrix
Try the following combination of the configuration. 
- os
  - ubuntu-latest
  - macos-latest
  - windows-latest
- python-version
  - 3.9
  - 3.10
- faiss-label
  - main
  - nightly
- faiss-version
  - 1.8.0


## Todo
- Build from source
- [conda-forge](https://anaconda.org/conda-forge/faiss)
- [pip faiss-cpu](https://github.com/kyamagu/faiss-wheels/)
- faiss-gpu? But how?
