"""LearnCraft AI Streamlit MVP.

This MVP implements the documented 3-step workflow without LLM integration:

1. Mode Selection
2. Topic/File Input
3. Output Selection and generation placeholder
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import streamlit as st


APP_TITLE: Final[str] = "LearnCraft AI"

MODES: Final[list[str]] = [
    "Lecture-Ready Presentation Pack",
    "Study Guide",
    "Focused Deep Dive",
]

OUTPUT_OPTIONS: Final[dict[str, list[str]]] = {
    "Lecture-Ready Presentation Pack": [
        "Slides Only",
        "Slides + Speaker Notes",
        "Full Presentation Pack",
    ],
    "Study Guide": [
        "Quick Learning",
        "Solid Understanding",
        "Deep Learning",
        "Implementation Ready",
    ],
    "Focused Deep Dive": [
        "Lecture Style",
        "Study Guide",
        "Advanced Concept Brief",
        "Just One Topic",
    ],
}

MODE_DESCRIPTIONS: Final[dict[str, str]] = {
    "Lecture-Ready Presentation Pack": "Create presentation-ready teaching material with slide-oriented structure.",
    "Study Guide": "Create structured learning material for understanding, review, and retention.",
    "Focused Deep Dive": "Explore a narrow concept with depth, precision, and minimal breadth.",
}

OUTPUT_DESCRIPTIONS: Final[dict[str, str]] = {
    "Slides Only": "Slide titles, concise bullets, and visual guidance.",
    "Slides + Speaker Notes": "Slides plus presenter notes for each section.",
    "Full Presentation Pack": "Slides, notes, objectives, flow, examples, recap, and activities.",
    "Quick Learning": "Essential concepts, fast recall, and concise examples.",
    "Solid Understanding": "Structured explanations, examples, and conceptual links.",
    "Deep Learning": "Deeper reasoning, edge cases, misconceptions, and layered examples.",
    "Implementation Ready": "Workflow, setup, usage patterns, mistakes, exercise, and next steps.",
    "Lecture Style": "Focused teachable explanation with examples and recap.",
    "Study Guide": "Learner-facing structure with review support.",
    "Advanced Concept Brief": "Concise expert-level analysis and nuanced insights.",
    "Just One Topic": "Single-topic depth with minimal contextual prerequisites.",
}

DEFAULT_STATE: Final[dict[str, object]] = {
    "step": 1,
    "mode": "",
    "topic": "",
    "uploaded_file_name": "",
    "uploaded_file_type": "",
    "uploaded_file_size": 0,
    "output_type": "",
    "generated": False,
}


@dataclass(frozen=True)
class UploadedFileSummary:
    """Small serializable summary of the uploaded file."""

    name: str
    file_type: str
    size: int


def initialize_state() -> None:
    """Initialize all Streamlit session state keys used by the app."""
    for key, value in DEFAULT_STATE.items():
        st.session_state.setdefault(key, value)


def set_step(step: int) -> None:
    """Navigate to a workflow step."""
    st.session_state.step = step
    st.session_state.generated = False


def reset_output_if_mode_changed() -> None:
    """Clear incompatible output selection after mode changes."""
    mode = st.session_state.mode
    if st.session_state.output_type not in OUTPUT_OPTIONS.get(mode, []):
        st.session_state.output_type = ""
    st.session_state.generated = False


def has_valid_input() -> bool:
    """Return True when Step 2 has a topic, file, or both."""
    return bool(st.session_state.topic.strip() or st.session_state.uploaded_file_name)


def capture_uploaded_file_summary() -> None:
    """Persist lightweight uploaded-file metadata in session state."""
    uploaded_file = st.session_state.get("file_upload")
    if uploaded_file is None:
        st.session_state.uploaded_file_name = ""
        st.session_state.uploaded_file_type = ""
        st.session_state.uploaded_file_size = 0
        return

    summary = UploadedFileSummary(
        name=uploaded_file.name,
        file_type=uploaded_file.type or "Unknown",
        size=uploaded_file.size,
    )
    st.session_state.uploaded_file_name = summary.name
    st.session_state.uploaded_file_type = summary.file_type
    st.session_state.uploaded_file_size = summary.size


def render_page_config() -> None:
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="LC",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def render_styles() -> None:
    st.markdown(
        """
        <style>
            .block-container {
                max-width: 1080px;
                padding-top: 2rem;
                padding-bottom: 3rem;
            }

            .hero {
                border: 1px solid #d9e2ec;
                border-radius: 8px;
                padding: 1.2rem 1.35rem;
                background: #f7fafc;
                margin-bottom: 1.2rem;
            }

            .hero h1 {
                font-size: 2.1rem;
                line-height: 1.2;
                margin: 0 0 0.35rem 0;
                color: #102a43;
                letter-spacing: 0;
            }

            .hero p {
                color: #52606d;
                margin: 0;
                font-size: 1rem;
            }

            .step-card {
                border: 1px solid #d9e2ec;
                border-radius: 8px;
                padding: 1rem 1.1rem;
                background: #ffffff;
                min-height: 96px;
            }

            .step-card strong {
                color: #102a43;
            }

            .muted {
                color: #627d98;
                font-size: 0.92rem;
            }

            .summary-panel {
                border: 1px solid #bcccdc;
                border-radius: 8px;
                padding: 1rem 1.1rem;
                background: #f8fbff;
            }

            .placeholder-output {
                border: 1px dashed #829ab1;
                border-radius: 8px;
                padding: 1.1rem;
                background: #f0f4f8;
            }

            div[data-testid="stButton"] > button {
                border-radius: 8px;
                min-height: 2.6rem;
                font-weight: 600;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    st.markdown(
        """
        <div class="hero">
            <h1>LearnCraft AI</h1>
            <p>Transform a topic or document into a structured learning experience in three guided steps.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_progress() -> None:
    labels = [
        ("1", "Mode Selection"),
        ("2", "Input"),
        ("3", "Output Selection"),
    ]

    columns = st.columns(3)
    for index, (number, label) in enumerate(labels, start=1):
        state_label = "Current" if st.session_state.step == index else "Complete" if st.session_state.step > index else "Pending"
        with columns[index - 1]:
            st.markdown(
                f"""
                <div class="step-card">
                    <strong>Step {number}</strong><br />
                    {label}<br />
                    <span class="muted">{state_label}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_step_1() -> None:
    st.subheader("Step 1: Mode Selection")
    st.write("Choose the learning experience you want to create.")

    selected_mode = st.radio(
        "Mode",
        MODES,
        index=MODES.index(st.session_state.mode) if st.session_state.mode in MODES else None,
        captions=[MODE_DESCRIPTIONS[mode] for mode in MODES],
        key="mode",
        label_visibility="collapsed",
        on_change=reset_output_if_mode_changed,
    )

    st.session_state.mode = selected_mode or ""

    _, next_col = st.columns([1, 1])
    with next_col:
        st.button(
            "Next: Add Input",
            type="primary",
            use_container_width=True,
            disabled=not st.session_state.mode,
            on_click=set_step,
            args=(2,),
        )


def render_step_2() -> None:
    st.subheader("Step 2: Input")
    st.write("Enter a topic, upload a file, or provide both.")

    st.text_input(
        "Topic",
        key="topic",
        placeholder="Example: Transformer self-attention, OAuth 2.0 authorization code flow",
    )

    st.file_uploader(
        "Optional file upload",
        type=["txt", "md", "pdf", "docx", "pptx"],
        key="file_upload",
        on_change=capture_uploaded_file_summary,
        help="This MVP stores file metadata only. File parsing will be added later.",
    )

    if st.session_state.uploaded_file_name:
        size_kb = st.session_state.uploaded_file_size / 1024
        st.success(
            f"File selected: {st.session_state.uploaded_file_name} "
            f"({st.session_state.uploaded_file_type}, {size_kb:.1f} KB)"
        )

    valid_input = has_valid_input()
    if not valid_input:
        st.info("Enter a topic or upload a file to continue.")

    back_col, next_col = st.columns([1, 1])
    with back_col:
        st.button("Back", use_container_width=True, on_click=set_step, args=(1,))
    with next_col:
        st.button(
            "Next: Choose Output",
            type="primary",
            use_container_width=True,
            disabled=not valid_input,
            on_click=set_step,
            args=(3,),
        )


def render_request_summary() -> None:
    topic = st.session_state.topic.strip() or "Not provided"
    file_name = st.session_state.uploaded_file_name or "Not uploaded"
    output_type = st.session_state.output_type or "Not selected"

    st.markdown(
        f"""
        <div class="summary-panel">
            <strong>Current setup</strong><br />
            <span class="muted">Mode:</span> {st.session_state.mode}<br />
            <span class="muted">Topic:</span> {topic}<br />
            <span class="muted">File:</span> {file_name}<br />
            <span class="muted">Output:</span> {output_type}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_step_3() -> None:
    st.subheader("Step 3: Output Selection")
    st.write("Select the output format for the chosen mode.")

    render_request_summary()
    st.divider()

    options = OUTPUT_OPTIONS[st.session_state.mode]
    st.radio(
        "Output type",
        options,
        index=options.index(st.session_state.output_type) if st.session_state.output_type in options else None,
        captions=[OUTPUT_DESCRIPTIONS[option] for option in options],
        key="output_type",
        label_visibility="collapsed",
        on_change=lambda: setattr(st.session_state, "generated", False),
    )

    back_col, generate_col = st.columns([1, 1])
    with back_col:
        st.button("Back", use_container_width=True, on_click=set_step, args=(2,))
    with generate_col:
        if st.button(
            "Generate Learning Content",
            type="primary",
            use_container_width=True,
            disabled=not st.session_state.output_type,
        ):
            st.session_state.generated = True

    if st.session_state.generated:
        render_generation_placeholder()


def render_generation_placeholder() -> None:
    st.divider()
    st.markdown(
        f"""
        <div class="placeholder-output">
            <strong>Generation placeholder</strong><br />
            LearnCraft AI is ready to generate a <strong>{st.session_state.output_type}</strong>
            output for <strong>{st.session_state.mode}</strong>.<br /><br />
            LLM integration is intentionally not connected in this MVP. The next implementation phase
            will connect this workflow to the prompt architecture and content generation pipeline.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.header("MVP Status")
        st.write("No LLM integration yet.")
        st.write("Session state preserves selections across steps.")
        st.divider()
        if st.button("Start New", use_container_width=True):
            for key, value in DEFAULT_STATE.items():
                st.session_state[key] = value
            st.rerun()


def main() -> None:
    render_page_config()
    initialize_state()
    render_styles()
    render_sidebar()
    render_header()
    render_progress()
    st.divider()

    if st.session_state.step == 1:
        render_step_1()
    elif st.session_state.step == 2:
        render_step_2()
    else:
        if not st.session_state.mode:
            set_step(1)
            st.rerun()
        if not has_valid_input():
            set_step(2)
            st.rerun()
        render_step_3()


if __name__ == "__main__":
    main()
