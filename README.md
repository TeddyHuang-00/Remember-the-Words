# Remember the Words

Simple, extensible web app to help remember words

_This is a project done in merely 2 hrs, so don't expect it to be perfect._

## Usage

You can access this app from [this link](https://teddyhuang-00-remember-the-words-main-b6ezoa.streamlitapp.com/) provided by [Streamlit Cloud](https://streamlit.io/cloud). Thank you, Streamlit!

## Contributing

_Please feel free to contribute._

You can [fork this repo](https://github.com/TeddyHuang-00/Remember-the-Words/fork) and [submit a pull request](https://github.com/TeddyHuang-00/Remember-the-Words/compare). You can also [file an issue](https://github.com/TeddyHuang-00/Remember-the-Words/issues/new/choose) to request a feature or bug fix.

If you are new to `Streamlit`, you can [learn more about it here](https://docs.streamlit.io/) or simply follow the [instruction](#deploy-locally) to quickly get started.

### Submitting new word lists

New word lists are welcome! Note that due to the original purpose of this project, the new submitted word lists should follow the following format guidelines:

- Extension doesn't matter
- Each word should be on a separate line
- Exact one `<Tab>` (`\t`) between extra info (like line number) and word with its meaning(s)
- The word meaning(s) should be separated by `<Space>-<Vertical bar>-<Space>`(`|`)
- Example:
  ```
  Line num.	Word Word meaning A | Word meaning B...
  ```

## Deploy locally

### Dependencies

```bash
pip3 install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

You can access the app at `http://localhost:8501/`, or use the `--server.port` option to specify a different port as follows:

```bash
streamlit run app.py --server.port=2022
```

## Acknoledgements

Huge thanks to and love for:

[![](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)]((https://docs.streamlit.io/))