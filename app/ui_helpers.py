import streamlit as st


def apply_css():
    st.markdown(
        """
        <style>
        @import url("https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,400&display=swap");

        :root {
            /* Slightly deeper mint-gray so white / glass panels read clearly vs. dark sidebar */
            --bg-page: #d8e6e2;
            --bg-page-2: #e0ebe8;
            /* Dual-tone canvas — stronger contrast so it reads on screen (theme often overrides weak gradients) */
            --bg-canvas-top: #a8c4b8;
            --bg-canvas-mid: #c5d8d0;
            --bg-canvas-bottom: #edf6f2;
            --bg-card: #ffffff;
            --border-soft: #c8dbd6;
            --border-sidebar: #d9ebe8;
            --teal-deep: #184b54;
            --teal-mid: #2a6570;
            --accent: #67c8bb;
            --accent-soft: #e8f7f4;
            --text-title: #20384a;
            --text-body: #4a6573;
            --text-muted: #607786;
            --shadow-sm: 0 1px 2px rgba(24, 75, 84, 0.06);
            --shadow-md: 0 8px 24px rgba(24, 75, 84, 0.08);
            --shadow-lg: 0 16px 48px rgba(15, 23, 42, 0.07);
            --radius-lg: 16px;
            --radius-md: 12px;
            --radius-pill: 999px;
            /* Type scale (rem) */
            --text-display: clamp(1.9rem, 2.8vw, 2.45rem);
            --text-lead: 1.0625rem;
            --text-section: 0.9375rem;
            --text-kpi-value: clamp(1.55rem, 2.15vw, 2rem);
            --text-kpi-value-lg: clamp(1.75rem, 2.45vw, 2.2rem);
            --leading-tight: 1.12;
            --leading-snug: 1.45;
            --leading-body: 1.58;
            --space-content-max: 1320px;
            --space-band: 2rem;
            --space-section: 1.35rem;
        }

        html, body, [class*="css"] {
            font-family: "DM Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
        }

        /* Let Streamlit’s canvas show through — theme often sets opaque grays on html/body */
        html,
        body {
            background: transparent !important;
        }

        /* Main column: readable measure + centered — must stay transparent so dual-tone is visible in margins */
        [data-testid="stMain"] {
            max-width: var(--space-content-max) !important;
            margin-left: auto !important;
            margin-right: auto !important;
            padding: 1.65rem clamp(1.25rem, 3vw, 2.25rem) 3rem !important;
            box-sizing: border-box;
            background: transparent !important;
        }

        [data-testid="stMain"] .block-container {
            background: transparent !important;
        }

        /* !important beats Streamlit theme inline background on these roots */
        .stApp,
        [data-testid="stAppViewContainer"] {
            background-color: var(--bg-canvas-mid) !important;
            /* Top = cooler slate-mint; bottom = airy recovery green. Cross grid + vignettes on top */
            background-image:
                url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='48' viewBox='0 0 48 48'%3E%3Cg fill='none' stroke='%23184b54' stroke-opacity='0.085' stroke-width='1.1'%3E%3Cpath d='M24 8v32M8 24h32'/%3E%3C/g%3E%3C/svg%3E"),
                radial-gradient(ellipse 70% 55% at 100% 0%, rgba(103, 200, 187, 0.22) 0%, transparent 52%),
                radial-gradient(ellipse 55% 50% at 0% 100%, rgba(24, 75, 84, 0.07) 0%, transparent 50%),
                linear-gradient(
                    175deg,
                    var(--bg-canvas-top) 0%,
                    #b6cfc4 14%,
                    var(--bg-canvas-mid) 36%,
                    #d6e8e1 62%,
                    var(--bg-canvas-bottom) 100%
                ) !important;
            background-repeat: repeat, no-repeat, no-repeat, no-repeat !important;
            background-size: 48px 48px, auto, auto, auto !important;
            background-position: 0 0, 0 0, 0 0, 0 0 !important;
            background-attachment: scroll !important;
        }

        [data-testid="stHeader"] {
            background: linear-gradient(
                180deg,
                rgba(190, 210, 204, 0.55) 0%,
                rgba(220, 235, 230, 0.35) 100%
            );
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(24, 75, 84, 0.11);
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(165deg, #0a2f36 0%, #0e3b44 38%, #124b54 72%, #15606a 100%);
            min-width: 288px !important;
            max-width: 288px !important;
            border-right: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 8px 0 40px rgba(8, 40, 46, 0.35);
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        /* Sidebar: default light text (inputs opt out below) */
        section[data-testid="stSidebar"] {
            color: rgba(255, 255, 255, 0.92) !important;
        }

        /* —— Brand —— */
        .sidebar-brand {
            padding: 0.15rem 0 1.1rem 0;
            margin-bottom: 0.25rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.14);
        }

        .sidebar-brand__mark {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 2.5rem;
            height: 2.5rem;
            border-radius: var(--radius-md);
            background: rgba(255, 255, 255, 0.14);
            border: 1px solid rgba(255, 255, 255, 0.22);
            color: #ffffff !important;
            font-size: 1.25rem;
            margin-bottom: 0.65rem;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
            backdrop-filter: blur(8px);
        }

        .sidebar-brand__title {
            font-size: 1.15rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: #ffffff !important;
            line-height: 1.2;
            margin: 0 0 0.35rem 0;
        }

        .sidebar-brand__tag {
            font-size: 0.78rem;
            font-weight: 600;
            color: rgba(255, 255, 255, 0.72) !important;
            letter-spacing: 0.02em;
            line-height: 1.35;
        }

        .sidebar-nav-label,
        .sidebar-filters-label {
            font-size: 0.68rem;
            font-weight: 800;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.48) !important;
            margin: 1rem 0 0.5rem 0;
        }

        .sidebar-filters-label {
            margin-top: 1.25rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.12);
        }

        /* Sidebar radio — Streamlit nests caption text in p/span with theme colors; force white */
        section[data-testid="stSidebar"] [data-testid="stRadio"] label {
            padding: 0.45rem 0.65rem !important;
            margin: 0.2rem 0 !important;
            border-radius: var(--radius-md) !important;
            border: 1px solid transparent !important;
            transition: background 0.15s ease, border-color 0.15s ease;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label p,
        section[data-testid="stSidebar"] [data-testid="stRadio"] label span,
        section[data-testid="stSidebar"] [data-testid="stRadio"] label div {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] [data-testid="stMarkdownContainer"] p,
        section[data-testid="stSidebar"] [data-testid="stRadio"] [data-testid="stMarkdownContainer"] span {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
            background: rgba(255, 255, 255, 0.08) !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
            background: rgba(255, 255, 255, 0.16) !important;
            border-color: rgba(255, 255, 255, 0.28) !important;
            font-weight: 700 !important;
        }

        section[data-testid="stSidebar"] [data-testid="stRadio"] input[type="radio"] {
            accent-color: #7fe8d8;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] span {
            color: rgba(255, 255, 255, 0.9) !important;
        }

        section[data-testid="stSidebar"] .stCaption {
            color: rgba(255, 255, 255, 0.72) !important;
        }

        /* Controls: white surfaces, dark typography (multiselect, search) */
        section[data-testid="stSidebar"] [data-baseweb="select"] > div {
            background: #ffffff !important;
            color: #184b54 !important;
            border: 1px solid rgba(24, 75, 84, 0.12) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.12) !important;
        }

        section[data-testid="stSidebar"] [data-baseweb="select"] svg {
            fill: #184b54 !important;
        }

        section[data-testid="stSidebar"] [data-baseweb="tag"] {
            background: #e8f7f4 !important;
            color: #0f4a52 !important;
            border: 1px solid rgba(103, 200, 187, 0.45) !important;
        }

        section[data-testid="stSidebar"] .stTextInput > div > div {
            background: #ffffff !important;
            border: 1px solid rgba(24, 75, 84, 0.12) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
        }

        section[data-testid="stSidebar"] .stTextInput input {
            background: #ffffff !important;
            color: #184b54 !important;
            border: none !important;
            border-radius: var(--radius-md) !important;
        }

        section[data-testid="stSidebar"] .stTextInput input::placeholder {
            color: #6b8790 !important;
        }

        /* Slider: white surface; label stays above on teal */
        section[data-testid="stSidebar"] [data-baseweb="slider"] {
            background: rgba(255, 255, 255, 0.97) !important;
            border-radius: var(--radius-md) !important;
            border: 1px solid rgba(24, 75, 84, 0.1) !important;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.12) !important;
            padding: 0.55rem 0.75rem 0.65rem 0.75rem !important;
            margin-bottom: 0.35rem !important;
        }

        section[data-testid="stSidebar"] [data-testid="stTickBarMin"],
        section[data-testid="stSidebar"] [data-testid="stTickBarMax"] {
            color: #40616b !important;
        }

        /* —— Page hero —— */
        .page-hero {
            margin-bottom: var(--space-band);
            padding-bottom: 1.35rem;
            border-bottom: 1px solid rgba(24, 75, 84, 0.11);
        }

        .page-hero__accent {
            width: 52px;
            height: 4px;
            border-radius: var(--radius-pill);
            background: linear-gradient(90deg, var(--accent) 0%, #2a9d8f 55%, #1f7a70 100%);
            margin-bottom: 1.05rem;
        }

        .page-title {
            font-size: var(--text-display);
            font-weight: 800;
            color: var(--text-title);
            letter-spacing: -0.045em;
            line-height: var(--leading-tight);
            margin: 0 0 0.55rem 0;
        }

        .page-subtitle {
            color: var(--text-body);
            font-size: var(--text-lead);
            font-weight: 400;
            line-height: var(--leading-body);
            max-width: 40rem;
            margin: 0;
            letter-spacing: -0.01em;
        }

        /* Vertical rhythm between major bands (used with section_spacer()) */
        .section-spacer--sm { height: 0.65rem; }
        .section-spacer--md { height: 1.2rem; }
        .section-spacer--lg { height: 2.15rem; }
        .section-spacer--xl { height: 2.75rem; }

        /* —— KPI —— */
        .kpi-card {
            background: linear-gradient(165deg, #ffffff 0%, #f7faf9 100%);
            border: 1px solid rgba(24, 75, 84, 0.11);
            border-radius: var(--radius-lg);
            padding: 1.2rem 1.3rem 1.15rem 1.3rem;
            min-height: 120px;
            box-shadow:
                0 1px 0 rgba(255, 255, 255, 0.9) inset,
                0 8px 32px rgba(8, 42, 48, 0.08),
                0 2px 10px rgba(8, 42, 48, 0.04);
            margin-bottom: 0.5rem;
            position: relative;
            overflow: hidden;
            transition: box-shadow 0.22s ease, transform 0.22s ease, border-color 0.22s ease;
        }

        .kpi-card::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background: linear-gradient(180deg, var(--accent) 0%, #3a9e91 100%);
            border-radius: 4px 0 0 4px;
        }

        .kpi-card:hover {
            border-color: rgba(24, 75, 84, 0.14);
            box-shadow:
                0 1px 0 rgba(255, 255, 255, 0.95) inset,
                0 12px 40px rgba(8, 42, 48, 0.1),
                0 4px 14px rgba(8, 42, 48, 0.05);
            transform: translateY(-2px);
        }

        /* Primary KPI row: slightly larger numbers + stronger frame */
        .kpi-card--emphasis {
            min-height: 132px;
            padding-top: 1.3rem;
            border-color: rgba(24, 75, 84, 0.13);
            background: linear-gradient(165deg, #ffffff 0%, #f4faf9 100%);
        }

        .kpi-card--emphasis::before {
            width: 5px;
            background: linear-gradient(180deg, #7ad4c8 0%, var(--accent) 45%, #2a8f82 100%);
        }

        .kpi-label {
            color: var(--text-muted);
            font-size: 0.6875rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 0.55rem;
            padding-left: 0.45rem;
            line-height: var(--leading-snug);
        }

        .kpi-value {
            color: var(--text-title);
            font-size: var(--text-kpi-value);
            font-weight: 800;
            line-height: var(--leading-tight);
            font-variant-numeric: tabular-nums;
            padding-left: 0.45rem;
            letter-spacing: -0.03em;
        }

        .kpi-card--emphasis .kpi-value {
            font-size: var(--text-kpi-value-lg);
        }

        /* —— Panels —— */
        .section-heading {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            color: var(--text-title);
            font-size: var(--text-section);
            font-weight: 700;
            letter-spacing: -0.025em;
            margin: 0.1rem 0 0.65rem 0;
            padding-bottom: 0.65rem;
            border-bottom: 1px solid rgba(24, 75, 84, 0.075);
            line-height: var(--leading-snug);
        }

        .section-heading::before {
            content: "";
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: linear-gradient(145deg, #8fe0d4 0%, var(--accent) 55%, #2a8f82 100%);
            box-shadow: 0 0 0 3px rgba(103, 200, 187, 0.22);
            flex-shrink: 0;
        }

        /* Chart / table: stronger glass + crisp edge so charts don’t melt into the page */
        [data-testid="stMain"] div[data-testid="stVerticalBlockBorderWrapper"] {
            margin-bottom: var(--space-section) !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: linear-gradient(
                165deg,
                rgba(255, 255, 255, 0.92) 0%,
                rgba(255, 255, 255, 0.78) 100%
            ) !important;
            backdrop-filter: blur(22px) saturate(170%);
            -webkit-backdrop-filter: blur(22px) saturate(170%);
            border: 1px solid rgba(24, 75, 84, 0.12) !important;
            border-radius: var(--radius-lg) !important;
            box-shadow:
                0 0 0 1px rgba(255, 255, 255, 0.55) inset,
                0 1px 0 rgba(255, 255, 255, 0.65) inset,
                0 14px 44px -12px rgba(6, 32, 38, 0.22),
                0 6px 20px rgba(8, 42, 48, 0.08) !important;
            padding: 0.85rem 1rem 1.1rem 1rem !important;
        }

        /* Plotly sits on a faint “mat” so the figure edge is visible inside the glass */
        [data-testid="stMain"] [data-testid="stPlotlyChart"] {
            border-radius: var(--radius-md);
            border: 1px solid rgba(24, 75, 84, 0.07);
            background: rgba(255, 255, 255, 0.55);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.75);
            padding: 0.35rem 0.4rem 0.15rem 0.4rem;
            margin-top: 0.15rem;
        }

        /* Data grid: force light clinical theme (overrides dark / system styling) */
        div[data-testid="stDataFrame"] {
            border-radius: var(--radius-md);
            overflow: hidden;
            border: 1px solid rgba(24, 75, 84, 0.1);
            box-shadow:
                inset 0 1px 0 rgba(255, 255, 255, 0.85),
                0 2px 10px rgba(8, 42, 48, 0.06);
            background: #ffffff !important;
            margin-top: 0.15rem;
            --gdg-bg-cell: #ffffff !important;
            --gdg-bg-bubble: #f2faf8 !important;
            --gdg-bg-header: #e4f2ef !important;
            --gdg-bg-header-has-focus: #d4ebe6 !important;
            --gdg-border-color: #c5ddd7 !important;
            --gdg-text-dark: #1a3340 !important;
            --gdg-text-medium: #3d5c66 !important;
            --gdg-text-light: #5f7a82 !important;
            --gdg-text-group-header: #0f3d45 !important;
            --gdg-accent-color: #2a8f82 !important;
            --gdg-accent-light: rgba(42, 143, 130, 0.16) !important;
            --gdg-accent-fg: #ffffff !important;
            --gdg-link-color: #0b5c52 !important;
            --gdg-font-family: "DM Sans", system-ui, sans-serif !important;
            --gdg-header-font-style: 600 12px !important;
            --gdg-editor-font-size: 13px !important;
        }

        /* Glide theme vars are often applied on an inner wrapper — mirror here */
        div[data-testid="stDataFrame"] > div {
            --gdg-bg-cell: #ffffff !important;
            --gdg-bg-bubble: #f2faf8 !important;
            --gdg-bg-header: #e4f2ef !important;
            --gdg-bg-header-has-focus: #d4ebe6 !important;
            --gdg-border-color: #c5ddd7 !important;
            --gdg-text-dark: #1a3340 !important;
            --gdg-text-medium: #3d5c66 !important;
            --gdg-text-light: #5f7a82 !important;
            --gdg-text-group-header: #0f3d45 !important;
            --gdg-accent-color: #2a8f82 !important;
            --gdg-accent-light: rgba(42, 143, 130, 0.16) !important;
            --gdg-accent-fg: #ffffff !important;
            --gdg-link-color: #0b5c52 !important;
            --gdg-font-family: "DM Sans", system-ui, sans-serif !important;
        }

        /* Tabs */
        [data-testid="stMain"] [data-testid="stWidgetLabel"] p {
            font-weight: 600 !important;
            letter-spacing: -0.015em !important;
            color: var(--text-title) !important;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.35rem;
            background: rgba(232, 247, 244, 0.65);
            padding: 0.4rem;
            border-radius: var(--radius-md);
            border: 1px solid rgba(24, 75, 84, 0.08);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.7);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 10px !important;
            font-weight: 600 !important;
            color: var(--text-muted) !important;
        }

        .stTabs [aria-selected="true"] {
            background: #ffffff !important;
            color: var(--teal-deep) !important;
            box-shadow: var(--shadow-sm) !important;
        }

        /* Buttons & alerts */
        .stButton > button {
            border-radius: var(--radius-md) !important;
            font-weight: 700 !important;
            border: none !important;
            background: linear-gradient(135deg, var(--teal-deep) 0%, #1f5f6a 100%) !important;
            color: #ffffff !important;
            padding: 0.45rem 1.1rem !important;
            box-shadow: 0 4px 14px rgba(24, 75, 84, 0.25) !important;
        }

        .stButton > button:hover {
            box-shadow: 0 6px 20px rgba(24, 75, 84, 0.32) !important;
        }

        div[data-testid="stAlert"] {
            border-radius: var(--radius-md) !important;
            border: 1px solid var(--border-soft) !important;
        }

        /* Badges */
        .badge-high {
            display: inline-block;
            padding: 6px 14px;
            border-radius: var(--radius-pill);
            background: linear-gradient(180deg, #ffeef0 0%, #ffe6e8 100%);
            color: #b42318;
            font-weight: 700;
            font-size: 0.82rem;
            border: 1px solid rgba(235, 106, 106, 0.25);
        }

        .badge-medium {
            display: inline-block;
            padding: 6px 14px;
            border-radius: var(--radius-pill);
            background: linear-gradient(180deg, #fff8e8 0%, #fff4d8 100%);
            color: #a15c07;
            font-weight: 700;
            font-size: 0.82rem;
            border: 1px solid rgba(241, 180, 88, 0.35);
        }

        .badge-low {
            display: inline-block;
            padding: 6px 14px;
            border-radius: var(--radius-pill);
            background: linear-gradient(180deg, #eefbf9 0%, #def7f3 100%);
            color: #0f766e;
            font-weight: 700;
            font-size: 0.82rem;
            border: 1px solid rgba(105, 184, 175, 0.35);
        }

        /* Insight / prose blocks */
        .insight-block {
            background: linear-gradient(135deg, #fafdfd 0%, #f3faf9 100%);
            border: 1px solid var(--border-soft);
            border-radius: var(--radius-md);
            padding: 1rem 1.15rem;
            margin-top: 0.5rem;
        }

        .insight-block h3 {
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--text-muted) !important;
            margin: 0 0 0.65rem 0;
        }

        .insight-list {
            margin: 0;
            padding-left: 1.1rem;
            color: var(--text-title);
            font-size: 0.95rem;
            line-height: 1.65;
        }

        .insight-list li {
            margin-bottom: 0.35rem;
        }

        .hint-text {
            font-size: 0.88rem;
            color: var(--text-muted);
            margin-top: 0.35rem;
        }

        [data-testid="stMain"] [data-baseweb="select"] > div {
            border-radius: var(--radius-md) !important;
            border-color: #cfe3e0 !important;
        }

        [data-testid="stMain"] .stTextInput input {
            border-radius: var(--radius-md) !important;
            border-color: #cfe3e0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def format_currency(x):
    return f"${x:,.0f}"


def render_kpi(col, label, value, *, emphasis: bool = False):
    mod = " kpi-card--emphasis" if emphasis else ""
    with col:
        st.markdown(
            f"""
            <div class="kpi-card{mod}">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def section_spacer(size: str = "md") -> None:
    """Vertical rhythm between hero / KPI bands and chart sections."""
    cls = {
        "sm": "section-spacer--sm",
        "md": "section-spacer--md",
        "lg": "section-spacer--lg",
        "xl": "section-spacer--xl",
    }.get(size, "section-spacer--md")
    st.markdown(
        f'<div class="section-spacer {cls}" aria-hidden="true"></div>',
        unsafe_allow_html=True,
    )


def priority_badge(value):
    if str(value).lower() == "high":
        return '<span class="badge-high">High</span>'
    if str(value).lower() == "medium":
        return '<span class="badge-medium">Medium</span>'
    return '<span class="badge-low">Low</span>'


def apply_sidebar_filters(df):
    st.sidebar.markdown('<p class="sidebar-filters-label">Data filters</p>', unsafe_allow_html=True)

    orgs = sorted(df["organization_name"].dropna().astype(str).unique().tolist())
    providers = sorted(df["provider_name"].dropna().astype(str).unique().tolist())
    priorities = sorted(df["financial_priority_bucket"].dropna().astype(str).unique().tolist())
    ages = sorted(df["claim_age_bucket"].dropna().astype(str).unique().tolist())
    statuses = sorted(df["status_primary"].dropna().astype(str).unique().tolist())

    selected_orgs = st.sidebar.multiselect("Organization", orgs)
    selected_providers = st.sidebar.multiselect("Provider", providers)
    selected_priorities = st.sidebar.multiselect("Priority bucket", priorities)
    selected_ages = st.sidebar.multiselect("Age bucket", ages)
    selected_statuses = st.sidebar.multiselect("Primary status", statuses)

    min_out = float(df["latest_outstanding"].min()) if len(df) else 0.0
    max_out = float(df["latest_outstanding"].max()) if len(df) else 1.0
    if min_out == max_out:
        max_out = min_out + 1.0

    out_range = st.sidebar.slider(
        "Latest outstanding range",
        min_value=float(min_out),
        max_value=float(max_out),
        value=(float(min_out), float(max_out)),
    )

    claim_search = st.sidebar.text_input("Search claim ID", placeholder="Type to filter…")

    filtered = df.copy()

    if selected_orgs:
        filtered = filtered[filtered["organization_name"].isin(selected_orgs)]
    if selected_providers:
        filtered = filtered[filtered["provider_name"].isin(selected_providers)]
    if selected_priorities:
        filtered = filtered[filtered["financial_priority_bucket"].isin(selected_priorities)]
    if selected_ages:
        filtered = filtered[filtered["claim_age_bucket"].isin(selected_ages)]
    if selected_statuses:
        filtered = filtered[filtered["status_primary"].isin(selected_statuses)]

    filtered = filtered[
        (filtered["latest_outstanding"] >= out_range[0]) &
        (filtered["latest_outstanding"] <= out_range[1])
    ]

    if claim_search:
        filtered = filtered[
            filtered["claim_id"].astype(str).str.contains(claim_search, case=False, na=False)
        ]

    return filtered
