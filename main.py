import os
import io
import streamlit as slt
import numpy as np

R8W, RAW, WL, GS = slt.tabs(
    ["Random 8 words", "Random all words", "Word list", "Global settings"]
)


@slt.cache(allow_output_mutation=True)
def parse_raw_content(content: list[str]):
    word_list = [x.strip("\n").strip().replace(", ", ",").split("\t") for x in content]
    word_list = [x[1].split(" ", 1) for x in word_list]
    word_list = [(x[0], x[1].strip().split(" | ")) for x in word_list]
    return word_list


@slt.cache(allow_output_mutation=True)
def get_word_list(file_path):
    with open(file_path, "r") as f:
        word_list = f.readlines()

    return parse_raw_content(word_list)


def show_word(
    word, check_box_id=None, check_box_info="Add to word list?", expanded=False
):
    with slt.expander(word[0], expanded=expanded):
        for meaning in word[1]:
            slt.markdown(meaning)
        if check_box_id is not None:
            slt.checkbox(check_box_info, value=False, key=check_box_id)


def shuffle_words(word_list):
    return np.random.permutation(word_list)


@slt.cache()
def dump_word_list(word_list):
    content = "\n".join(
        [str(i) + "\t" + x[0] + " " + " | ".join(x[1]) for i, x in enumerate(word_list)]
    )
    return content


if "file_path" not in slt.session_state:
    slt.session_state["file_path"] = "./word_lists/french-800.txt"

if "word_list" not in slt.session_state:
    slt.session_state["word_list"] = get_word_list(slt.session_state["file_path"])

if "review_list" not in slt.session_state:
    slt.session_state["review_list"] = []

with GS:
    slt.session_state["file_path"] = slt.selectbox(
        "Word list to use",
        os.listdir("./word_lists"),
        index=0,
        format_func=lambda x: x.split(".")[0],
    )

with R8W:
    slt.header("Random 8 words")
    expanded = slt.checkbox("Toggle expend", key="R8W_expanded", value=False)
    with slt.form("Random 8 words", clear_on_submit=True):
        R8W_L, R8W_R = slt.columns(2)
        word_list = [
            slt.session_state["word_list"][i]
            for i in np.random.choice(
                len(slt.session_state["word_list"]), 8, replace=False
            )
        ]
        with R8W_L:
            for i, word in enumerate(word_list[:4]):
                show_word(word, i, expanded=expanded)
        with R8W_R:
            for i, word in enumerate(word_list[4:]):
                show_word(word, i + 4, expanded=expanded)
        _, centering, _ = slt.columns([3, 2, 3])
        with centering:
            if slt.form_submit_button("Add selected words"):
                for i in range(8):
                    if slt.session_state[str(i)]:
                        slt.session_state["review_list"].append(word_list[i])

    _, centering, _ = slt.columns([3, 2, 3])
    with centering:
        if slt.button("Random new ones"):
            slt.experimental_rerun()

with RAW:
    slt.header("Random all words")
    expanded = slt.checkbox("Toggle expend", key="RAW_expanded", value=False)
    with slt.form("Random all words", clear_on_submit=True):
        word = slt.session_state["word_list"][
            np.random.choice(len(slt.session_state["word_list"]))
        ]
        show_word(word, check_box_id="AW", expanded=expanded)
        _, centering, _ = slt.columns([3, 2, 3])
        with centering:
            if slt.form_submit_button("Show me next one"):
                if slt.session_state["AW"]:
                    slt.session_state["review_list"].append(word)

with WL:
    slt.header("Word list")
    if len(slt.session_state["review_list"]) > 0:
        expanded = slt.checkbox("Toggle expend", key="WL_expanded", value=False)
        with slt.form("Word list", clear_on_submit=True):
            for i, word in enumerate(slt.session_state["review_list"]):
                show_word(word, f"d_{i}", "Remove from word list?", expanded)
            _, centering, _ = slt.columns([3, 2, 3])
            with centering:
                if slt.form_submit_button(
                    "Confirm delete",
                    help="This will remove the word from this list, but it can appear again in the future!",
                ):
                    slt.session_state["review_list"] = [
                        slt.session_state["review_list"][i]
                        for i in range(len(slt.session_state["review_list"]))
                        if not slt.session_state[f"d_{i}"]
                    ]
                    slt.experimental_rerun()

        _, centering, _ = slt.columns([3, 2, 3])
        with centering:
            slt.download_button(
                label="Download word list",
                data=dump_word_list(slt.session_state["review_list"]),
                file_name="word_list.txt",
                mime="text/plain",
            )
    else:
        slt.subheader("No words to review!")
        slt.subheader("Get some words or get to sleep!")
        with slt.form("Load from file", clear_on_submit=True):
            file = slt.file_uploader(
                "Load word list from file",
            )
            _, centering, _ = slt.columns([4, 1, 4])
            with centering:
                if slt.form_submit_button("Load"):
                    if file is None:
                        slt.warning("No file uploaded")
                        slt.experimental_rerun()
                    file = io.StringIO(file.read().decode("utf-8"))
                    slt.session_state["review_list"] = parse_raw_content(
                        file.readlines()
                    )
                    slt.experimental_rerun()

# slt.session_state
