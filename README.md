# Remember the Words

Simple, extensible web app to help remember words

_This is a project done in merely 2 hrs, so don't expect it to be perfect._

## Usage

You can [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://teddyhuang-00-remember-the-words-main-b6ezoa.streamlitapp.com/) provided by [Streamlit Cloud](https://streamlit.io/cloud), or alternatively, you can directly use this app in the follow frame. Thank you, Streamlit!

<iframe loading="lazy" src="https://teddyhuang-00-remember-the-words-main-b6ezoa.streamlitapp.com/?embedded=true" style="
                        width: 100%;
                        border: none;
                        height: 400px
                    "></iframe>

## Contributing

_Please feel free to contribute._

You can [fork this repo](https://github.com/TeddyHuang-00/Remember-the-Words/fork) and [submit a pull request](https://github.com/TeddyHuang-00/Remember-the-Words/compare). You can also [file an issue](https://github.com/TeddyHuang-00/Remember-the-Words/issues/new/choose) to request a feature or bug fix.

If you are new to `Streamlit`, you can [learn more about it here](https://docs.streamlit.io/) or simply follow the [instruction](#deploy-locally) to quickly get started.

### Submitting new word lists

New word lists are welcome! Note that due to the original purpose of this project, the new submitted word lists should follow the following format guidelines:

- Extension doesn't matter
- Each word should be on a separate line
- **EXACTLY ONE** `<Tab>` (`\t`) between extra info (like line number) and word with its meaning(s)
- **AT LEAST ONE** `<Space>` between each word and its meaning(s), although one space is enough and is recommended. Note that you need to make sure it is the **FIRST** `<Space>` after the `<Tab>`
- **NO** `<Space>` should be in the word itself
- The word meaning(s) should be separated by `<Space>-<Vertical bar>-<Space>`(`|`)
- Example:
  ```
  17	un(e) adj.num. 一【one】 | art. indéf. ( des) 一个（一些）【a（≈some）】
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

Huge shoutout to

[![](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)](<(https://docs.streamlit.io/)>)
